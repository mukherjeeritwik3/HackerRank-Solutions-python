#!/bin/python3

import math
import os
import random
import re
import sys


def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost *(tip_percent/100)
    tax = meal_cost*(tax_percent/100)
    total_cost = tip+meal_cost+tax
    return(int(round(total_cost,0)))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))
