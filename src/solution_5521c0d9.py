# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 23:28:18 2019

@author: emmetlee
"""
import json

def solve(grid):
    """Call solve() function """
    
    #Open the json file passed into the solve function
    d2 = json.load (open(grid))

    tmpd2 = {k: len(v) for k,v in d2.items()}
    lengths2 = [lengthv for lengthv in tmpd2.values()]

    """Print the Output Grids for training inputs"""
    #training grids are in lengths[0]
    for x in range(lengths2[0]):
        for y in (range(len(d2['train'][0]['input']))):
            output_grid3 = []
            if ((d2['train'][x]['input'][y])!=0):
                output_grid3.extend(d2['train'][x]['input'][y-1])
            else:
                output_grid3.extend(d2['train'][x]['input'][y])
            print(output_grid3)
        print(" ")

 def get_height():
    for x in range(lengths2[0]):
        for y in (range(len(d2['train'][0]['input']))):
            output_grid3 = []
            blue = 0
            red = 0
            yellow = 0
            for z in (d2['train'][x]['input'][y]):
                if z==1:
                    blue+=1
                elif z==2:
                    red+=1
                elif z==4:
                    yellow+=1
    print(blue, red, yellow)
            
            


    #z for z in (d2['train'][x]['input'][y]) 
    
    
def main():
    """Call solve() function and pass the json"""
    output = solve("5521c0d9.json")
    



main()