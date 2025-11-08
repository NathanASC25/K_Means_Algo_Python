#!/usr/bin/python3
import random
directFile = open("coordinates.csv", "w")
for i in range(38000):
    ''' For x and y respectively, Gen1 creates a random integer
        and Gen2 is a float multiplier
    '''
    xGen1 = random.randint(-80,50)
    xGen2 = random.random()
    yGen1 = random.randint(-80,50)
    yGen2 = random.random()
    x = xGen1 * xGen2
    y = yGen1 * yGen2
    directFile.write(f"({str(x)},{str(y)})\n")
