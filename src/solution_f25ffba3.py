# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:26:33 2019

@author: emmetlee
"""

import json


#def json_convert(grid):
#    """Open json file input and return numpy array"""
#   d = json.load (open(grid))
#   return d

def solve(grid):
    """Call solve() function """
    
    #Open the json file passed into the solve function
    d1 = json.load (open(grid))

#    tmpd = {k: len(v) for k,v in d.items()}
#    lengths = [lengthv for lengthv in tmpd.values()]
    
    """Print the Output Grids for training inputs"""
    
#    for i in range(lengths[1]):
#        for j in range(len(d['train'][0]['input'][i])):
#            output_grid1 = []
#            output_grid1.extend(d['train'][i]['input'][j])
#            for z in range(len(output_grid1)):
#                output_grid1.append(output_grid1[2-z])
#            print(output_grid1)
#        print(" ")    

    """Print the Output Grids for Evaluation inputs"""
    
#    for i in range(lengths[0]):
#        for j in range(len(d['test'][0]['input'][i])):
#            output_grid2 = []
#            output_grid2.extend(d['test'][i]['input'][j])
#            for z in range(len(output_grid2)):
#                output_grid2.append(output_grid2[2-z])
#            print(output_grid2)
    
    #return(output_grid2)


def main():
    """Call solve() function and pass the json"""
    output = solve("f25ffba3.json")
    
    
  
main()