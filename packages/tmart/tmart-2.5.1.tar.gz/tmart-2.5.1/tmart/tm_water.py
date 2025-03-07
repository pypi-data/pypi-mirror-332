# This file is part of T-Mart.
#
# Copyright 2023 Yulun Wu.
#
# T-Mart is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Water 

import random
import math
import numpy as np
import pandas as pd 
import os.path

if __name__=='__main__':
    from tm_geometry import rotation_matrix, dirP_to_coord, dirC_to_dirP, angle_3d
else:
    from .tm_geometry import rotation_matrix, dirP_to_coord, dirC_to_dirP, angle_3d

# Calculate whitecap reflectance 
def find_R_wc(wl, wind_speed):

    if wind_speed > 6.5: 
        from scipy.interpolate import interp1d
        
        # interpolate whitecape factor 
        df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'ancillary/whitecap_factor.csv'))
        df_wl = df.Wavelength.to_numpy()
        df_value = df.Value.to_numpy()
        f2 = interp1d(df_wl, df_value, kind='cubic')
        whitecap_factor = f2(wl).item()
        
        # fraction of sea surface covered by whitecaps 
        F_wc = 8.75e-5 * (wind_speed - 6.33)**3
        
        R = whitecap_factor * 0.22 * F_wc
        
        return F_wc, R
    
    elif wind_speed >= 0:
        return 0, 0 
    
    else:
        print('Warning: wind-speed error when calculating whitecap reflectance ')
        return None


# Refractive index as a function of Salinity, Temeprature and Wavelength
# Source: Quan and Fry
# https://www.osapublishing.org/ao/fulltext.cfm?uri=ao-34-18-3477&id=45728

def RefraIdx(salinity,temperature,wavelength):
    '''
    Parameters
    ----------
    salinity : TYPE
        parts per thousand.
    temperature : TYPE
        Celsius.
    wavelength : TYPE
        Nanometer.

    Returns
    -------
    refractive index of water.

    '''
    n0 = 1.31405
    n1 = 1.779e-4
    n2 = -1.05e-6
    n3 = 1.6e-8
    n4 = -2.02e-6
    n5 = 15.868
    n6 = 0.0155
    n7 = -0.00423
    n8 = -4382
    n9 = 1.1455e6
      
    n_w = n0 + (n1 + n2 * temperature + n3 * temperature**2) * salinity + n4 * temperature**2 + (
        n5 + n6*salinity + n7*temperature)/wavelength + n8/(wavelength**2) + n9/(wavelength**3)
    
    return n_w


# Calculate Fresnel reflectance 
def fresnel(n_w, zenith_i): # incident zenith 

    if zenith_i >= 90:
        print('Warning: incident angle > 90 for fresnel reflection')

    # Refractive index 
    n_a = 1  # air
    # n_w = 1.34 # water
    
    # incident angle == 0
    if zenith_i == 0:
        R = ( (n_w-1)  / (n_w+1) )**2
    
    elif zenith_i < 90 and zenith_i >0:
        # for incident zenith > 0, i=incident, t=transmission 
        
        ### Fresnel's reflection (for both air&water incident) (
        n_i = n_a # incident 
        n_t = n_w # transmitted 
        
        # Transmission angle 
        sin_zenith_i = math.sin( zenith_i/ (180/math.pi))
        zenith_t = math.asin((n_i/n_t)* sin_zenith_i) * (180/math.pi)
        
        # Convert to radian
        z_i = zenith_i/ (180/math.pi)
        z_t = zenith_t/ (180/math.pi)
        
        # Reflectance 
        
        R = 0.5 * ((math.sin(z_i-z_t)/math.sin(z_i+z_t))**2 + (math.tan(z_i-z_t)/math.tan(z_i+z_t))**2)

    else:
        print('Warning: fresnel error: zenith is ' + str(zenith_i))
        R = None

    return R



# Slope in degrees to polar directions 
def eta_to_dirP(eta_a_degree, eta_c_degree):

    # Find intersectino of two arcs
    # Source: https://blog.mbedded.ninja/mathematics/geometry/spherical-geometry/finding-the-intersection-of-two-arcs-that-lie-on-a-sphere/
    
    # Take in degrees 
    a1 = dirP_to_coord(1,[eta_a_degree,0])
    a2 = np.array([0, 1, 0])
    
    c1 = dirP_to_coord(1,[eta_c_degree,90])
    c2 = np.array([1, 0, 0])
    
    N_a = np.cross(a1, a2)
    N_c = np.cross(c1, c2)
    L = np.cross(N_a, N_c)
    
    # Meaning that we only get the one that faces upwards, could be problematic for other applications!  
    if L[2] < 0:
        L = np.negative(L)
    
    return dirC_to_dirP(L) 



