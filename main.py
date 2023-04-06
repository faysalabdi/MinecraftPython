import mcpi.block as Block
# import blocks
from mcpi.minecraft import Minecraft
from time import sleep
# from village import Village
import mcutil
import random
from house import house
from pillar import Plots, Pillar
from pathClass import Path

from timeit import default_timer as timer
import os
import house as House

mc = Minecraft.create()

import furniture as Furniture
from mcpi.vec3 import Vec3

chairPosition = Vec3(0,0,0)
# OR
chairPosition = mc.player.getPos()
chairLength = 10
chairRotation = Furniture.Orientation.EAST

# make the chair object
chair = Furniture.Chair(chairPosition, chairLength, chairRotation)
# builds the chair in the world
chair.build()


pids = mc.getPlayerEntityIds()
# blocks = mc.getBlocks(0,24,0,0,48,0)

# for x in blocks:
#     print(x)
# last_coords = (0, 0)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def getHighest(col):
    pass


def tprint(a):
    mc.postToChat(a)
    print(a)


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

    arr = [[[-1] * (sz) for _ in range(sy)] for _ in range(sx)]
    barr = blocks.split(",")

    bi = 0
    for j in range(sy):
        for i in range(sx):
            for k in range(sz):
                if (bi > len(barr)):
                    break
                curBlock = barr[bi]
                arr[i][j][k] = int(curBlock)
                bi += 1

    return arr


def getHeights(x, z, x2, z2):
    xdiff = int(mcutil.diff(x, x2))
    zdiff = int(mcutil.diff(z, z2))

    arr = [[-1] * (zdiff + 1) for _ in range(xdiff + 1)]
    blocks = mcutil.getBlocks(
        x, 0, z,
        x2, 255, z2
    )

    for x in range(xdiff + 1):
        for z in range(zdiff + 1):
            for y in range(254, -1, -1):
                if (blocks[x][y][z] == Block.AIR.id):
                    continue
                elif (y == 0):
                    arr[x][z] == -1
                    # print(f"max height at {baseX+x:.0f},{baseZ+z:.0f} is: {-1}")
                else:
                    arr[x][z] = y
                    # print(f"max height at {baseX+x:.0f},{baseZ+z:.0f} is: {y}")
                    break

    return arr


def compareTimes(xsize, zsize):
    tprint(f"getBlocks/python time for area of {xsize*zsize}")

    baseX, baseY, baseZ = mc.player.getPos()

    xsize = max(0, xsize)
    zsize = max(0, zsize)
    # center the coords
    baseX = baseX - (xsize / 2)
    baseZ = baseZ - (zsize / 2)

    tprint(f"base coords: {baseX:0.2f}, {baseY:0.2f}, {baseZ:0.2f}")

    start1 = timer()
    arr = getHeights(baseX, baseZ, baseX + xsize - 1, baseZ + zsize - 1)
    # start2 = timer()
    # blocks = mcutil.getBlocks(
    #     baseX, 0, baseZ,
    #     baseX + (xsize if xsize > 1 else 0),
    #     255,
    #     baseZ + (zsize if zsize > 1 else 0)
    # )

    # for x in range(xsize):
    #     for z in range(zsize):
    #         for y in range(254, -1, -1):
    #             curBlock = blocks[x][y][z]
    #             if (curBlock == Block.AIR.id):
    #                 continue
    #             elif (y == 0):
    #                 arr[x][z] == -1
    #                 # print(f"max height at {baseX+x:.0f},{baseZ+z:.0f} is: {-1}")
    #             else:
    #                 arr[x][z] = y
    #                 # print(f"max height at {baseX+x:.0f},{baseZ+z:.0f} is: {y}")
    #                 break

    end = timer()

    tprint(
        f"    Took {(end-start1 )* 1000:.5f}ms for area of {xsize*zsize} blocks (before array init)")
    # tprint(f"    Took {(end-start2) * 1000:.5f}ms for area of {xsize*zsize} blocks (after array init)")

    # tprint(f"getHeight/plugin time for area of {xsize*zsize}")

    # start1 = timer()
    # arr2 = [[-1] * zsize for _ in range(xsize)]
    # # start2 = timer()

    # for x in range(xsize):
    #     for z in range(zsize):
    #         arr2[x][z] = mc.getHeight(x + baseX, z + baseZ)

    # end = timer()

    # tprint(f"    Took {(end-start1) * 1000:.5f}ms for area of {xsize*zsize} blocks (before array init)")
    # tprint(f"    Took {(end-start2) * 1000:.5f}ms for area of {xsize*zsize} blocks (after array init)")

    PLACE_BLOCKS = True
    if (PLACE_BLOCKS):
        FIRST_BLOCK = Block.STONE_BRICK
        SECOND_BLOCK = Block.STONE_BRICK
        BLOCK_TO_PLACE = FIRST_BLOCK
        iter = 0
        for i, e in enumerate(arr):
            for j, y in enumerate(e):
                iter += 1
                # swap halfway to the other array, see if they're aligned
                if (iter > (len(arr) * len(e)) / 2
                        and BLOCK_TO_PLACE == FIRST_BLOCK):
                    # arr = arr2
                    BLOCK_TO_PLACE = SECOND_BLOCK

                # print(f"Placing block at {baseX+i:.0f}, {y}, {baseZ+j:.0f}")
                mc.setBlock(baseX + i, y+1, baseZ + j, BLOCK_TO_PLACE.id)
                pass


