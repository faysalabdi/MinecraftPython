# from tkinter import Y
from re import S
import mcpi.minecraft as minecraft
import random
import mcpi.block as block
# import math
import numpy as np
from mcpi.vec3 import Vec3


mc = minecraft.Minecraft.create()

# pos = mc.player.getTilePos()

# l_h = mc.getHeight(pos.x, pos.z)


# y = pos.y + random.randint(5, 20)

class Pillar:
    def __init__(self, x, z, height, width, length):
        self.x = x
        self.z = z
        self.height = height
        self.width = width
        self.length = length

    def getPos(self):
        return Vec3(self.x, self.height - 1, self.z)

    def getEdges(self):
        return [
            self.x,
            self.z,
            self.x + self.width - 1,
            self.z + self.length - 1
        ]

    def getPosSize(self):
        return [
            self.x, 
            self.z,
            self.width,
            self.length]

    def plot(self):
        PLOT_BLOCK = block.STONE_BRICK
        mc.setBlocks(self.x, 0, self.z, self.x + self.width - 1,
                     self.height - 1, self.z + self.length - 1, PLOT_BLOCK)
        # mc.setBlocks(self.x, self.height , self.z, self.x + self.width - 1, 200, self.z + self.length - 1, block.AIR)

    def intersects(self, plot):
        p1e = self.getEdges()
        p2e = plot.getEdges()
        x1Intersect = p1e[0] >= p2e[0] and p1e[0] <= p2e[2]
        x2Intersect = p1e[2] >= p2e[0] and p1e[2] <= p2e[2]
        z1Intersect = p1e[1] >= p2e[1] and p1e[1] <= p2e[3]
        z2Intersect = p1e[3] >= p2e[1] and p1e[3] <= p2e[3]
        if ((x1Intersect or x2Intersect) and (z1Intersect or z2Intersect)):
            return True

        return False


def getLandHeight(x, z):
    return (x * x / 100 + 50 + 5 * np.sin(x / 10) * np.cos(z / 10))
# (x * x / 100 + 50 + 5 * np.sin(x / 10) * np.cos(z / 10)) * np.sin(x/ 5)


# x1 = -50
# z1 = -50
# x2 = 50
# z2= 50
# for x in range (x1, x2):
#     for z in range(z1, z2):
#         mc.setBlocks(x , -100, z, x, getLandHeight(x, z), z + 20 , block.GRASS)
#         mc.setBlocks(x , getLandHeight(x, z) +1, z, x, 100, z, block.AIR)


pillars = []


def generateRandomPillar():
    ppos = mc.player.getPos()
    x = random.randint(10, 10) + ppos.x
    z = random.randint(10, 20) + ppos.z
    y = random.randint(70, 80)
    w = random.randint(10, 25)
    l = random.randint(8, 20)

    p = Pillar(x, z, y, w, l)

    for x in pillars:
        if (p.intersects(x)):
            print(
                f"Pillar intersects ({p.x:.2f} {p.z:.2f}, {x.x:.2f}, {x.z:.2f}")
            mc.postToChat(
                f"Pillar intersects ({p.x:.2f} {p.z:.2f}, {x.x:.2f}, {x.z:.2f}")
            return
    p.plot()
    pillars.append(p)

    # getEnds()


# generateRandomPillar()
# generateRandomPillar()
# generateRandomPillar()
# generateRandomPillar()
# generateRandomPillar()
def tprint(a):
    print(a)
    mc.postToChat(a)


ppos = mc.player.getPos()
# p = Pillar(ppos.x, ppos.z, 64, 5, 5)
# p.plot()
# p2 = Pillar(ppos.x, ppos.z + 5, 64, 5, 5)
# p2.plot()
# tprint(f"p1 intersecting p2? {p.intersects(p2)}")


