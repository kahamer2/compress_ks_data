"""
compress_ks_data.py

Created on Tue Sep 18 19:56:52 2018

@author: Kyle Hamer
"""

from os import getcwd, listdir, makedirs, walk
from sys import argv

# retrieves command line arguments; if none found, uses current working directory
if len(argv) == 1:
    cwd = getcwd().replace('\\', '/')
elif len(argv) == 2:
    cwd = argv[-1].replace('\\', '/')
else:
    print('Error: invalid number of command line arguments.')

# finds all instances of 'output_iter' directories in the specified directory
dirs = []
for root, subdir, file in walk(cwd):
    root = root.replace('\\', '/')
    if root.split('/')[-1] == 'output_iter':
        dirs.append(root)

# iterates through all 'output_iter' directories
for i in range(len(dirs)):
    ks_multipoles = [[], [], []]    
    
    # iterates through all folders within each 'output_iter' directory
    for folder in sorted(listdir(dirs[i])):
        folder_path = dirs[i] + '/' + folder + '/'
        iter_no = int(folder[3:])
        
        # iterates through the three files in each subdirectory
        for filename in listdir(folder_path):
            with open(folder_path + filename) as in_file:
                # parses the matrix element data
                temp = []
                for line in in_file:
                    if line[0] == '#':
                        continue
                    
                    temp.append(line.replace(',', ' ').split()) #generates 2D matrix
                    
                # appends time to diagonal Kohn-Sham elements, stores it in ks_multipoles
                diag = [str(iter_no)] + [temp[j][2*j] for j in range(len(temp))]
                ks_multipoles[int(filename[-1]) - 1].append(diag)
    
    # makes the output directory
    output_path = '/'.join(dirs[i].split('/')[:-1]) + '/ks_diagonals'
    print(output_path)
    makedirs(output_path)
    
    # generates ks_diag files
    for i in range(3):       
        filename = output_path + '/ks_diag_' + str(i + 1)
        with open(filename, 'w') as out_file:
            out_file.write('# Diagonal Kohn-Sham matrix elements corresponding to \'ks_me_multipoles.%d\'\n' % (i + 1))
            for j in range(len(ks_multipoles[i])):
                out_file.write('\t'.join(ks_multipoles[i][j]) + '\n')
