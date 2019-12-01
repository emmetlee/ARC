# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 23:28:18 2019

@author: emmetlee
"""
import sys
import json
import numpy as np

def solve(grid):
    """Call solve() function """
    
    #Open the json file passed into the solve function
    d2 = json.load (open(grid))

    tmpd2 = {k: len(v) for k,v in d2.items()}
    lengths2 = [lengthv for lengthv in tmpd2.values()]

    """Print the Output Grids for training inputs"""
    #Convert the training dict value to a numpy array
    train_array = np.asarray(d2['train'][0]['input'])
   
    for x in range(lengths2[0]):
        for y in (range(len(train_array))):
            output_grid3 = []
            output_grid3.extend(d2['train'][x]['output'][y])
            #train_height = get_height(train_array)
            #np.add(output_grid3(y), (get_height(train_array)[y]))
                        
            #print as a numpy 2D array, rather than list
            
            print(np.asarray(output_grid3))
        print(" ")
        
    """ Print the Output grids for Test inputs"""
    #Convert the test dict value to a numpy array
    test_array = np.asarray(d2['test'][0]['input'])
    test_height = get_height(test_array)

    for x in range(lengths2[1]):
        for y in range(len(test_array)):
            output_grid3 = []
            #np.add(output_grid3, (test_height))
            output_grid3.extend(d2['test'][x]['input'][y])
            #output_grid3[:,y]+(test_height[y])
            #output_grid3.append(output_grid3,test_height)
            
            #print as a numpy 2D array, rather than list
            #print(np.asarray(output_grid3)) 
            
            #if ynp.add((output_grid3[:,y],(get_height(train_array)))
            print(np.asarray(output_grid3))
        print(" ")

"""Function to get the height of each shape in each column of the input grid"""
def get_height(grid):
     #Get the height of each column in the grid
     heights = (len(grid)) -(grid !=0).argmax(axis=0)
     return(heights)
            

def main():
    """Call solve() function and pass the json
    Read the first command-line argument (after python script) 
    as the input file"""
    input_grid = sys.argv[1]
    solve(input_grid)         #pass the input file to the solve function
    #output = solve("5521c0d9.json")
    
"""Call the main function"""    
if __name__ == "__main__":
   main()