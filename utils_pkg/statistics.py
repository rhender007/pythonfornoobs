'''
Created on Feb 3, 2018

@author: Robert
'''
#from http.cookiejar import offset_from_tz_string
def arithmetic_mean(x,*l):
    '''This function calculates the arithmetic mean
    of non empty arbitrary number of numbers'''
    
    sum = x
    for i in l:
        sum+=i
    return sum / (1.0 + len(l))

# a= arithmetic_mean(1,3,4,5,6,7,7)
# t=(3,4,5,6,7,7)
# b= arithmetic_mean(1,*t)
# print(a)
# print(b)