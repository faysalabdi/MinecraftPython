# Server commands to suspend time:
# gamerule doDaylightCycle false
# # time set day

from mcpi.minecraft import Minecraft
import random
from mcpi import block
from math  import sqrt
mc = Minecraft.create()
import time
# Get player's exact coordinates

x, y , z = mc.player.getTilePos()



def vec_distance(vector1, vector2):
    distance = 0.0
    for cntr in range(len(vector1)):
        distance += (vector1[cntr] - vector2[cntr]) ** 2
    return sqrt(distance)



doorsxyz = [(90, 72, 9), (104, 72, 5), (90, 72, -7), (104, 76, -11), (89,72, -15), (86, 70, -31), (101, 72,-32)]

doors = []
for door in doorsxyz:
    doors.append((door[0], door[-1]))
doorssorted = []
for i in range(len(doors)):
    for j  in range(i + 1, len(doors) - 1):
        dist = vec_distance(doors[i], doors[j])
        doorssorted.append(((doors[i], doors[j]), dist))

doorssorted = sorted(doorssorted, key=lambda x: (x[-1] ))
firstDoor = doorssorted[-1][0][0]
lastDoor = doorssorted[-1][0][1]

nearestFirstDoor = []
for i in range(len(doors)):
    if vec_distance(firstDoor, doors[i]) > 0:
        nearestFirstDoor.append((doors[i],vec_distance(firstDoor, doors[i])))

nearestFirstDoor = sorted(nearestFirstDoor, key=lambda x: (x[1]))

nearestLastDoor = []
for i in range(len(doors)):
    if vec_distance(lastDoor, doors[i]) > 0:
        nearestLastDoor.append((doors[i],vec_distance(lastDoor, doors[i])))

nearestLastDoor = sorted(nearestLastDoor, key=lambda x: (x[1] ))
nearestLastDoor = nearestLastDoor[0][0]
nearestFirstDoor = nearestFirstDoor[0][0]


startOfPath = (int((firstDoor[0] + nearestFirstDoor[0] )/ 2), int((firstDoor[1] + nearestFirstDoor[1] )/ 2))
endOfPath = (int((lastDoor[0] + nearestLastDoor[0] )/ 2), int((lastDoor[1] + nearestLastDoor[1] )/ 2))

extraDist = max(abs(startOfPath[0] - endOfPath[0]), abs(startOfPath[1] - endOfPath[1]))
extraDist=  int(extraDist * 0.05) + 1

startOfPaths = [((startOfPath[0] - extraDist, startOfPath[1]), vec_distance((startOfPath[0] - extraDist, startOfPath[1]), endOfPath)),
                ((startOfPath[0], startOfPath[1] + extraDist), vec_distance((startOfPath[0], startOfPath[1] + extraDist), endOfPath)),
                ((startOfPath[0] + extraDist, startOfPath[1]), vec_distance((startOfPath[0] + extraDist, startOfPath[1]), endOfPath)),
                ((startOfPath[0], startOfPath[1] - extraDist), vec_distance((startOfPath[0], startOfPath[1] - extraDist), endOfPath))
                ]
startOfPaths = sorted(startOfPaths, key=lambda x: (x[1]))
startOfPath = startOfPaths[-1][0]

endOfPaths = [((endOfPath[0] - extraDist, endOfPath[1]), vec_distance((endOfPath[0] - extraDist, endOfPath[1]), startOfPath)),
                ((endOfPath[0], endOfPath[1] + extraDist), vec_distance((endOfPath[0], endOfPath[1] + extraDist), startOfPath)),
                ((endOfPath[0] + extraDist, endOfPath[1]), vec_distance((endOfPath[0] + extraDist, endOfPath[1]), startOfPath)),
                ((endOfPath[0], endOfPath[1] - extraDist), vec_distance((endOfPath[0], endOfPath[1] - extraDist), startOfPath))
                ]

endOfPaths = sorted(endOfPaths, key=lambda x: (x[1]))
endOfPath = endOfPaths[-1][0]
yavg = 0
for (x, y ,z) in doorsxyz:
    yavg += y
