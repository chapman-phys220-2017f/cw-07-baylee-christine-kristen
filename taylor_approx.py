#!/usr/bin/env python3
# Name: Baylee Mumma, Christine Outlaw, Kristen Peet
# Email: mumma103@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 7

import array_calculus as ac
import numpy as np

def taylor(x,f,i,n):
    y = len(x)
    mat = ac.derivative(x[0],x[y-1],y)
    fx = np.zeros(y) #array on zeros of length y
    def tay_matrix():
        matrix = np.eye(y)
        while True:
            matrix = np.dot(matrix,mat)
            yield matrix
    yint = np.arange(y)
    m = tay_matrix()
    fx[yint] = f[i]
    array = x[i]
    for k in range(1,n):
        matrix = next(m)
        fx += (np.dot(matrix,f)[i]*((x-array)**k)/(np.math.factorial(k)))
    return (x,fx)







