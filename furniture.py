# import
import math
import mcpi.block as Block
from mcpi.minecraft import Minecraft
from enum import Enum
import time

# from numpy import number


mc = Minecraft.create()


class Furniture:

    def __init__(self, origin) -> None:
        self.origin = origin
        pass

    def build():
        raise "Not yet been implemented!"


class Orientation(Enum):
    NORTH = 0
    WEST = 1
    SOUTH = 2
    EAST = 3



class Chair(Furniture):

    def __init__(self, origin, length=1, rotation=Orientation.EAST, **kwargs):
        self.origin = origin
        self.length = length
        if (type(rotation) == int):
            self.rotation = Orientation(min(max(rotation, 0), 3))
        else:
            self.rotation = rotation

    def build(self):
        rotationData = {
            1: 0,
            2: 3,
            3: 1,
            0: 2,
        }
        time.sleep(0.1)
        STAIR_BLOCK = Block.STAIRS_WOOD
        rotate = rotationData[self.rotation.value]
        mc.postToChat(f"length: {self.length}, rotation: {self.rotation}")
        if (not (self.rotation.value & 1)):
            START = [math.floor(self.origin.x - (self.length / 2)), self.origin.y, self.origin.z]
            END = [math.floor(self.origin.x - (self.length / 2) + self.length - 1), self.origin.y, self.origin.z]
            # for x in range(self.length):
            mc.setBlocks(START[0], START[1], START[2], END[0], END[1], END[2],
                            STAIR_BLOCK.withData(rotate))
            # time.sleep(1)
            # time.sleep(0.2)
            if (not mc.getBlock(START[0] - 1, START[1], START[2])):
                mc.setBlock(START[0] - 1, START[1], START[2], Block.SIGN_WALL.withData(4))
            if (not mc.getBlock(END[0] + 1, END[1], END[2])):
                mc.setBlock(END[0] + 1, END[1], END[2], Block.SIGN_WALL.withData(5))
        else:
            START = [math.floor(self.origin.x), self.origin.y, math.floor(self.origin.z - (self.length / 2))]
            END = [math.floor(self.origin.x), self.origin.y, math.floor(self.origin.z - (self.length / 2) + self.length - 1)]
            # for x in range(self.length):
            mc.setBlocks(START[0], START[1], START[2], END[0], END[1], END[2],
                            STAIR_BLOCK.withData(rotate))
            # time.sleep(0.2)
            if (not mc.getBlock(START[0], START[1], START[2] - 1)):
                mc.setBlock(START[0], START[1], START[2] - 1, Block.SIGN_WALL.withData(0))
            if (not mc.getBlock(END[0], END[1], END[2] + 1)):
                mc.setBlock(END[0], END[1], END[2] + 1, Block.SIGN_WALL.withData(3))


class Table(Furniture):

    def __init__(self, origin, size, **kwargs):
        self.origin = origin
        self.size = size
        # if (type(rotation) == int):
        #     self.rotation = Orientation(min(max(rotation, 0), 3))
        # else:
        #     self.rotation = rotation

    def build(self):

        O = self.origin
        S = self.size

        # white carpet
        TABLETOP_BLOCK = Block.Block(171)
        POST_BLOCK = Block.FENCE
        time.sleep(0.1)
        mc.setBlocks(
            math.floor(O.x) - ((S[0] - 1) / 2),              O.y, math.floor(O.z) - ((S[1] - 1) / 2),
            math.floor(O.x) - ((S[0] - 1) / 2) + (S[0] - 1), O.y, math.floor(O.z) - ((S[1] - 1) / 2) + (S[1] - 1),
            POST_BLOCK
            )
        
        # time.sleep(1)
        
        mc.setBlocks(
            math.floor(O.x) - ((S[0] - 1) / 2),              O.y+1, math.floor(O.z) - ((S[1] - 1) / 2),
            math.floor(O.x) - ((S[0] - 1) / 2) + (S[0] - 1), O.y+1, math.floor(O.z) - ((S[1] - 1) / 2) + (S[1] - 1),
            TABLETOP_BLOCK
        )

        # time.sleep(0.5)



