
###################The trial code#######################

S = input().strip()
try:
    bruh= int(S)
    print(bruh)
except :
    print("Bad String")
        
##########################the code that had problems ##########

# if __name__ == '__main__':

# after removing this part it started working perfecty 

#!bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    S = input().strip()
    try:
        bruh=int(S)
        print(bruh)
    except ValueError:
        print("Bad String")
