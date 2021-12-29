import numpy as np
from scipy.interpolate import RegularGridInterpolator
from numpy import genfromtxt
import h5py as h5py
import matplotlib.pyplot as plt
from numba import vectorize


class interpolation:
    def __init__(self, rank, start_x, end_x, start_y, end_y, start_z, end_z, nx_old, ny_old, nz_old, nx_new, ny_new, nz_new, nv, old_data_path, old_file_name, new_data_path, new_file_name, key='data', dim=3):
        self.rank = rank
        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y
        self.start_z = start_z
        self.end_z = end_z
        self.nx_old = nx_old
        self.ny_old = ny_old
        self.nz_old = nz_old
        self.nx_new = nx_new
        self.ny_new = ny_new
        self.nz_new = nz_new
        self.nv = nv
        self.old_data_path = old_data_path
        self.old_file_name = old_file_name
        self.new_data_path = new_data_path
        self.new_file_name = new_file_name
        self.key = key
        self.dim = dim
        
#    @vectorize()
    def interPolate(self):
        print("STARTED INTERPOLATION for "+str(self.rank)+"\n") 
        
        # ----   READ OLD DATA    ----
        mydata = h5py.File(self.old_data_path+self.old_file_name+'_'+str(self.rank)+'.h5', 'r')
        mydata = np.array(mydata[self.key])
        
        # ----   Old grid   ----
        x_grid_old = np.linspace(self.start_x, self.end_x, self.nx_old, endpoint=True)
        y_grid_old = np.linspace(self.start_y, self.end_y, self.ny_old, endpoint=True)
        z_grid_old = np.linspace(self.start_z, self.end_z, self.nz_old, endpoint=True)

        # ----   NEW GRID   ----
        x_new = np.linspace(self.start_x, self.end_x, self.nx_new, endpoint=True)
        y_new = np.linspace(self.start_y, self.end_y, self.ny_new, endpoint=True)
        z_new = np.linspace(self.start_z, self.end_z, self.nz_new, endpoint=True)

        # ----   Fit INTERPOLATION FUNCTION on OLD GRID and OLD DATA
        my_interpolating_function = RegularGridInterpolator((x_grid_old, y_grid_old, z_grid_old), mydata)

        # ----   Create TEST DATA POINTS for NEW GRID    ----
        test_data = np.stack(np.meshgrid(x_new, y_new, z_new, indexing='ij'), axis=-1).reshape(-1, self.dim)

        # ----   INTERPOLATE the TEST DATA POINTS using the INTERPOLATE FUNCTION    ----
        new_data = my_interpolating_function(test_data) 

        # ----   SAVE THE INTERPOLATED DATA to the NEW DATA PATH   ----- 
        new_grid = h5py.File(self.new_data_path+self.new_file_name+'_'+str(self.rank)+'.h5', 'w')
        new_grid.create_dataset(self.key,data=np.array(new_data)) 

        print("COMPLETED INTERPOLATION for "+str(self.rank)+"\n") 
