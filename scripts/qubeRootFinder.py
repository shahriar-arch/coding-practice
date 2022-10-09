#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 00:00:08 2021

@author: shahriar
"""

x = int(input("Enter an integer: "))
ans = 0
while ans ** 3 < abs(x):
    ans += 1
if ans ** 3 != abs(x):
    print(f"{x} is not a perfect qube")
else:
    if x < 0:
        ans = -ans
    print(f"Qube root of {x} is: {ans}")

print("Finished!")
