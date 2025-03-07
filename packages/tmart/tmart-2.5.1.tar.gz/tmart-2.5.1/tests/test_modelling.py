

# Test adjacency effect modelling 

import tmart
import numpy as np
from Py6S.Params.atmosprofile import AtmosProfile

# Specify wavelength in nm
wl = 400

### DEM and reflectance ###
image_DEM = np.array([[0,0],[0,0]]) # in meters
image_reflectance = np.array([[0.1,0.1],[0.1,0.1]]) # unitless     
image_isWater = np.zeros(image_DEM.shape) # 1 is water, 0 is land

# Synthesize a surface object
my_surface = tmart.Surface(DEM = image_DEM,
                           reflectance = image_reflectance,
                           isWater = image_isWater,
                           cell_size = 10_000)  
                               
### Atmosphere ###
atm_profile = AtmosProfile.PredefinedType(AtmosProfile.MidlatitudeSummer) 
aerosol_type = 'Maritime'  
my_atm = tmart.Atmosphere(atm_profile, aot550 = 0, aerosol_type = 'Maritime'  )

### Create T-Mart Object ###
my_tmart = tmart.Tmart(Surface = my_surface, Atmosphere= my_atm, shadow=False)
my_tmart.set_geometry(sensor_coords=[51,50,130_000], 
                      target_pt_direction=[180,0],
                      sun_dir=[0,0])

### Multiprocessing needs to be wrapped in 'if __name__ == "__main__":' for Windows systems. 
### This can be ignored for Linux-based systems. 
if __name__ == "__main__":
    results = my_tmart.run(wl=wl, band=None, n_photon=10_000)
    
    # Calculate reflectances using recorded photon information 
    R = tmart.calc_ref(results)
    for k, v in R.items():
        print(k, '     ' , v)








