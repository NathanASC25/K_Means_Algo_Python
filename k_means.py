#!/usr/bin/python3
import math, random
def euclidean_distance(coord1, coord2):
    x1 = float(coord1[0])
    y1 = float(coord1[1])
    x2 = float(coord2[0])
    y2 = float(coord2[1])
    result = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return result
def closest_stationary_point(singleCoord, points):
    shortestDistance = euclidean_distance(singleCoord, points[0])
    # Index of closest cluster
    closestCluster = 0
    for i in range(1, len(points)):
        newDistance = euclidean_distance(singleCoord, points[i])
        if newDistance < shortestDistance:
            shortestDistance = newDistance
            closestCluster = i
    squares.append(math.pow(shortestDistance, 2))
    x = float(singleCoord[0])
    y = float(singleCoord[1])
    xSums[closestCluster] += x
    ySums[closestCluster] += y
    pointCount[closestCluster] += 1
    closestClusters.append(closestCluster)
directFile = open("coordinates.csv","r")
resultsFile = open("model_results.csv","w")
endLoop = False
# Capture the distances squared of each point to the closest cluster
squares = []
liz = []
xCoords = []
yCoords = []
# Random centroids/later clusters
pointArray = []
numIterations = 1
numRepits = 0
# Compares the last array with the current array of closest clusters
tempArray = []
# Add the x and y of each point closest to each cluster
xSums = []
ySums = []
# Count the number of points that are closest to each cluster
pointCount = []
# Each point will have their closest cluster calculated by index
closestClusters = []
for i in directFile:
    liz.append(i.split(','))
for i in range(len(liz)):
    xCoords.append(liz[i][0][1:len(liz[i][0])])
    yCoords.append(liz[i][1][0:len(liz[i][1]) - 2])
print()
chosenPoints = []
numClusters = int(input("Enter the number of clusters: "))
print("Number of Clusters:", numClusters)
resultsFile.write(f"Number of Clusters: {int(numClusters)}")
while numClusters > 0:
    rand_num = random.randint(0, len(liz))
    if rand_num in chosenPoints:
        notSame = False
        while notSame != True:
            numRepits += 1
            rand_num = random.randint(0, len(liz))
            if (rand_num not in chosenPoints):
                notSame = True
    r = rand_num
    # Truncate string parentheses
    pointArray.append([liz[r][0][1:len(liz[r][0])], liz[r][1][0:len(liz[r][1]) - 2]])
    chosenPoints.append(r)
    numClusters -= 1
print("Number of Repetitions Chosen:", numRepits)
del numClusters, chosenPoints
for i in range(len(pointArray)):
    xSums.append(0)
    ySums.append(0)
    pointCount.append(0)
print("\nPoints:\n")
resultsFile.write(f"\nPoints:\n")
for i in pointArray:
    print(i,"\n")
    resultsFile.write(f"{list(i)}\n")
# Testing subject
#for i in range(len(liz)):
#    closest_stationary_point([xCoords[i], yCoords[i]], pointArray)
#print(len(closestClusters),"\n")
#print(len(pointCount),len(pointArray),"\n")
#print(len(xSums), len(ySums),"\n")
#print("xSums: ",xSums,"\n","ySums: ",ySums,"\n")
while endLoop == False:
    squares = []
    changes = 0
    for i in range(len(liz)):
        closest_stationary_point([xCoords[i], yCoords[i]], pointArray)
        if (numIterations >= 2 and tempArray[i] != closestClusters[i]):
            changes += 1
    num = sum(squares)
    print("\n\nSum of Squares:",num)
    print("\nPoints:\n")
    resultsFile.write(f"\n\nSum of Squares: {float(num)}")
    resultsFile.write(f"\nPoints:\n")
    for i in range(len(pointArray)):
        xAvg = xSums[i] / pointCount[i]
        yAvg = ySums[i] / pointCount[i]
        pointArray[i] = [xAvg, yAvg]
        print(pointArray[i], "\n")
        resultsFile.write(f"{list(pointArray[i])}\n")
    print("Number of clusters changed:",changes)
    print("\nThis is iteration:", numIterations)
    resultsFile.write(f"Number of clusters changed: {int(changes)}")
    resultsFile.write(f"\nThis is iteration: {int(numIterations)}")
    if numIterations >= 2 and changes == 0:
        endLoop = True
    numIterations += 1
    tempArray = closestClusters
    closestClusters = []
print("\nDone!\n")
resultsFile.write(f"\nDone!\n")
