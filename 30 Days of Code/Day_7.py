#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    b = ""
    for i in range(len(arr)):
        b = b+str(arr[i])+" "
    print(b)
