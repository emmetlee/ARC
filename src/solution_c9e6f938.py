# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:12:08 2019

@author: emmetlee
StudentID = 19240024
PTAI Assignment3
"""
import sys
import json
import numpy as np

"""The solve() function takes an input file and returns a printed solution"""
def solve(grid):
    #Open the json file passed into the solve function
    d = json.load (open(grid))

    #Work out the shape and size of the input dictionary
    tmpd = {k: len(v) for k,v in d.items()}
    lengths = [lengthv for lengthv in tmpd.values()]
    
    """Print the Output Grids for training inputs"""
    
    for i in range(lengths[1]):
        for j in range(len(d['train'][0]['input'][i])):
            #Create a new list to input the solution to
            #extend the input grid to create a larger output grid footprint
            output_grid1 = []           
            output_grid1.extend(d['train'][i]['input'][j])
            
            #iterate through the list and output to the solution grid
            for z in range(len(output_grid1)):
                output_grid1.append(output_grid1[2-z])
            #print as a numpy 2D array, rather than list
            print(np.asarray(output_grid1)) 
        print(" ")        #Add a blank line between output grids

    """Print the Output Grids for Evaluation inputs"""
    
    for i in range(lengths[0]):
        for j in range(len(d['test'][0]['input'][i])):
            #Create a new list to input the solution to
            output_grid2 = []
            output_grid2.extend(d['test'][i]['input'][j])
            
            #iterate through the list and output to the solution grid
            for z in range(len(output_grid2)):
                output_grid2.append(output_grid2[2-z])
            #print as a numpy 2D array, rather than list
            print(np.asarray(output_grid2))

"""main function will call the solve function and pass in the json"""
def main():
    """Call solve() function and pass the json
    Read the first command-line argument (after python script) 
    as the input file"""
    input_grid = sys.argv[1]
    solve(input_grid)         #pass the input file to the solve function
    
"""Call the main function"""    
if __name__ == "__main__":
   main()