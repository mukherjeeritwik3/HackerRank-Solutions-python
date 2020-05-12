#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    bins = bin(n)
    bin_num = bins[2:]
    count = 0
    longest = 0
    for i in range(len(bin_num)):
        if bin_num[i]=='1':
            count = count +1
        else:
            longest = max(longest,count)
            count = 0
    print(max(longest,count))

