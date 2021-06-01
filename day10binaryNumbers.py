#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    number=list(bin(n))
    number=number[2:]
    
    count=0
    maximum=0
    for i in range(len(number)):
        if number[i]=='1':
            count+=1
        else:
            if maximum < count:
                maximum=count
            count=0
            
    if maximum < count:
        print(count)
    else:
        print(maximum)