yavg = int(yavg / len(doorsxyz))
mc.setBlocks(startOfPath[0]  , yavg - 1,  startOfPath[1] , endOfPath[0] , yavg - 1, endOfPath[1], block.STONE_BRICK)

"""
def avg(l):
    return sum(l) / len(l)

def diff(base, x):
    if (base > x):
        temp = base
        base = x
        x = temp
    
    if (x > 0 and base < 0):
        return abs(base) + x
    elif (x < 0):
        return abs(base) + x
    else:
        return x - base
"""
"""
class Path:

    def __init__(self, x1, x2, z1, z2) -> None:
        self.pos = (x1, x2, z1, z2)
        self.dimensions = (diff(x1, x2), diff(z1, z2))
        self.axis = 'x' if self.dimensions[0] > self.dimensions[1] else 'z'
        self.buildMainPath()


    def buildMainPath(self):

        # end1y = avg([for x in range(self.dimensions)])
"""



istart = min(startOfPath[0], endOfPath[0])
iend = max(startOfPath[0], endOfPath[0])
jstart = min(startOfPath[1], endOfPath[1])
jend = max(startOfPath[1], endOfPath[1])
pathBlocks = []
for i in range(istart, iend + 1):
    for j in range(jstart, jend + 1):
        pathBlocks.append((i, yavg,j))

pathBlocksDist = []

i = 0
doors1 = doorsxyz.copy()

doorToPathBlock = []
tempPathBlocksDist = []
while doors1:

    door = doorsxyz[i]
   
    for pathBlock in pathBlocks:
        tempPathBlocksDist.append((door, pathBlock, vec_distance(door, pathBlock)))

    tempPathBlocksDist = sorted(tempPathBlocksDist , key=lambda x: (x[-1]))
    
    temp = (tempPathBlocksDist[0][0],(tempPathBlocksDist[0][1][0], int(tempPathBlocksDist[0][1][1] - 1), tempPathBlocksDist[0][1][2]), tempPathBlocksDist[0][2])
   # tempPathBlocksDist[0] = (tempPathBlocksDist[0][0], 
    print(temp)
    print(tempPathBlocksDist[0])
    #doorToPathBlock.append(tempPathBlocksDist[0])
    doorToPathBlock.append(temp)
    tempPathBlocksDist = []
    doors1.pop(0)
    i += 1

pathBlock = block.STONE

#p stands for  plus and m stand for minus

#y
def Xp1YZ(x, y, z):
    return mc.setBlock(x + 1, y, z , pathBlock)

def Xm1YZ(x, y, z):
    return mc.setBlock(x - 1, y, z , pathBlock)

def XYZp1(x, y, z):
    return mc.setBlock(x, y, z + 1 , pathBlock)

def XYZm1(x, y, z):
    return mc.setBlock(x, y, z - 1 , pathBlock)


#y - 1
def Xp1Ym1Z(x, y, z):
    return mc.setBlock(x + 1, y - 1, z, pathBlock)

def Xm1Ym1Z(x, y, z):
    return mc.setBlock(x - 1, y - 1, z, pathBlock)

def XYm1Zp1(x, y, z):
    return mc.setBlock(x, y - 1, z + 1, pathBlock)

def XYm1Zm1(x, y, z):
    return mc.setBlock(x, y - 1, z - 1, pathBlock)

#y - 2
def Xp1Ym2Z(x, y, z):
    return mc.setBlock(x + 1, y - 2, z, pathBlock)

def Xm1Ym2Z(x, y, z):
    return mc.setBlock(x - 1, y - 2, z, pathBlock)

def XYm2Zp1(x, y, z):
    return mc.setBlock(x, y - 2, z + 1, pathBlock)

def XYm2Zm1(x, y, z):
    return mc.setBlock(x, y - 2, z - 1, pathBlock)


