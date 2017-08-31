# This program contains functions that evaluate formulas used in geometry.
#
# Your Name
# August 22, 2014

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

def para_area(b, h):
    a = b * h
    return a

def trap_area(b, c, h):
    a = b + c / 2 * h
    return a

def rectprism_volume(w, h, l):
    v = w * h * l
    return v

def cone_volume(r, h):
    v = math.pi * r**2 * h/3
    return v

def sphere_volume(r):
    v = 4/3 * math.pi * r**3
    return v

def rectprism_area(w, l, h):
    a = 2 * (w*l+h*l+h*w)
    return a

def sphere_area(r):
    a = 4 * math.pi * r**2
    return a

def hypotenuse(a, b):
    c = 2//(a**2 + b**2) 
    return c

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(para_area(12, 6))
print(trap_area(4, 5, 6))
print(rectprism_volume(6, 7, 8))
print(cone_volume(5, 6))
print(sphere_volume(5))
print(rectprism_area(5,6,7))
print(sphere_area(8))
print(hypotenuse(2, 3))
