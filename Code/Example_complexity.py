
# For Umar
import numpy as np
#import LZ78Complexity
import KC # used for Lempel-Ziv complexity estimation
import matplotlib.pyplot as plt




# random SS
BinaryString = ["0101000100","0101000100","001011","11010"]

Z = []
for s in BinaryString:
    k = KC.calc_KC(s)
    Z.append(np.round(k,1))
    

print(Z)