# Basic Cox-Munk, calculate the probability of having the given slope 
def cox_munk(slope_along_wind, slope_cross_wind, wind_speed, unit='slope'):
    '''
    
    Parameters
    ----------
    slope_along_wind : TYPE
        either slope or degree.
    slope_cross_wind : TYPE
        either slope or degree.
    wind_speed : TYPE
        wind speed in unit of m/s.
    unit : TYPE, optional
        either slope or degree.

    Returns
    -------
    p : TYPE
        normalized p (integrate to 1 over all directions).

    '''

    if unit == 'slope':
        Z_y = slope_along_wind
        Z_x = slope_cross_wind
    elif unit == 'degree':
        # Degree => Slope 
        # eta has to be slope in order to use Cox-Munk equation,  
        Z_y = math.tan(slope_along_wind / (180/math.pi))    # along wind 
        Z_x = math.tan(slope_cross_wind/ (180/math.pi))      # cross wind
    else:
        print('Warning: unit unknown in calculating cox_munk probability')
        return None
   
    
    # Slope variances 
    sigma_c_2 = 1.92 * 10**-3 * wind_speed + 0.003 # cross-wind direction 
    sigma_a_2 = 3.16 * 10**-3 * wind_speed # along-wind direction, u in the 1954 paper 
    
    # Normalized slope 
    xi = Z_x / math.sqrt(sigma_c_2) # cross wind
    eta = Z_y / math.sqrt(sigma_a_2) # along wind
    
    # Cox-Munk distribution 
    c21 = 0.01 - 0.0086*wind_speed
    c03 = 0.04 - 0.033*wind_speed
    c40 = 0.40
    c22 = 0.12
    c04 = 0.23
    
    cm_exp = math.exp(-0.5 * (xi**2 + eta**2)) * (
        1 - 0.5*c21*(xi**2 - 1)*eta - (1/6)*c03*(eta**3 - 3*eta) +
        (1/24)*c40 * (xi**4 - 6*xi**2 + 3) + (1/4) * c22 *(xi**2 - 1)*(eta**2 - 1) + 
        (1/24)*c04*(eta**4 - 6*eta**2 + 3) )
    
    p = cm_exp / (2 * math.pi * math.sqrt(sigma_a_2) * math.sqrt(sigma_c_2)) # correcpond to value corrected 
    if p < 0: p = 0
    
    return p





# Calculate the Cox-Munk slope needed to make a specular reflection 

def find_eta_P(pt_direction_op_C,sun_dir,q_collision_N_polar,wind_dir):
    '''
    Use sensor, sun, surface-normal geometry to calculate Cox-Munk slopes needed to make the specular reflection. 
    It considers wind direction 

    Parameters
    ----------
    pt_direction : TYPE
        essentially sensor viewing angle.
    sun_dir : TYPE
        DESCRIPTION.
    q_collision_N_polar : TYPE
        DESCRIPTION.
    wind_dir : TYPE
        DESCRIPTION.

    Returns
    -------
    rotated_p : TYPE
        DESCRIPTION.

    '''
    
    # Sun's direction in XYZ
    sun_dir_c = dirP_to_coord(1,sun_dir)
    
    # Direction between the photon's incoming direction and the sun 
    # When surface is flat, this is the angle
    middle_c = (pt_direction_op_C + sun_dir_c) /2 
    angle_specular = dirC_to_dirP(middle_c)
    angle_specular_c = dirP_to_coord(1,angle_specular[0:2])
    
    
    # Angle = normal + cox-munk
    # So we solve for cox-munk by (angle - normal) 
    
    axis = [math.sin((q_collision_N_polar[1])*math.pi/180),
            math.sin((q_collision_N_polar[1]-90)*math.pi/180),
            0] 
    
    theta = q_collision_N_polar[0]*math.pi/180 
    # angle_specular_c around axis, clockwise by theta
    rotated = np.dot(rotation_matrix(axis, theta), angle_specular_c)
    rotated_p = dirC_to_dirP(rotated)
    
    # Correct for wind direction, this is for sampling only 
    rotated_p[1] = rotated_p[1] + wind_dir
    if rotated_p[1] >=360:
        rotated_p[1] = rotated_p[1] - 360
    
    return rotated_p
        



# Find the angle between incident pt_direction and the sun 
# Calculate the normal needed
# Calculate needed normal relative to surface normal, taking into account wind direction  
# Convert it to eta_a and eta_c 
# Find fresnel reflectance 
# Multipied by Cox-Munk intensity 

