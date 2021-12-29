import interpolate as interpolate
import sys
from mpi4py import MPI
import numba
from numba import jit,njit,vectorize

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def get_args():
    import argparse

    parser =argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description= "3D Interpolation'")

    parser.add_argument('--start_x', dest='start_x', help="Starting point of the grid in X-direction", type=float)
#                         action='store_true') # ,default=False)
    parser.add_argument('--end_x', dest='end_x', help="Ending point of the grid in X-direction",type=float) #action='store_true')
                        #default=True)
    parser.add_argument('--start_y', dest='start_y', help='Starting point of the grid in Y-direction',type=float)
    parser.add_argument('--end_y', dest='end_y', help='Ending point of the grid in Y-direction',type=float)
    parser.add_argument('--start_z', dest='start_z', help='Starting point of the grid in Z-direction',type=float)
    parser.add_argument('--end_z', dest='end_z', help='Ending point of the grid in Z-direction',type=float)
    parser.add_argument('--nx_old', dest='nx_old', help="Number of points in X-direction in old grid",type=int) #action='store_true')
    parser.add_argument('--ny_old', dest='ny_old', help="Number of points in Y-direction in old grid",type=int) #action='store_true')
    parser.add_argument('--nz_old', dest='nz_old', help="Number of points in Z-direction in old grid",type=int) #action='store_true')
    parser.add_argument('--nx_new', dest='nx_new', help="Number of points in X-direction in new grid",type=int) #action='store_true')
    parser.add_argument('--ny_new', dest='ny_new', help="Number of points in Y-direction in new grid",type=int) #action='store_true')
    parser.add_argument('--nz_new', dest='nz_new', help="Number of points in Z-direction in new grid",type=int) #action='store_true')
    parser.add_argument('--nv', dest='nv', help="Number of variables in the data",type=int) #action='store_true')
    parser.add_argument('--old_data_path', dest='old_data_path', help="Path where the old data is present",type=str)#, action='store_true')
    parser.add_argument('--new_data_path', dest='new_data_path', help="Path where the new data is present",type=str)#, action='store_true')
    parser.add_argument('--key', dest='key', help="Key is required to store the output data in HDF5 format (For optimal data storing)", type=str, default='data') #action='store_true', default='data')

    args = parser.parse_args()

    return args

@jit(parallel=True)
def main():
    args = get_args()
    ip = interpolate.interpolation(rank,args.start_x,args.end_x,args.start_y,args.end_y,args.start_z,args.end_z,args.nx_old,args.ny_old,args.nz_old,args.nx_new,args.ny_new,args.nz_new,args.nv,args.old_data_path,args.new_data_path)
    ip.interPolate()
    
if __name__ == "__main__":
    main()
