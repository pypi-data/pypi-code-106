import numpy as np
from scipy.interpolate import RegularGridInterpolator
from numpy import genfromtxt
import h5py as h5py
import matplotlib.pyplot as plt
from numba import vectorize


class distribute:
    def __init__(self, rank, nx_old, ny_old, nz_old, nv, old_data_path, old_file_name, new_data_path, key='data'):
        self.rank = rank
        self.nx_old = nx_old
        self.ny_old = ny_old
        self.nz_old = nz_old
        self.nv = nv
        self.old_data_path = old_data_path
        self.old_file_name = old_file_name
        self.new_data_path = new_data_path
        self.key = key
        
#    @vectorize()
    def generate(self):
        print("STARTED READING for "+str(self.rank)+"\n") 
        
        # ----   READ OLD DATA    ----
        mydata = np.fromfile(self.old_data_path+self.old_file_name+'.h5', dtype="float64", count=(self.nx_old*self.ny_old*self.nz_old*self.nv))
        mydata = np.reshape(mydata, newshape=(self.nx_old, self.ny_old, self.nz_old, self.nv))

        # ----   SAVE THE CREATED DATA to the NEW DATA PATH   ----- 
        new_grid = h5py.File(self.new_data_path+self.old_file_name+'_'+str(self.rank)+'.h5', 'w')
        new_grid.create_dataset(self.key, data=np.array(mydata[:,:,:,self.rank])) 

        print("COMPLETED SAVING for "+str(self.rank)+"\n") 
