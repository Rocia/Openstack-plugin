import math
import random

file = open ('a.txt', "r")
content = file.read()
asci = [ord(c) for c in content]
file.close()

#for asci[0] in range (000,099)
if 0 <= asci[0] <= 99 or asci[0] == 126:
    asci.insert(0, 126)
print(asci)

data = ''.join(map(str, asci))
'''
for i in range(0,len(asci)):
    data[i] += asci[i]
for asci[i] in range(0,len):
    data=str[i] + str[i+1]
print(data)

data = 0
for i in asci:
    ''.join(data)'''
print(data)

#data = 1234

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
        x = random.randint(1, 1000)
        H= int(data) + (R1*x) + (R2*x*x)
        nodes[x] = H
print (nodes)
'''
suppose 10 is the max no. of nodes in the system
'''


# rand function for random prime numbers
# create poolynomial as
# data + rand1X+ rand2X^2

