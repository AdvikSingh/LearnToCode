'''
Created on 20 Oct 2019
This is to test the Map Functionality 
@author: satya
'''
def addition(n):
    return n + n

numbers = {1 , 2 , 3 , 4}

result = map(addition , numbers)

print(list(result))

lambdaResult = map(lambda x : x + x , numbers)

print(list(lambdaResult))

strn = ['mat' , 'cat' , 'bat']

strlist = map(list , strn)

print(list(strlist))

import numpy as np
arr = np.array([1, 3, 2, 4, 5])
print(arr.argsort()[-4:][::-1])

arr1 = np.array([1, 2, 3 , 4, 5 , 6])
percentileResult = np.percentile(arr1, 30)

print(percentileResult)