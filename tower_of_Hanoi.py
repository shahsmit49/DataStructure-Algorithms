# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 01:56:39 2017

@author: smit
"""

#tower of hanoi

arr=["from_peg","aux_prg","to_peg"];
def tower_of_Hanoi(n,from_peg,aux_peg,to_peg):
    if n>0:
        tower_of_Hanoi(n-1,from_peg,to_peg,aux_peg);
        print('Move disk %d to %s' % (n,arr[to_peg-1]));
        tower_of_Hanoi(n-1,aux_peg,from_peg,to_peg);

no_of_disk=int(input("enter total no of disks:"));    
tower_of_Hanoi(no_of_disk,1,2,3);