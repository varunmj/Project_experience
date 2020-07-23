import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n = int(input())

def print_my_name(n):
    array =[]

    for i in range(0,n):
        print("Hello, Varun MJ")
        array.append(i)
        print("the code is executed for the "+ str(i) +"th time")
        print(array[i])

    return n

if __name__ =="__main__":
    print_my_name(n)