def handleChat():
    c = mc.events.pollChatPosts()
    ppos = mc.player.getPos()
    for x in c:
        if (x.message.startswith("!compareTimes")):
            t = x.message.split(" ")
            if (len(t) == 3):
                compareTimes(int(t[1]), int(t[2]))
        elif (x.message == "!stop"):
            mc.postToChat("/stop")
        elif (x.message.startswith("!tp")):
            # mc.postToChat()
            pos = x.message.split(" ")
            print(pos)
            mc.player.setPos(pos[1], pos[2], pos[3])
        elif (x.message == "!b"):
            block = mc.getBlockWithData(ppos.x, ppos.y - 1, ppos.z)
            print(f"below: {block}")
            mc.postToChat(f"below: {block}")
        elif (x.message.startswith("!house")):
            House.house(
                Vec3(ppos.x, ppos.y, ppos.z) + Vec3(2, 0, 0),
                14, 14, 6)
        elif (x.message.startswith("!p")):
            p = Plots()
            p.build()
        elif (x.message.startswith("!r")):
            r = Path()
            p.build()
        elif (x.message.startswith("!h")):
            house(ppos, random.randint(8,20), random.randint(8,20), random.randint(4,9))
        elif (x.message.startswith("!f")):
            tokens = x.message.split(' ')
            if (not tokens[1]):
                return
            # if (tokens[])
            f = tokens[1].capitalize()
            try:
                if (getattr(Furniture, f)):
                    def_length = random.randint(2,5)
                    def_size = 1, 1
                    def_height = 4
                    def_rotation = random.randint(0, 3)
                    print(tokens)
                    if (len(tokens) > 2):
                        for x in tokens[2:]:
                            if (x.startswith("l")):
                                def_length = int(x.split('=')[1].strip())
                                continue
                            elif (x.startswith("h")):
                                def_height = int(x.split('=')[1].strip())
                                continue
                            elif (x.startswith("s")):
                                stoken = x.split('=')[1]
                                def_size = int(stoken.split(',')[0]), int(stoken.split(',')[1]) 
                                continue
                            elif (x.startswith("r")):
                                def_rotation = int(x.split('=')[1].strip())
                                continue
                        # if (x.startswith("rot")):
                        #     def_rotation = int(x.split('-')[1])
                        #     continue
                    piece = getattr(Furniture, f)(origin=ppos, rotation=def_rotation, size=def_size, length=def_length, height=def_height)
                    piece.build()
            except Exception as e: 
                print(e)

        elif (x.message.startswith("!test")):
            test()

# def createLamp():
#     pass


def test():
    pos = mc.player.getPos()

    for x in range(15):
        mc.setBlock(pos.x + 2, pos.y, pos.z + x, Block.WOOL.withData(x))


p = mc.player.getPos()
# print(mcutil.getHeights(p.x, p.z, p.x + 2, p.z + 2))
# heights = mcutil.getHeights(p.x, p.z, p.x + 2, p.z + 2)

while True:
    handleChat()

    sleep(0.1)