class Plots:

    def __init__(self) -> None:
        self.MAX_PLOT_SIZE = 20
        self.MIN_PLOT_SIZE = 9
        self.CENTER = (random.randint(-500, 500), random.randint(-500, 500))
        self.PLOTS_PER_SIDE = 4
        self.plots = []
        self.MIN_CENTER_SPACING = 8
        self.MAX_CENTER_SPACING = 10
        self.GAP_BETWEEN_PLOTS_MIN = 8
        self.GAP_BETWEEN_PLOTS_MAX = 10
        self.height = mc.getHeight(self.CENTER[0], self.CENTER[1])
        pass

    def setCenter(self, x, y):
        self.CENTER = (x, y)

    def getAllPlots(self):
        if (not len(self.plots)):
            return None

        return self.plots

    # clear the space for the plots
    def prepareSpace(self):
        x1 = self.CENTER[0] + (((self.GAP_BETWEEN_PLOTS_MAX +
                                       self.MAX_PLOT_SIZE) * (-self.PLOTS_PER_SIDE / 2)))
        x2 = x1 + ((self.GAP_BETWEEN_PLOTS_MAX + self.MAX_PLOT_SIZE) * (self.PLOTS_PER_SIDE))
        
        z1 = self.CENTER[1] - self.MAX_CENTER_SPACING - self.MAX_PLOT_SIZE
        z2 = z1 + (self.MAX_CENTER_SPACING * 2) + (self.MAX_PLOT_SIZE * 2)

        # mc.

        # remove blocks above
        mc.setBlocks(x1, self.height, z1, x2, 255, z2, block.AIR)
        
        FILLER_BLOCK = block.GRASS
        # fill ground
        mc.setBlocks(x1, self.height, z1, x2, self.height, z2, FILLER_BLOCK)

        # fill underneath
        mc.setBlocks(x1, 5, z1, x2, self.height - 1, z2, block.STONE)

        pass

    def build(self):
        self.prepareSpace()
        
        # mark the center
        # mc.setBlocks(
        #     self.CENTER[0], 64, self.CENTER[1],
        #     self.CENTER[0], 128, self.CENTER[1],
        #     block.WOOD)
        
        # mc.player
        # loop twice for each side
        for i in range(-1, 2, 2):
            last_x = None

            # for loop for each side
            for j in range(-self.PLOTS_PER_SIDE, self.PLOTS_PER_SIDE, 2):
                vert_gap = random.randint(
                    self.MIN_CENTER_SPACING, self.MAX_CENTER_SPACING)
                width = random.randint(self.MIN_PLOT_SIZE, self.MAX_PLOT_SIZE)
                length = random.randint(self.MIN_PLOT_SIZE, self.MAX_PLOT_SIZE)
                # width = width * i
                pz = self.CENTER[1] + ((vert_gap*i))
                pz = pz if i == 1 else pz - length

                if (last_x == None):
                    px = self.CENTER[0] + (((self.GAP_BETWEEN_PLOTS_MIN +
                                       self.MAX_PLOT_SIZE) * (j / 2)))
                else:
                    px = last_x + random.randint(self.GAP_BETWEEN_PLOTS_MIN, self.GAP_BETWEEN_PLOTS_MAX)
                

                pheight = self.height + random.randint(1,3)
                last_x = px + width
                # make the plot, and add it to our list of plots
                p = Pillar(px, pz, pheight, width, length)
                p.plot()
                # append plot and whether its on north or south side
                self.plots.append([p, i == -1])





p = Plots()
p.setCenter(ppos.x + 200, ppos.z)
# uncomment to build the plots (and teleport to it)

# mc.player.setPos(ppos.x + 200, 128, ppos.z)
# p.build()





# mc.player.setPos(0,getLandHeight(0, 0) + 1, 0)

# def car_park():

#     mc.setBlocks(x +1 , getHeight(x, z), z, x + 130, getHeight(x, z) + 100, z + 149, block.AIR)
#     mc.setBlocks(x + 1 , getHeight(x, z), z, x + 149, getHeight(x, z), z + 148, block.GRASS)
#     mc.player.setPos(x +1,100, z+ 1)
# car_park()


# def pillar(x, y, z):

#     height = y + 5 + random.randint(0, 3)
#     #Pillar
#     mc.setBlocks(x, y + 1, z, x + 2, height, z+ 2, block.STONE_BRICK)

