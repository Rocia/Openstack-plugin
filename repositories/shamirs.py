import math

file = open ('a.txt', "r")
data = file.read()
asci = [ord(c) for c in data]
file.close()
print(asci)