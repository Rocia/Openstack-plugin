import math
import random

file = open ('a.txt', "r")
content = file.read()
asci = [ord(c) for c in content]
file.close()

print(asci)
data = 1234
#data = int(asci)
'''for c in asci:
    if c in range(0,99):
        c= 0+'c'
print(asci)
'''
# convert to 3 dig format
# if dig in first position is 0 or ~ is the first char of document append ascii equivalent of ~
# number of nodes active are detected
n = random.randint(1, 10)
R1= random.randint(1, 1000)
R2= random.randint(1, 1000)
nodes = {}

print (n)
if(n <4 ):
    print ("The system is currently incapable of securing your data. Please try again later.")
else:
    for i in range (0, n):
        H= data + (R1*i) + (R2*i*i)
        nodes[i] = H
print (nodes)
'''
suppose 10 is the max no. of nodes in the system
'''


# rand function for random prime numbers
# create poolynomial as
# data + rand1X+ rand2X^2