for door, path, dist in doorToPathBlock:
    count = 0
    walk = door
    
    while vec_distance(walk, path) > 0:
        count += 1
        #time.sleep(1)
        if count == 100:
        
            break
        # y  -  1
        if vec_distance((walk[0], walk[1] - 1, walk[2]), path) < vec_distance(walk, path):

            # (x + 1, y - 1, z)
            if vec_distance((walk[0] + 1, walk[1] - 1, walk[2]), path) < vec_distance((walk[0], walk[1] - 1, walk[2]),
                                                                                      path):
                Xp1Ym1Z(walk[0], walk[1], walk[2])
                walk = (walk[0] + 1, walk[1] - 1, walk[2])

            # (x - 1, y - 1, z)
            elif vec_distance((walk[0] - 1, walk[1] - 1, walk[2]), path) < vec_distance((walk[0], walk[1] - 1, walk[2]),
                                                                                        path):
                Xm1Ym1Z(walk[0], walk[1], walk[2])
                walk = (walk[0] - 1, walk[1] - 1, walk[2])

            # (x , y - 1, z + 1)
            elif vec_distance((walk[0], walk[1] - 1, walk[2] + 1), path) < vec_distance((walk[0], walk[1] - 1, walk[2]),
                                                                                        path):
                XYm1Zp1(walk[0], walk[1], walk[2])
                walk = (walk[0], walk[1] - 1, walk[2] + 1)

            # (x , y + 1, z - 1)
            elif vec_distance((walk[0], walk[1] - 1, walk[2] - 1), path) < vec_distance((walk[0], walk[1] - 1, walk[2]),
                                                                                        path):
                XYm1Zm1(walk[0], walk[1], walk[2])
                walk = (walk[0], walk[1] - 1, walk[2] - 1)

        # y - 2
        elif vec_distance((walk[0], walk[1] - 2, walk[2]), path) < vec_distance(walk, path):

            # (x + 1, y - 2, z)
            if vec_distance((walk[0] + 1, walk[1] - 2, walk[2]), path) < vec_distance((walk[0], walk[1] - 2, walk[2]),
                                                                                      path):
                Xp1Ym2Z(walk[0], walk[1], walk[2])
                walk = (walk[0] + 1, walk[1] - 2, walk[2])

            # (x - 1, y - 2, z)
            elif vec_distance((walk[0] - 1, walk[1] - 2, walk[2]), path) < vec_distance((walk[0], walk[1] - 2, walk[2]),
                                                                                        path):
                Xm1Ym2Z(walk[0], walk[1], walk[2])
                walk = (walk[0] - 1, walk[1] - 2, walk[2])

            # (x , y - 2, z + 1)
            elif vec_distance((walk[0], walk[1] - 2, walk[2] + 1), path) < vec_distance((walk[0], walk[1] - 2, walk[2]),
                                                                                        path):
                XYm2Zp1(walk[0], walk[1], walk[2])
                walk = (walk[0], walk[1] - 2, walk[2] + 1)

            # (x , y - 1, z - 1)
            elif vec_distance((walk[0], walk[1] - 2, walk[2] - 1), path) < vec_distance((walk[0], walk[1] - 2, walk[2]),
                                                                                        path):
                XYm2Zm1(walk[0], walk[1], walk[2])
                walk = (walk[0], walk[1] - 2, walk[2] - 1)


        # y 
        else:
            # (x + 1, y , z)
            if vec_distance((walk[0] + 1, walk[1], walk[2]), path) < vec_distance(walk, path):

                Xp1YZ(walk[0], walk[1], walk[2])
                walk = (walk[0] + 1, walk[1], walk[2])

            # (x - 1, y , z)
            elif vec_distance((walk[0] - 1, walk[1], walk[2]), path) < vec_distance(walk, path):

                Xm1YZ(walk[0], walk[1], walk[2])
                walk = (walk[0] - 1, walk[1], walk[2])

            # (x , y , z + 1)
            elif vec_distance((walk[0], walk[1], walk[2] + 1), path) < vec_distance(walk, path):

                XYZp1(walk[0], walk[1], walk[2])
                walk = (walk[0], walk[1], walk[2] + 1)

            # (x , y , z - 1)
            elif vec_distance((walk[0], walk[1], walk[2] - 1), path) < vec_distance(walk, path):

                XYZm1(walk[0], walk[1], walk[2])
                walk = (walk[0], walk[1], walk[2] - 1)






            


