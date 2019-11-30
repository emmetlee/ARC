# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:26:33 2019

@author: emmetlee
"""
import sys
import json
import numpy as np


#def json_convert(grid):
#    """Open json file input and return numpy array"""
#   d = json.load (open(grid))
#   return d

def solve(grid):
    """Call solve() function """
    
    #Open the json file passed into the solve function
    d1 = json.load (open(grid))

    tmpd1 = {k: len(v) for k,v in d1.items()}
    lengths1 = [lengthv for lengthv in tmpd1.values()]
    
    """Print the Output Grids for training inputs"""
    #training grids are in lengths[0]
    for x in range(lengths1[0]):
        for y in reversed(range(len(d1['train'][0]['input']))):
            output_grid2 = []
            if y>=5:
                output_grid2.extend(d1['train'][x]['input'][y])
            else:
                output_grid2.extend((d1['train'][x]['input'][-y+9]))
            print(np.asarray(output_grid2))
        print(" ")    

    """Print the Output Grids for Evaluation inputs"""
    
    for x in range(lengths1[1]):
        for y in reversed(range(len(d1['test'][0]['input']))):
            output_grid2 = []
            if y>=5:
                output_grid2.extend(d1['test'][x]['input'][y])
            else:
                output_grid2.extend((d1['test'][x]['input'][-y+9]))
            print(np.asarray(output_grid2))
        print(" ")

"""main function will call the solve function and pass in the json"""
def main():
    """Call solve() function and pass the json"""
    #Read the first command-line argument as the input file
    input_grid = sys.argv[1]
    solve(input_grid)         #pass the input file to the solve function
    
    
if __name__ == "__main__":
   main()