### Calculate glint reflectance using Cox-Munk + Fresnel reflectance 
def find_R_cm(pt_direction_op_C, sun_dir, q_collision_N_polar, wind_dir, wind_speed, water_refraIdx_wl, print_on):
    '''
    

    Parameters
    ----------
    pt_direction_op_C : TYPE
        DESCRIPTION.
    sun_dir : TYPE
        DESCRIPTION.
    q_collision_N_polar : TYPE
        DESCRIPTION.
    wind_dir : TYPE
        DESCRIPTION.
    wind_speed : TYPE
        DESCRIPTION.
    water_refraIdx_wl : TYPE
        DESCRIPTION.
    print_on : TYPE
        DESCRIPTION.

    Returns
    -------
    rho_glint : TYPE
        DESCRIPTION.

    '''

    # Find eta relative to q_collision_N_polar, wind-corrected 
    # AKA the needed angle for CM
    eta_P = find_eta_P(pt_direction_op_C,sun_dir,q_collision_N_polar,wind_dir)
    if print_on: print('\neta_P, or needed Cox-Munk slope in polar: '+str(eta_P))
    
    # beta: steepest slope of the water surface facet
    beta = eta_P[0]/180*math.pi
    
    # eta_polar ==> coords ==> slopes 
    
    eta_coord = dirP_to_coord(1, eta_P[0:2])
    if print_on: print('eta_coord: '+str(eta_coord))
    
    x = eta_coord[0]
    y = eta_coord[1]
    
    eta_a = x / eta_coord[2]
    eta_c = y / eta_coord[2]
    
    if print_on: 
        print('eta_a, slope: '+str(eta_a))
        print('eta_c: '+str(eta_c))
    
    # Angle between viewing and solar angles --> used to find fresnel reflectance 
    # Surface normal is right between the two because of CM
    angle_pt_sun = angle_3d(dirP_to_coord(1,sun_dir), [0,0,0], pt_direction_op_C)
    R_specular = fresnel(water_refraIdx_wl, angle_pt_sun/2)
    p_cox_munk = cox_munk(eta_a, eta_c, wind_speed,unit='slope') 
    
    solar_zenith = sun_dir[0] /180 * math.pi
    
    rho_glint = math.pi * p_cox_munk * R_specular / (4 * math.cos(solar_zenith) * math.cos(beta)**4 )       
    

    # incident_angle = dirC_to_dirP(pt_direction_op_C) 
    # incident_zenith = incident_angle[0] /180 * math.pi
    # rho_glint2 = math.pi * p_cox_munk * R_specular / (4 * math.cos(solar_zenith) * math.cos(incident_zenith) * math.cos(beta)**4 )
    # print('rho_glint with solar_z correction: ' +str(rho_glint2))    
    
    # MC model doesn't need cos(solar_z) in the denominator because it inherently deals with it
    
    if print_on: 
        print('angle_pt_sun: '+str(angle_pt_sun))
        print('R_fresnel: '+str(R_specular))
        print('p_cox_munk: '+str(p_cox_munk))
        print('cos_solar_zenith: '+str(math.cos(solar_zenith)))
        print('cos_beta**4: '+str(math.cos(beta)**4))
        print('cox_munk reflectance: '+str(rho_glint))
    
    return rho_glint 



# Sample a random slope, not related to the sun, correct to X direction  
def sample_cox_munk(wind_speed, wind_dir):
    '''
    
    Parameters
    ----------
    wind_speed : TYPE
        wind speed in m/s.
    wind_dir : TYPE
        wind direction, same as zenith angle.

    Returns
    -------
    L : TYPE
        returned xyz coordinates 

    '''
    
    if wind_speed==0:
        return[0,0,1]
    
    else:
        # Find maximum 
        # maximum is in the downwind direction
        cm_max = 0
        for i in range(0,90):
            
            eta_a_degree = -i # make it downwind
            eta_c_degree = 0
            cm_calc = cox_munk(eta_a_degree, eta_c_degree, wind_speed, unit='degree') 

            if cm_calc >= cm_max:
                cm_max = cm_calc
            else:
                cm_max = cm_max *1.1 # in case we did not find the actual max, to be safe 
                break
            
        # Just to create it and make it greater than calc 
        cm_rand = cm_calc +1 
        
        while cm_calc < cm_rand:
            eta_a_degree = random.uniform(-90,90)    
            eta_c_degree = random.uniform(-90,90)    
            cm_calc = cox_munk(eta_a_degree, eta_c_degree, wind_speed, unit='degree')
            cm_rand = random.uniform(0,cm_max) 
        
        L = eta_to_dirP(eta_a_degree, eta_c_degree)
        
        # Correct for wind_direction 
        L[1] = L[1] + wind_dir
        if L[1] >=360:
            L[1] = L[1] - 360
        
        coords = dirP_to_coord(1, L[0:2])
        
        return coords
