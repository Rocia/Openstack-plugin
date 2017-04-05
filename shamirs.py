import math
import random
import itertools

'''
def isprime(n):
    for m in range(2, int(n**0.5)+1):
        if not n%m:
            return False
    return True
'''

file = open ('a.txt', "r")
content = file.read()
asci = [ord(c) for c in content]
file.close()

#for asci[0] in range (000,099)
if 0 <= asci[0] <= 99 or asci[0] == 126:
    asci.insert(0, 126)
print(asci)

#managing 2 digit numbers
for n,i in enumerate(asci):
    if 0 <= i <= 9:
        asci[n] = '00' + str(i)
    elif 10 <= i <= 99:
        asci[n] = '0' + str(i)

print(asci)

data = ''.join(map(str, asci))

print(data)

#data = 1234
#data = int(asci)
# convert to 3 dig format
# if dig in first position is 0 or ~ is the first char of document append ascii equivalent of ~
# number of nodes active are detected
n = random.randint(1, 10)

# rand function for random prime numbers
x = len(data)
l = '1'+('0'*(x-1))
length = int(l)
print(length)

R1= random.randint(length/2,length)
R2= random.randint(0,length/2)
nodes = {}

# create polynomial as data + rand1X+ rand2X^2
print (n)
if n <4 :
    print ("The system is currently incapable of securing your data. Please try again later.")
else:
    for i in range (0, n):
        x = random.randint(-length/2,-1)
        H= int(data) + (R1*x) + (R2*x*x)
        nodes[x] = H
print (nodes)
