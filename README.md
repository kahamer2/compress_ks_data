# compress_ks_data
A simple script that condenses the diagonal Kohn-Sham matrix elements output from Octopus into three files.

Author: Kyle Hamer

Last Updated: September 19, 2018

Description:
This is a Python script that, when placed in a directory, will search that directory (or a directory given by a command line argument -- can be absolute or relative) for all instances of the folder 'output_iter', each of which contains the Kohn-Sham matrix elements at every time step as returned by an Octopus simulation. The program then compresses all of the folders within each 'output_iter' directory to one folder containing three files, corresponding to 'ks_me_mulitpoles.(1, 2, 3)'. Make sure to delete any previous 'ks_diagonals' folders. These files contain the real-valued diagonal Kohn-Sham matrix elements with each row corresponding to a different time step (tabulated in the first column of each file), separated by tabs. This program will not delete the 'output_iter' directory when it is finished, but it is recommended that you do so if you intend to move the output directory before further processing, as the 'output_iter' directory as is could take hours to transfer. The .py version of this program can be used in an Python IDE (it was tested and should work in both Python 2.x and 3.x), or in a Unix command line by going to your working directory and typing 'python compress_ks_data.py'. This program could take anywhere from a few seconds to a few minutes, depending on the number of folders within the 'output_iter' directory. The .exe version can be used by moving it to the directory of your choice and simply opening it.

Dependencies: os module, sys module
