import numpy as np
import math

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    divisor = 0
    for i in L:
        divisor += math.e**i

    softmaxval = [((math.e**x)/divisor) for x in L]
    return softmaxval


L = [0,1,2,3,4,5,6]

print(softmax(L))
print(sum(softmax(L)))

# numpy answer from udacity
def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result

