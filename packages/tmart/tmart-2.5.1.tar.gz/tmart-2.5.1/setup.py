# This file is part of TMart.
#
# Copyright 2022 Yulun Wu.
#
# TMart is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.




import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tmart",                     # This is the name of the package
    version="2.5.1",                       
    author="Yulun Wu",                     # Full name of the author
    description="Modelling and correcting for the adjacency effect in aquatic remote sensing",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    # packages=setuptools.find_packages(),    # List of all python modules to be installed
    packages = ['tmart','tmart.surface_rho','tmart.AEC','tmart.ancillary','tmart.ancillary.aerosolSPF','tmart.config'],
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.8',                # Minimum version requirement of the package
    # py_modules=["tmart"],             # Name of the python package
    # package_dir={'':'tmart/'},     # Directory of the source code of the package
    license_files=('license.txt'),
    install_requires=['scipy','pathos','matplotlib','netCDF4','mgrs','geopandas','requests','pandas']  # Install other dependencies if any
)