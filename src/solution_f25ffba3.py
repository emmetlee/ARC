# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:26:33 2019

@author: emmetlee
"""
import sys
import json
import numpy as np


def solve(grid):
    """Call solve() function """
    
    #Open the json file passed into the solve function
    d1 = json.load (open(grid))
    
    #Work out the shape and size of the input dictionary
    tmpd1 = {k: len(v) for k,v in d1.items()}
    lengths1 = [lengthv for lengthv in tmpd1.values()]
    
    """Print the Output Grids for training inputs"""
    #training grids are in lengths[0]
    for x in range(lengths1[0]):
        for y in reversed(range(len(d1['train'][0]['input']))):
            output_grid2 = []       #An empty list
            if y>=(len(d1['train'][0]['input'])/2):     #bottom half of grid
                output_grid2.extend(d1['train'][x]['input'][y])
            else:
                #mirror the bottom half of the grid to the top half
                #of the output grid
                output_grid2.extend(
                        (d1['train'][x]['input'][-y+(len(d1['train'][0]['input'])-1)]))
            print(np.asarray(output_grid2))
        print(" ")    

    """Print the Output Grids for Evaluation inputs"""
    for x in range(lengths1[1]):
        for y in reversed(range(len(d1['test'][0]['input']))):
            output_grid2 = []      #An empty list
            if y>=(len(d1['train'][0]['input'])/2):    #bottom half of grid
                output_grid2.extend(d1['test'][x]['input'][y])
            else:
                #mirror the bottom half of the input grid to the top half
                #of the output grid
                output_grid2.extend(
                        (d1['test'][x]['input'][-y+(len(d1['test'][0]['input'])-1)]))
            print(np.asarray(output_grid2))
        print(" ")

"""main function will call the solve function and pass in the json"""
def main():
    """Call solve() function and pass the json
    Read the first command-line argument (after python script) 
    as the input file"""
    input_grid = sys.argv[1]
    solve(input_grid)         #pass the input file to the solve function
    
"""Call the maiin function"""    
if __name__ == "__main__":
   main()