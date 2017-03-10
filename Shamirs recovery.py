import random

available = {0: 1234, 1: 2772, 2: 5910, 3: 10648, 4: 16986, 5: 24924, 6: 34462, 7: 45600, 8: 58338, 9: 72676}
n = random.randint(0, 9)
if(n <4 ):
    print ("The system is currently incapable of recovering your data. Please try again later.")
else:
    for i in range(0,3):
        available = random.randint(0, 9)


