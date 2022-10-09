#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 00:38:49 2021

@author: shahriar
"""

x = float(input("Enter a number: "))
ans = 0.0
ans2 = 0.0
limit = 0.0

while ans ** 3 < abs(x):
    ans += 1

if ans ** 3 == abs(x):
    if x < 0:
        ans = -ans
    print(f"Quberoot of {x} is: {ans}")

else:
    while ans ** 3 != abs(x):
        ans2 = (abs(x)/ans)/ans
        ans = (ans + ans2)/2
        print(f"Please wait, processing..... {ans}")
        if ans ** 3 == abs(x):
            if x < 0:
                ans = -ans
            print(f"Quberoot of {x} is: {ans}")
            break
        limit += 1
        if limit == 100000:
            ans = (abs(x)) ** (1/3)
            if x < 0:
                ans = -ans
            print(f"Quberoot of {x} is : {ans}")
            break
