from mcpi.block import *
from mcpi.minecraft import Minecraft
import math
# global mc 
mc = Minecraft.create()

def getHighestPoint(x, z, x2=None, z2 = None):
    """
    get the highest block on this x,z coordinate
    """
    if (x2 and z2):
        return getListMax(getHighestPointArray(x, z, x2, z2))

    print(f"checking highest at: {x}, {z}")
    print(f"block at sea level: {mc.getBlock(x, 64, z)}")
    blocks = mc.getBlocks(x, 0, z, x, 256, z)
    for y in range(128, 0, -1):
        b = mc.getBlock(x, y, z)
        
        if y % 1 == 0:
            print(f" got {x}, {y}, {z} = {b}")
        if (b != AIR.id):
            return y
    
    return 0

def getListMax(list):
    max = None
    for l in list:
        if (type(l) == list):
            n = getListMax(max)
        else: 
            n = l

        max = n if n > max else max
    # for x in range(256, 0, -1):

def getHighestPointArray(x, z, x2, z2):
    if (x > x2):
        temp = x
        x2 = x
        x = temp
    if (z > z2):
        temp = z
        z2 = z
        z = z2
    # x2/z2 if base is 0
    bx = x2 - x
    bz = z2 - z
    # print(f"x: {x}, {x2}")
    # print(f"z: {z}, {z2}")
    # print(f"bx: {bx}, bz: {bz}")
    arr = [[-1] * bz for e in range(bx)] 
    # print(len(arr))   
    # print(len(arr[0]))   
    for i in range(len(arr)):
        for j in range(arr[i]):
            arr[i][j] = getHighestPoint(i + x, j + z)

    return arr

def getBlocks(*args):
    if (len(args) != 6):
        raise ValueError
    a = []
    for e in args:
        a.append(float(e))


    blocks = mc.getBlocks(a[0], a[1], a[2], a[3], a[4], a[5])
    minX = min(a[0], a[3])
    maxX = max(a[0], a[3])
    minY = min(a[1], a[4])
    maxY = max(a[1], a[4])
    minZ = min(a[2], a[5])
    maxZ = max(a[2], a[5])

    sx = int(max(diff(maxX, minX) + 1, 1))
    sy = int(max(diff(maxY, minY) + 1, 1))
    sz = int(max(diff(maxZ, minZ) + 1, 1))
    
    arr = [ [ [-1] * (sz) for _ in range(sy) ] for _ in range(sx)]
    barr = blocks.split(",")
    
    bi = 0
    for j in range(sy):
        for i in range(sx):
            for k in range(sz):
                if (bi > len(barr)): break
                curBlock = barr[bi]
                arr[i][j][k] = int(curBlock)
                bi += 1
            

    return arr


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

def getHeights(x, z, x2, z2):
    xdiff = int(diff(x, x2))
    zdiff = int(diff(z, z2))

    arr = [[-1] * (zdiff + 1) for _ in range(xdiff + 1)]
    blocks = getBlocks(
        x, 0, z, 
        x2, 255, z2
    )
    

    for x in range(xdiff + 1):
        for z in range(zdiff + 1):
            for y in range(254, -1, -1):
                if (blocks[x][y][z] == AIR.id):
                    continue
                elif (y == 0):
                    arr[x][z] == -1
                    # print(f"max height at {baseX+x:.0f},{baseZ+z:.0f} is: {-1}")
                else:
                    arr[x][z] = y
                    # print(f"max height at {baseX+x:.0f},{baseZ+z:.0f} is: {y}")
                    break

    return arr
    
