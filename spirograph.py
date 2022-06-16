#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:25:01 2022

@author: somi
"""

import turtle as t
import random

tim=t.Turtle()
tim.speed("fastest")
t.colormode(255)

def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    random_color=(r,g,b)
    return random_color
 
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)
draw_spirograph(5)