#     size = random.randint(10, 15)
#     #BRANCH
#     for i in range(size):
#         mc.setBlock(x + i + 1, height, z + 1, block.STONE_BRICK)
#         mc.setBlock(x - i + 1, height, z + 1, block.STONE_BRICK)
#         mc.setBlock(x + 1, height, z + i + 1 , block.STONE_BRICK)
#         mc.setBlock(x + 1, height, z - i +1  , block.STONE_BRICK)

#         height = height + 1

#     minimum = size+ 1
#     #RECTANGLE

#     mc.setBlocks(x  -minimum + 1, height, z - minimum, x + minimum + 1  , height, z + minimum, block.STONE_BRICK)


#     mc.setBlocks(x + 6, y, z -10, x + 25, y -5, z + 20, block.BEDROCK)
#     mc.setBlocks(x + 7, y, z -9, x + 24, y -4, z + 19, block.AIR)
#     mc.setBlocks(x + 7, y, z -9, x + 24, y -4, z + 19, block.WATER_FLOWING)

#     # # POOL Fences
#     # mc.setBlocks(x + 5, y+ 1, z -11, x +5, y+3, z + 21, block.FENCE)
#     # mc.setBlocks(x + 26, y+ 1, z -11, x +26, y+3, z + 21, block.FENCE)
#     # mc.setBlocks(x+ 5, y+ 1, z - 11 , x + 25, y+3, z - 11, block.FENCE)
#     # mc.setBlocks(x+ 5, y+ 1, z +21 , x + 25, y+3, z +21, block.FENCE)


# a =  pos.x + 20
# b= pos.z + random.randint(25 , 30)


# for i in range (3):

#     gap = random.randint(20, 25) * 2

#     y= mc.getHeight(a, b)


#     pillar(a, y, b)
#     pillar(a, y, b + random.randint(62, 67))

#     a = a + gap

# x = pos.x + 5
# z = pos.z + 3


# def fence():
#     #SIDE 1
#     mc.setBlocks(x, y+ 1, z -1, x , y + 5, z + 56, block.FENCE_DARK_OAK)
#     mc.setBlocks(x, y+ 1, z + 66, x , y + 5, z + 139, block.FENCE_DARK_OAK)

#     #SIDE 2
#     d = pos.x + 145
#     mc.setBlocks(d, y+ 1, z -2, d , y + 5, z + 56, block.FENCE_DARK_OAK)
#     mc.setBlocks(d, y+ 1, z + 66, d , y + 5, z + 139, block.FENCE_DARK_OAK)

#     #SIDE 3
#     mc.setBlocks(x, y+ 1, z -2, x + 140, y + 5, z -2, block.FENCE_DARK_OAK)

#     #SIDE 4
#     e  = pos.z + 144
#     mc.setBlocks(x, y+ 1, e -2, x + 140, y + 5, e -2, block.FENCE_DARK_OAK)

# fence()


# def tree(x, y, z):
#     mc.setBlocks(x,y+1,z, x, y + 10, z, block.WOOD)
#     mc.setBlocks(x -3, y+11, z -3, x +3, y + 11, z +3, block.LEAVES)
#     mc.setBlocks(x -2, y+12, z -2, x +2, y + 12, z +2, block.LEAVES)
#     mc.setBlocks(x -1, y+13, z -1, x +1, y + 13, z +1, block.LEAVES)


# x = pos.x + 10
# z = pos.z + 3

# for i in range(16):

#     tree(x, y, z)
#     tree(x, y, z +51)
#     tree(x, y, z +71)
#     tree(x, y, z +137)

#     x = x + 8

# g = pos.x + 15
# s= pos.z + 119

# def garden(g, s):
#     mc.setBlocks(g, y, s+1, g + 55, y+2 , s + 18, block.FARMLAND)
#     mc.setBlocks(g, y + 1, s+1, g + 55, y+ 2 , s + 18, block.FLOWER_YELLOW)
#     mc.setBlocks(g + 60, y, s+1, g + 115, y+2 , s + 18, block.FARMLAND)
#     mc.setBlocks(g+ 60, y + 1, s+1, g + 115, y+ 2 , s + 18, block.FLOWER_CYAN)
# garden(g, s)
