# This file is part of T-Mart.
#
# Copyright 2023 Yulun Wu.
#
# T-Mart is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Replacing tm
# function as second page 
# Overall control of photon movement

# T-MART: Topography-adjusted Monte-Carlo Adjacency-effect Radiative Transfer code  

import sys
import numpy as np
import pandas as pd
import random
import math
from scipy.interpolate import interp1d
from copy import copy

from .tm_move import pt_move
from .tm_OT import find_OT
from .tm_sampling import sample_Lambertian, sample_scattering, weight_impSampling
from .tm_geometry import dirP_to_coord, dirC_to_dirP, rotation_matrix, angle_3d, dirC_to_coord
from .tm_intersect import find_atm2, intersect_line_DEMtri2
from .tm_intersect import reflectance_intersect, reflectance_background, intersect_background
from .tm_water import fresnel, sample_cox_munk, find_R_cm

# Plotting 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# The class is overwritten in Tmart 
class Tmart2(): 

    def _run_single_photon_test(self,pt_id): 
        return [1,1]
    
    
    # A single photon run 
    def _run_single_photon(self,pt_id):

        if self.print_on: print("\n------- Movement 1 -------")
        
        # numpy atmospheric profile, to runs faster 
        atm_profile = self.atm_profile_wl.sort_values('Alt_bottom').to_numpy()
        
        # Initial position of the photon 
        if self.pixel == None:
            q0 = self.sensor_coords
        else:
            pixel_x = self.Surface.cell_size * (self.pixel[1] + random.random()) # X
            pixel_y = self.Surface.cell_size * (self.pixel[0] + random.random()) # Y
            q0 = self.sensor_coords + [pixel_x,pixel_y,self.pixel_elevation]
            
        # Initial moving direction of the photon
        
        if self.target_pt_direction == 'lambertian_up': 
            pt_direction = sample_Lambertian()[1]
        elif self.target_pt_direction == 'lambertian_down': 
            pt_direction = sample_Lambertian()[1]
            pt_direction[0] = pt_direction[0] + 90
        else:
            pt_direction = self.target_pt_direction
        
        pt_weight = 1_000_000
        
        # When true, exit atm 
        out = False
        
        # Optimization: when true, skip all scenarios 1 and 2
        black_surface = ((not self.Surface.reflectance.any()) and (not self.Surface.isWater.any()) and 
                         self.Surface.bg_ref[0]==0 and self.Surface.bg_ref[1]==0 and 
                         self.Surface.bg_isWater[0]==0 and self.Surface.bg_isWater[1]==0)
        
        # A numpy array to collect information, here 14 columns, local_estimate has 14 too, output only 13
        pt_stat = np.empty((0,14))     
        
        ### For loop: photon movements 
        for movement in range(0, 500): 
            
            # sample an optical thickness 
            sampled_tao = -math.log(random.random())
            
            # after moving the sampled_tao, the properties of the photon and the atmosphere layer 
            q1, tao_abs, ot_rayleigh_NA, ot_mie_NA, out = pt_move(atm_profile,q0,pt_direction,sampled_tao)
            # note: ot_rayleigh and ot_mie are replaced later, the accumulated ot should not be used, thus add _NA to mask them
    
            if self.print_on:
                print ('\nInitial position: ' +str(q0))
                print ('Final position: ' +str(q1))
                print ('Absorption optical thickness (OT): ' +str(tao_abs))
                print('Sampled OT: ' + str(sampled_tao))
                print ('Photon moving direction: ' +str(pt_direction))
                print('If out of atmosphere: ' + str(out)) 
            
            ### Test triangle collision             

            # If the two ends of the movement are both above the max elevation of the DEM, skip the test
            if self.Surface.DEM.max() < q0[2] and self.Surface.DEM.max() < q1[2]:
                intersect_tri = pd.DataFrame()  
                
            else:
                # intersect_tri = intersect_line_DEMtri(q0, q1, self.Surface.DEM_triangulated, self.print_on)      
                intersect_tri = intersect_line_DEMtri2(q0, q1, self.Surface.DEM_triangulated, self.print_on)      
            
            
            ###### Three scenarios 
            
            # 1 Triangle collision 
            # 2 Background collision 
            # 3 Photon movement and scattering 
            
            
            # If there is triangle intersection 
            if intersect_tri.shape[0] > 0:
                if self.print_on: print ("\nScenario 1: Triangle collision")
                scenario = 1
            
            # If no triangle intersection 
            else:      
                
                intersect_bg = intersect_background(q0, q1, self.Surface.bg_elevation) 
                intersect_bg_x = intersect_bg[0] < self.Surface.x_min or intersect_bg[0] > self.Surface.x_max
                intersect_bg_y = intersect_bg[1] < self.Surface.y_min or intersect_bg[1] > self.Surface.y_max
                
                # if xy of intersecting background is outside the triangles on X or Y axies 
                if q1[2]<self.Surface.bg_elevation and (intersect_bg_x or intersect_bg_y):     
                    if self.print_on: print ("\nScenario 2: Background collision")
                    scenario = 2 
                else: 
                    if self.print_on: print ("\nScenario 3: Photon movement and scattering ")
                    scenario = 3 
            
            
            ### Black surface acceleration
            if (scenario == 1 or scenario == 2) and black_surface: 
                if self.print_on: print ("\n=== Black surface acceleration, exit ===")
                break

            
            ### Triangle Collision 
            if scenario == 1:
                
                rotated_cm = None
                
                # Find triangle with the shortest distance and the exact collision point
                intersect_tri_chosen = intersect_tri.iloc[intersect_tri.linear_distance.idxmin()] 
                q_collision = intersect_tri_chosen.tolist()[0:3]  
                
                if self.print_on: print('Collision position: ' + str(q_collision))    
                
                # Re-calculate absorption 
                tao_abs = find_OT(q0,q_collision,atm_profile)
                tao_abs = tao_abs / abs(math.cos(pt_direction[0]/180*math.pi))  
                
                # Avoid intersecting again
                q_collision[2] = q_collision[2] + 0.01 
                
                # Direction of normal to the triangle 
                q_collision_N = intersect_tri_chosen.tolist()[3:6] 
                q_collision_N_polar = dirC_to_dirP(q_collision_N)
                
                if self.print_on:
                    print("\nNormal to collision: " + str(q_collision_N))
                    print("Normal to collision polar: " + str(q_collision_N_polar))                
                
                # Find the reflectance at the collision point 
                q_collision_ref = reflectance_intersect(q_collision, self.Surface.reflectance, 
                                                        self.Surface.cell_size, self.Surface.bg_ref, 
                                                        self.Surface.bg_coords)
                if self.print_on: print("Reflectance at collision position: " + str(q_collision_ref))    
                
            
                ### If water --> there is a chance of specular reflectance             
                # Chance is determined by Fresnel, pt_weight stays as 1
                # Use pt_direction, q_collision_N and Cox-Munk to calculate the new pt_direction 
                
                # Test if it's water at the collision point 
                q_collision_isWater = reflectance_intersect(q_collision, self.Surface.isWater, 
                                                            self.Surface.cell_size, self.Surface.bg_isWater, 
                                                            self.Surface.bg_coords)    
                if self.print_on: print('\nIf surface is water: '+str(q_collision_isWater))
                
    
                # By default, non-specular. If chance, switch on 
                specular_on = False
                
                # If water, calculate Fresnel reflectance and if specular reflection   
                # q_collision_ref is now R0+
                if q_collision_isWater == 1:
                    
                    # Opposite to pt_direction in XYZ coordinates, only for isWater scenarios 
                    pt_direction_op_C = np.negative(dirP_to_coord(1, pt_direction)) 
                    
                    # If an impossible angle (CM does it sometimes), re-randomize
                    in_angle = 100 # just an impossible incident angle 
                    while in_angle>90: 
                    
                        # Use Cox-munk to draw a normal, output polar coordinates 
                        random_cox_munk = sample_cox_munk(self.wind_speed, self.wind_dir)
                        
                        # Azimuthally averaged sampling 
                        if self.wind_azi_avg:
                            random_cox_munk2 = sample_cox_munk(self.wind_speed, self.wind_dir+90)
                            random_cox_munk = (random_cox_munk + random_cox_munk2) / 2
                        
                        
                        axis = [math.cos((q_collision_N_polar[1]+90)*math.pi/180),
                                math.cos(q_collision_N_polar[1]*math.pi/180),
                                0] 
                        theta = q_collision_N_polar[0]*math.pi/180
                        
                        # tilt cox_munk to the existing polar_N as a new normal 
                        rotated_cm = np.dot(rotation_matrix(axis, theta), random_cox_munk)                    
    
                        # incident angle to calculate Fresnel reflectance 
                        in_angle = angle_3d(rotated_cm, [0,0,0], pt_direction_op_C)
                        
                    # Specular reflectance                     
                    R_specular = fresnel(self.water_refraIdx_wl, in_angle)
                    
                    # Total surface reflectance
                    R_surf = self.R_wc_wl + (1-self.F_wc_wl) * R_specular 
                    
                    # Modify reflectance, use the original one as R0+ in the absence of white caps 
                    # '(1-self.F_wc_wl) * q_collision_ref' is R0+ in the presence of white caps 
                    q_collision_ref = R_surf + (1-self.F_wc_wl) * q_collision_ref
                    
                    # If chance (R_specular) out of q_collision_ref, siwtch on specular_on
                    specular_on = random.uniform(0,q_collision_ref) < R_specular
                    # specular_on = True # for testing
                    
                    if self.print_on: 
                        print('random_cox_munk: ' + str(random_cox_munk))
                        print("Rotated_cox_munk: " + str(rotated_cm)) 
                        print('Incident angle: ' + str(in_angle))
                        print('F_whitecap: ' + str(self.F_wc_wl))
                        print('R_whitecap: ' + str(self.R_wc_wl))
                        print('R_fresnel: ' + str(R_specular))
                        print('R_surf: ' + str(R_surf))
                        print('specular_on: ' + str(specular_on))
                        # print("Modified reflectance at collision position: " + str(q_collision_ref))  
                          
                pt_weight = pt_weight * q_collision_ref
                 
                # If water and specular 
                if q_collision_isWater == 1 and specular_on:
                    if self.print_on: print('\n== Specular reflection ==')  
                    
                    # Rotate pt_direction_op_C  around rotated_cm by 180 degrees       
                    rotated = np.dot(rotation_matrix(rotated_cm, math.pi), pt_direction_op_C)
       
                    # pt_direction is the specular reflection of the original direction at the new normal 
                    pt_direction = dirC_to_dirP(rotated)[0:2]
                    tpye_collision = 'Ws' # water specular
                    
                # Else lambertian 
                else: 
                    
                    # Sample a direction and tilt it to the surface normal 
    
                    random_lambertian = sample_Lambertian()
    
                    # axis is azimuthal, clockwise 90 degrees
                    axis = [math.cos((q_collision_N_polar[1]+90)*math.pi/180),
                            math.cos(q_collision_N_polar[1]*math.pi/180),
                            0] 
                    theta = q_collision_N_polar[0]*math.pi/180 #math.pi  # zenith
                    
                    # 000 at the bottom, axis on top, clockwise move
                    rotated = np.dot(rotation_matrix(axis, theta), random_lambertian[0])
                    
                    pt_direction = dirC_to_dirP(rotated)[0:2]
                    tpye_collision = 'W'  # water lambertian 
                    
                    if self.print_on:
                        print("\nRandom_lambertian: " + str(random_lambertian))
                        print("Rotated_lambertian: " + str(rotated)) 
                        # print("q_collision_ref: " + str(q_collision_ref))
                        
                if self.print_on: print("Photon weight before absorption: " + str(pt_weight))      
                
                
            ### Background collision     
            elif scenario == 2:
                
                # For plotting, not used 
                rotated, rotated_cm, intersect_tri_chosen, q_collision_N = None, None, None, None 
                q_collision_N_polar = [0,0] 
                
                
                q_collision = intersect_bg 
                if self.print_on: print('Collision position: ' + str(q_collision))  
                
                # re-calculate absorption 
                tao_abs = find_OT(q0,q_collision,atm_profile)
                tao_abs = tao_abs / abs(math.cos(pt_direction[0]/180*math.pi))                
                  
                # Avoid intersecting again
                q_collision[2] = q_collision[2] + 0.01 
    
                # Reflectance of the background at the collision point 
                q_collision_ref = reflectance_background(q_collision,self.Surface.bg_ref, self.Surface.bg_coords)
                if self.print_on:
                    print ('\nOut of the padded DEM')
                    print("Reflectance at collision position: " + str(q_collision_ref))
                
                # Test if it's water at the collision point 
                q_collision_isWater = reflectance_intersect(q_collision, self.Surface.isWater, 
                                                            self.Surface.cell_size, self.Surface.bg_isWater, 
                                                            self.Surface.bg_coords)    
                if self.print_on: print('\nIf surface is water: '+str(q_collision_isWater))                    
                specular_on = False
                
                # If water, calculate Fresnel reflectance and if specular reflection   
                # q_collision_ref is now R0-
                if q_collision_isWater == 1:
                    
                    # Opposite to pt_direction in XYZ coordinates, only for isWater scenarios 
                    pt_direction_op_C = np.negative(dirP_to_coord(1, pt_direction)) 
                                        
                    # If an impossible angle (CM does it sometimes), re-randomize
                    in_angle = 100 # just an impossible incident angle 
                    while in_angle>90: 
                        
                        # Use Cox-munk to draw a normal, no need for rotation
                        random_cox_munk = sample_cox_munk(self.wind_speed, self.wind_dir)
                        
                        # Azimuthally averaged sampling 
                        if self.wind_azi_avg:
                            random_cox_munk2 = sample_cox_munk(self.wind_speed, self.wind_dir+90)
                            random_cox_munk = (random_cox_munk + random_cox_munk2) / 2                        
                                       
                        # incident angle to calculate Fresnel reflectance 
                        in_angle = angle_3d(random_cox_munk, [0,0,0], pt_direction_op_C)
                    
                    R_specular = fresnel(self.water_refraIdx_wl, in_angle)
                    R_surf = self.R_wc_wl + (1-self.F_wc_wl) * R_specular # total surface reflectance
                    
                    # modify reflectance, use the original q_collision_ref as R0+
                    q_collision_ref = R_surf + (1-self.F_wc_wl) * q_collision_ref
                    
                    # if chance (R_specular) out of q_collision_ref, siwtch on specular_on
                    specular_on = random.uniform(0,q_collision_ref) < R_specular
      
                    if self.print_on: 
                        print('random_cox_munk: ' + str(random_cox_munk))
                        print('Incident angle: ' + str(in_angle))
                        print('F_whitecap: ' + str(self.F_wc_wl))
                        print('R_whitecap: ' + str(self.R_wc_wl))
                        print('R_fresnel: ' + str(R_specular))
                        print('R_surf: ' + str(R_surf))
                        print('specular_on: ' + str(specular_on))   
                        # print("Modified reflectance at collision position: " + str(q_collision_ref))  
                
                pt_weight = pt_weight * q_collision_ref   
                
                # if water and specular 
                if q_collision_isWater == 1 and specular_on:
                    if self.print_on: print('\n== Specular reflection ==')  
                        
                    rotated = np.dot(rotation_matrix(random_cox_munk, math.pi), pt_direction_op_C)
       
                    pt_direction = dirC_to_dirP(rotated)[0:2]
                    tpye_collision = 'Ws'
                    
                # else lambertian 
                else: 
                    # pt_direction = dirC_to_dirP(sample_Lambertian()[0])[0:2] # the line below can be faster???
                    pt_direction = sample_Lambertian()[1]
                    tpye_collision = 'W'
                        
                if self.print_on: print("Photon weight before absorption: " + str(pt_weight))               
            
            
            ### Photon movement and scattering 
            elif scenario == 3:
                q_collision = q1
                
                ### Find ot_mie and ot_rayleigh
                ot_rayleigh, ot_mie = find_atm2(atm_profile,q1)
                pt_direction_op_C = np.negative(dirP_to_coord(1, pt_direction))
                
                # regular sampling  
                if random.random() >= self.VROOM:
                    if self.print_on: print('\n== Regular Sampling ==')  
                    pt_direction, scatt_intensity, type_scat = sample_scattering(ot_mie, ot_rayleigh, pt_direction, self.aerosol_SPF_wl, self.print_on)
    
                # importance sampling 
                else:
                    if self.print_on: print('\n== Importance Sampling ==')  
                    
                    # Force mie scattering when importance sampling 
                    pt_direction, scatt_intensity, type_scat = sample_scattering(1, 0, self.sun_dir, self.Atmosphere.aerosol_SPF, self.print_on)
                    
                    
                    # angle between the old direction and the importance-sampled direction --> Scattering angle 
                    angle_impSampling = angle_3d(dirP_to_coord(1,pt_direction), [0,0,0], pt_direction_op_C)
                    
                    scatt_intensity_impSampling = weight_impSampling(ot_mie,ot_rayleigh,angle_impSampling,self.Atmosphere.aerosol_SPF, self.print_on)
                    
                    if self.print_on: print("  pt_weight before adjustment: " + str(pt_weight))
                    if self.print_on: print("  adjustment factor: " + str(scatt_intensity_impSampling/scatt_intensity))
                    pt_weight = pt_weight * (scatt_intensity_impSampling/scatt_intensity)
 
                
            
            ###### Calculate absorption 
          
            T_abs = math.exp(-tao_abs) # tao_abs is unchanged if scenario 3 because the whole segment was used
            pt_weight = pt_weight * T_abs
            
            if self.print_on:
                print('\n== Calculating absorption ==')
                print("Modified absorption OT: " + str(tao_abs))
                print("Absorption transmittance: " + str(T_abs))
                print("Photon weight: " + str(pt_weight))
                
                      
            
            ###### Local estimates 
            
            # Every movement has a row of local_est
            # Columes: pt_id, movement, L_cox-munk, L_whitecap, L_water, L_land, L_rayleigh, L_mie, surface xyz, shadowed, if_env, type of collision
            # Type of collision: W (water leaving), Ws (water specular), L (land), M (mie), R (Rayleigh)
            
            
            if_shadow = False
            
            # Reflection 
            if scenario == 1 or scenario == 2: 
                if self.print_on: print('\n== Calculating local estimate ==')
                
                if movement == 0:
                    is_env = 0
                else: # move>0 means at least one atmospheric scattering happened
                    is_env = 1
                
                if self.shadow: if_shadow = self.detect_shadow(q_collision)
                
                # Water
                if q_collision_isWater==1:
                    le_water = self.local_est_water(pt_weight, pt_direction_op_C, q_collision, 
                                                    q_collision_N_polar, R_specular, q_collision_ref, R_surf)
                    local_est = [pt_id, movement] + le_water + [0,0,0] + q_collision + [0,is_env,tpye_collision]
                        
                # Land 
                else: 
                    le_land = self.local_est_land(q_collision, pt_weight)
                    local_est = [pt_id, movement,0,0,0] + le_land + [0,0] + q_collision + [0,is_env,'L']
                
                if if_shadow: local_est[11] = 1
                if self.print_on: print("local_est: " + str(local_est))
                pt_stat = np.vstack([pt_stat, local_est])     
                
            # Scattering 
            if scenario == 3 and out == False:
                if self.print_on: print('\n== Calculating local estimate ==')
                
                if self.shadow: if_shadow = self.detect_shadow(q_collision)
                le_scatt = self.local_est_scat(pt_direction_op_C, q_collision, pt_weight, ot_mie, ot_rayleigh)
                local_est = [pt_id, movement,0,0,0,0] + le_scatt + q_collision.tolist() + [0,0,type_scat]
                if if_shadow: local_est[11] = 1
                if self.print_on: print("local_est: " + str(local_est))
                pt_stat = np.vstack([pt_stat, local_est])            
            
            
            ###### Plot and out 
            
            # Plotting, only supposed to be run by self.run_plot()
            if self.plot_on:
                
                if scenario==1 or scenario == 2:
                    self._plot(q0, q_collision, scenario, intersect_tri_chosen, rotated, q_collision_N, specular_on, rotated_cm) 
                
                else: 
                    self._plot(q0, q_collision, scenario)
        
            # Exit if out 
            if out:
                if self.print_on: print('\nPhoton out of atmosphere \n')
                break
        
            if self.print_on: print("\n------- Movement {} -------".format(movement+2))  
            # the last print won't show because the code breaks above
            # +2 because it starts from the 2nd one 
    
            # starting the next movement at the collision         
            q0 = q_collision
        
        pt_stat = self._diff_ref(pt_stat)
        
        # return np.array([surface_irradiance]) # for surface_irradiance 
        return pt_stat
    

    # Differentiate reflectances
    def _diff_ref (self,pt_stat):
        
        pt_stat_num = pt_stat[:,0:13].astype(float)
        moves = pt_stat_num[:,1].astype(int)
        
        if not np.all(np.diff(moves) > 0): # check if sorted 
            sys.exit('pt movement has to be sorted')
            
        pt_stat_output = np.empty((0,13))   
            
        for move in moves:
            
            # Entire row 
            pt_movement = copy( pt_stat_num[move == moves,:] )
            
            # Type of collision 
            t_c = pt_stat[pt_stat[:,1] == str(move), 13].item()
            
            if t_c=='W' or t_c=='L':
                # Adding all after to L_whitecap, L_water, L_land
                
                # Total lambertian in a single row 
                total = np.sum(pt_movement[0][3:6])
                
                # If surface is black, quit loop to speed up calculation 
                if total == 0: 
                    break
        
                # Identify all movements after that contribute to this 
                pt_mov_after = pt_stat_num[move+1:,:]
                pt_mov_after_nonShadow = pt_mov_after[pt_mov_after[:,11]==0]
                sum_after = np.sum(pt_mov_after_nonShadow[:,2:8])
              
                # Ratios: whitecap, water and land 
                r_wc    = pt_movement[0][3]/ total 
                r_water = pt_movement[0][4]/ total 
                r_land  = pt_movement[0][5]/ total 
                
                # We calculate ratio before setting shadowed 'total' to 0
                if pt_movement[0][11] == 1: total = 0
                
                total_new = total + sum_after
            
                pt_movement[0][3] = total_new * r_wc
                pt_movement[0][4] = total_new * r_water
                pt_movement[0][5] = total_new * r_land
                
                # Add to the main numpy array 
                pt_stat_output = np.vstack([pt_stat_output, pt_movement])
                
                break 
            
            elif t_c=='Ws':    
                # Adding all after to L_coxmunk
                
                pt_mov_after = pt_stat_num[move+1:,:]
                pt_mov_after_nonShadow = pt_mov_after[pt_mov_after[:,11]==0]
                sum_after = np.sum(pt_mov_after_nonShadow[:,2:8])       
                
                if pt_movement[0][11] == 1: # shadow
                    total = 0
                else:
                    total = pt_movement[0][2]
                
                pt_movement[0][2] = total + sum_after
                
                pt_stat_output = np.vstack([pt_stat_output, pt_movement])
                
                break         
                
            # If rayleigh or mie 
            pt_stat_output = np.vstack([pt_stat_output, pt_movement])
            
        return pt_stat_output
        
    def local_est_scat(self,pt_direction_op_C,q_collision, pt_weight, ot_mie, ot_rayleigh):
        
        # calculate remaining Transmittance 
        OT = self._local_est_OT(q_collision)
        OT = OT / math.cos(self.sun_dir[0]/180*math.pi)
        T = math.exp(-OT)
        if self.print_on: print ('\nTotal transmittance for local_est: ' +str(T))
        
        # total scattering in that layer 
        ot_scattering = ot_mie + ot_rayleigh
        
        # angle between pt_direction and the sun 
        angle_pt_sun = angle_3d(dirP_to_coord(1,self.sun_dir), [0,0,0], pt_direction_op_C)
        
        # the angle needed to scatter the photon into the sun's direction 
        angle_scattering = 180 - angle_pt_sun
        
        # rayleigh 
        rayleigh = (3/4)*(1+(math.cos(angle_scattering/180*math.pi))**2)
        rayleigh_c = rayleigh / math.cos(self.sun_dir[0]/180*math.pi)  / 4 # 4 should be the right normalization 
        rayleigh_c = rayleigh_c * (ot_rayleigh/ot_scattering)
    
        # mie
        df_angle = self.aerosol_SPF_wl.Angle.to_numpy()
        df_value = self.aerosol_SPF_wl.Value.to_numpy()
        f2 = interp1d(df_angle, df_value, kind='cubic')
        mie = f2(angle_scattering).item()
        
        mie_c = mie / math.cos(self.sun_dir[0]/180*math.pi) / 4 # / math.pi   
        mie_c = mie_c * (ot_mie/ot_scattering)
        
        local_est = np.array([rayleigh_c, mie_c]) * T * pt_weight / 1_000_000   
        return local_est.tolist()

    def local_est_land(self, q_collision, pt_weight): 
    
        # Direct transmittance 
        OT = self._local_est_OT(q_collision)
        OT = OT / math.cos(self.sun_dir[0]/180*math.pi)
        T = math.exp(-OT)
        if self.print_on: print ('\nTotal transmittance for local_est: ' +str(T))
        
        local_est = pt_weight * T / 1_000_000
        return [local_est]
   
    def local_est_water(self, pt_weight, pt_direction_op_C, q_collision, q_collision_N_polar, R_specular, q_collision_ref, R_surf):   
        
        R_wc = self.R_wc_wl
        
        # Cox-Munk and Fresnel, this one tells us nothing about the actual flux reflectance!
        R_cm = find_R_cm(pt_direction_op_C, self.sun_dir, q_collision_N_polar, 
                         self.wind_dir, self.wind_speed, self.water_refraIdx_wl, self.print_on)
        
        # Average = (regular + wind 90 degrees) / 2
        if self.wind_azi_avg:
            if self.print_on: print ('\nSampling R_cm again for azimuthally averaged values')
            
            R_cm2 = find_R_cm(pt_direction_op_C, self.sun_dir, q_collision_N_polar, 
                              self.wind_dir + 90, self.wind_speed, self.water_refraIdx_wl, self.print_on)
            R_cm = (R_cm + R_cm2) / 2
            
        R_cm = (1-self.F_wc_wl) * R_cm # remove whitecaps from cox-munk reflection 
        if self.print_on:print('\nFinal cox_munk reflectance: '+str(R_cm))
        
        # Dicrect transmittance 
        OT = self._local_est_OT(q_collision)
        OT = OT / math.cos(self.sun_dir[0]/180*math.pi)
        T = math.exp(-OT)
        
        if self.print_on: print ('\nTotal transmittance for local_est: ' +str(T))
            
        # cox-munk
        pt_weight_cm = pt_weight * (R_cm / q_collision_ref) 
        
        # whitecap
        pt_weight_wc = pt_weight * (R_wc / q_collision_ref)
        
        # water-leaving, '(1-self.F_wc_wl) * q_collision_ref' AKA R0+ in the presence of white caps 
        pt_weight_lw = pt_weight * (   (q_collision_ref - R_surf) /  q_collision_ref)
            
        local_est = np.array([pt_weight_cm, pt_weight_wc, pt_weight_lw]) / 1_000_000 
            
        # Absorption 
        local_est = local_est * T 
        return local_est.tolist()
           
    
    # If the path between a point and the sun is blocked 
    def detect_shadow(self, q_collision):
        
        dist_120000 = (120_000 - q_collision[2]) / np.cos(self.sun_dir[0]/180*np.pi) 
        q_sun = dirP_to_coord(dist_120000, self.sun_dir) + q_collision
        
        intersect_tri = intersect_line_DEMtri2(q_collision, q_sun, self.Surface.DEM_triangulated, self.print_on)  
        
        if_shadow = intersect_tri.shape[0] > 0
        
        if self.print_on: print ('\nIf shaded: ' +str(if_shadow))
        
        return if_shadow
        

    # finds OT between TOA and z
    def _local_est_OT(self,q_collision): 
        
        # Altitude of the collision point  
        z = q_collision[2]
 
        # Find all layers whose bottoms are equal to or higher than z, panda series Boolean 
        alts_higher = np.array(self.atm_profile_wl.Alt_bottom *1000 >= z)

        # Calculate OTs in layers above, capital is output 
        OT_out = (sum(self.atm_profile_wl.ot_abs[alts_higher]) +  
                      sum(self.atm_profile_wl.ot_rayleigh[alts_higher]) + 
                      sum(self.atm_profile_wl.ot_mie[alts_higher]) )   

        # boolean if equal 
        alts_equal = np.array( self.atm_profile_wl.Alt_bottom * 1000 == z )
        
        if sum(alts_equal): 
            pass
        else: # Alternative: find the layer where Z is in, find OT_remain_ratio...
            
            # calculate top altitudes - collision altitude
            alts_diff = (self.atm_profile_wl.Alt_top - z/1000)
            
            alts_diff_positive_min = alts_diff[alts_diff>0].min()
            
            # edited 
            alts_diff_positive_min_idx = alts_diff[alts_diff>0].idxmin()
            height = self.atm_profile_wl.Alt_top[alts_diff_positive_min_idx] - self.atm_profile_wl.Alt_bottom[alts_diff_positive_min_idx]
            OT_remain_ratio = alts_diff_positive_min / height        
            
            OT_layer = (self.atm_profile_wl.ot_abs[alts_diff_positive_min_idx] + 
                        self.atm_profile_wl.ot_rayleigh[alts_diff_positive_min_idx] + 
                        self.atm_profile_wl.ot_mie[alts_diff_positive_min_idx]  ) 
            
            OT_abs_remain = OT_layer * OT_remain_ratio 
            OT_out = OT_out + OT_abs_remain
        return OT_out

    def _plot(self,q0,q1, scenario, intersect_tri_chosen=None, rotated=None, q_collision_N=None, specular_on=False, rotated_cm=None, linewidth=2.5):
        
        
        fig = plt.figure()
        ax = Axes3D(fig, auto_add_to_figure=False)
        fig.add_axes(ax)
        
        # ax.invert_xaxis()
        # ax.set_xlim(0, 100_000 * 1) 
        # ax.set_ylim(100_000 * 1, 0 )
        # ax.set_zlim(0, 100_000 * 1 )   
        
        ax.set_xlim(self.plot_range[0],self.plot_range[1]) 
        ax.set_ylim(self.plot_range[3],self.plot_range[2])
        ax.set_zlim(self.plot_range[4],self.plot_range[5])   
        
        ax.set_xlabel('X axis (m)')
        ax.set_ylabel('Y axis (m)')
        ax.set_zlabel('Z axis (m)')
        
        # Plotting DEM_tri
        for tri in self.Surface.DEM_triangulated:
            for row in range (0, tri.shape[2]):
                for col in range (0, tri.shape[3]):
            
                    p0 = tri[0,:,row,col] 
                    p1 = tri[1,:,row,col]
                    p2 = tri[2,:,row,col]
                    
                    plot_tri = np.array([[p0,p1,p2]])
                    
                    p_centre = (p0 + p1 + p2)/3
                    
                    q_collision_ref = reflectance_intersect(p_centre, self.Surface.reflectance, 
                                                            self.Surface.cell_size, self.Surface.bg_ref, 
                                                            self.Surface.bg_coords)    
                    
                    if q_collision_ref>1: q_collision_ref=1
                    if q_collision_ref<0: q_collision_ref=0
                    
                    poly = Poly3DCollection(plot_tri,
                                #facecolors='ivory',
                                facecolors=str(q_collision_ref),
                                linewidths=0.5,
                                edgecolors='black',
                                alpha=0.9
                                )
                    ax.add_collection3d(poly)
        

        x=[q0[0],q1[0]]
        y=[q0[1],q1[1]]
        z=[q0[2],q1[2]]
        
        cols = ['cyan','paleturquoise','honeydew','mistyrose','tomato','red']
        # cols = ['cyan','paleturquoise','honeydew','blue','blue','blue']
        n_cols = 6
        
        for i in range(n_cols):
            ax.plot([x[0] + (x[1]-x[0]) /n_cols *i  ,  x[0] + (x[1]-x[0])/n_cols*(i+1)],
                    [y[0] + (y[1]-y[0]) /n_cols *i  ,  y[0] + (y[1]-y[0])/n_cols*(i+1)],
                    zs=[z[0] + (z[1]-z[0]) /n_cols *i  ,  z[0] + (z[1]-z[0])/n_cols*(i+1)],
                    color=cols[i],
                    zorder=100, 
                    linewidth = linewidth)

        if scenario==1:
            
            # Manual length of the other two lines 
            my_length = 50_000

            if self.print_on: print ("\nPlotting triangle collision")
        
            triangle = intersect_tri_chosen.tolist()
            
            # convert normal_direction to normal_coordinates
            if specular_on:
                color_normal = 'blue'
                triangle[3:6] = dirC_to_coord(rotated_cm,triangle[0:3],my_length)
            else:
                color_normal = 'lime'
                triangle[3:6] = dirC_to_coord(triangle[3:6],triangle[0:3],my_length)
                
            # normal 
            ax.plot([triangle[0] , triangle[3]],
                    [triangle[1] ,  triangle[4]],
                    zs=[triangle[2] ,  triangle[5]],
                    color = color_normal,
                    zorder=100,
                    linewidth = linewidth
                    )
            
            # reflected direction 
            reflected_viz_q1 = triangle[0:3] + rotated * 33_000

            # new pt_direction 
            ax.plot([triangle[0] , reflected_viz_q1[0]],
                    [triangle[1] ,  reflected_viz_q1[1]],
                    zs=[triangle[2] ,  reflected_viz_q1[2]],
                    color = 'orange',
                    zorder=100,
                    linewidth = linewidth
                    )
            
            if self.print_on: print("Angle between normal and new moving direction is: " + 
                                    str(angle_3d(rotated,[0,0,0],q_collision_N)))
    
        # Plot atmospheres to the same extend as the surface 
        plt.show()
