#!/bin/python3

import math
import os
import random
import re
import sys

def _get_hourglass_sum(grid, i, j):
    sum = 0
    sum += grid[i-1][j-1]
    sum += grid[i-1][j]
    sum += grid[i-1][j+1]
    sum += grid[i][j]
    sum += grid[i+1][j-1]
    sum += grid[i+1][j]
    sum += grid[i+1][j+1]
    return sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_hourglass_sum = -63
    for i in range(1,5):
        for j in range(1, 5):
            current_hourglass_sum = _get_hourglass_sum(arr, i, j)
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum

    print(max_hourglass_sum)    