class Well(Furniture):

    def __init__(self, origin, **kwargs):
        self.origin = origin

    def build(self):
                # the well
        BOTTOM_SLAB = Block.STONE_SLAB.withData(5)
        WELL_BLOCK = Block.STONE_BRICK
        POST_BLOCK = Block.FENCE
        FLUID_BLOCK = Block.WATER

        # fixed size well (2x2 inner, 4x4 outer)
        O = self.origin
        WELL_DEPTH = 6
        time.sleep(0.1)
        # make bricks blocks for well
        mc.setBlocks(
            O.x - 1, O.y, O.z - 1,
            O.x + 2, O.y - WELL_DEPTH, O.z + 2,
            WELL_BLOCK
        )
        # slab rims
        mc.setBlocks(
            O.x - 1, O.y, O.z, 
            O.x + 2, O.y, O.z + 1,
            BOTTOM_SLAB)
        mc.setBlocks(
            O.x, O.y, O.z - 1, 
            O.x + 1, O.y, O.z + 2,
            BOTTOM_SLAB)


        # clear center
        mc.setBlocks(
            O.x, O.y, O.z,
            O.x + 1, O.y - WELL_DEPTH, O.z + 1,
            Block.AIR
        )
        mc.setBlocks(
            O.x, O.y - WELL_DEPTH + 2, O.z,
            O.x + 1, O.y - WELL_DEPTH + 2, O.z + 1,
            FLUID_BLOCK
        )

        # fence posts
        mc.setBlocks(
            O.x - 1, O.y + 1, O.z - 1,
            O.x - 1, O.y + 2, O.z - 1,
            POST_BLOCK)
        mc.setBlocks(
            O.x + 2, O.y + 1, O.z - 1,
            O.x + 2, O.y + 2, O.z - 1,
            POST_BLOCK)
        mc.setBlocks(
            O.x - 1, O.y + 1, O.z + 2,
            O.x - 1, O.y + 2, O.z + 2,
            POST_BLOCK)
        mc.setBlocks(
            O.x + 2, O.y + 1, O.z + 2,
            O.x + 2, O.y + 2, O.z + 2,
            POST_BLOCK)

        # ROOF
        self.buildRoof()



    def buildRoof(self):
        ROOF_SLAB_TOP = Block.WOODEN_SLAB.withData(8)
        ROOF_SLAB_BOTTOM = Block.WOODEN_SLAB.withData(0)
        O = self.origin

        # first layer
        mc.setBlocks(
            O.x + 3, O.y + 3, O.z,
            O.x - 2, O.y + 3, O.z+1,
            ROOF_SLAB_BOTTOM)
        mc.setBlocks(
            O.x, O.y + 3, O.z - 2,
            O.x+1, O.y + 3, O.z + 3,
            ROOF_SLAB_BOTTOM)
        mc.setBlocks(
            O.x - 1, O.y + 3, O.z - 1,
            O.x + 2, O.y + 3, O.z + 2,
            ROOF_SLAB_BOTTOM)

        # second layer
        mc.setBlocks(
            O.x + 2, O.y + 3, O.z,
            O.x - 1, O.y + 3, O.z+1,
            ROOF_SLAB_TOP)
        mc.setBlocks(
            O.x, O.y + 3, O.z - 1,
            O.x+1, O.y + 3, O.z + 2,
            ROOF_SLAB_TOP)

        # third layer
        mc.setBlocks(
            O.x, O.y + 3, O.z,
            O.x + 1, O.y + 3, O.z + 1,
            Block.AIR
        )



class Lamp(Furniture):
    def __init__(self, origin, height=4, **kwargs):
        self.origin = origin
        self.height = height


    def build(self):
        POST_BLOCK = Block.FENCE
        LAMP_BLOCK = 169
        TRAPDOOR = Block.TRAPDOOR
        BPOS = [
            [self.origin.x - 1, self.origin.y + self.height, self.origin.z],
            [self.origin.x + 1, self.origin.y + self.height, self.origin.z],
            [self.origin.x, self.origin.y + self.height, self.origin.z - 1],
            [self.origin.x, self.origin.y + self.height, self.origin.z + 1]
        ]
        BDATA = [14, 15, 12, 13]
        time.sleep(0.1)
        for i, x in enumerate(BPOS):
            mc.setBlock(x[0], x[1], x[2], TRAPDOOR.withData(BDATA[i]))
        mc.setBlocks(
            self.origin.x, self.origin.y, self.origin.z,
            self.origin.x, self.origin.y + self.height - 1, self.origin.z,
            POST_BLOCK
        )
        mc.setBlock(
            self.origin.x, self.origin.y + self.height, self.origin.z,
            LAMP_BLOCK)
        # trapdoors


class Lightpost(Furniture):

    def __init__(self, origin, rotation, height=4, **kwargs):
        self.origin = origin
        if (type(rotation) == int):
            self.rotation = Orientation(min(max(rotation, 0), 3))
        else:
            self.rotation = rotation

        self.height = max(height, 4)

        # build()

    def getCoordinates(self):
        if (type(self.origin) == "dict"):
            return self.origin
        else:
            return {
                "x": self.origin[0],
                "y": self.origin[1],
                "z": self.origin[2]
            }

    def build(self):
        POST_BLOCK = Block.FENCE
        LAMP_BLOCK = 169

        p = self.origin
        time.sleep(0.1)
        mc.setBlocks(p.x, p.y, p.z,
                     p.x, p.y + self.height, p.z,
                     POST_BLOCK)

        # check if odd or even
        # odd = x axis

        rot = self.rotation.value
        top = [p.x, p.y + self.height, p.z]
        post = list(top)
        if (rot & 1):
            post[0] += (rot - 2) * 2
        else:
            post[2] += (rot - 1) * 2

        mc.setBlocks(
            top[0], top[1], top[2],
            post[0], post[1], post[2],
            POST_BLOCK)
        mc.setBlock(post[0], post[1] - 1, post[2], LAMP_BLOCK)
