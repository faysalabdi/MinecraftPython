from mcpi.minecraft import Minecraft
import random
import furniture as Furniture
from mcpi.vec3 import Vec3

mc = Minecraft.create()

class gettype:

    floorList = [4, 1, 24, 24, 5, 45]
    floorSubList = [0, 1, 2, 3, 4, 5]
    wallList = [98, 4, 1, 24, 17, 162]
    wallSubList = [0, 0, 2, 0, 1, 0]
    windowList = [0, 102]
    windowSubList = [0, 1, 2, 3, 4, 5]
    rooftypeList = [5, 17, 159, 45]
    rooftypeSubList = [1, 0, 1, 2, 3, 4]
    doorList = [0]
    stairsList = [53, 67, 108, 109, 114, 128, 134, 135, 136, 156, 163, 164, 180]


    floortype = floorList[random.randrange(len(floorList))]
    floorSubColour = floorSubList[random.randrange(len(floorSubList))]
    wall = wallList[random.randrange(len(wallList))]
    wallSubColour = wallSubList[random.randrange(len(wallSubList))]
    window = windowList[random.randrange(len(windowList))]
    windowSubColour = windowSubList[random.randrange(len(windowSubList))]
    rooftype = rooftypeList[random.randrange(len(rooftypeList))]
    rooftypeSubColour = rooftypeSubList[random.randrange(len(rooftypeSubList))]
    door = doorList[random.randrange(len(doorList))]
    stairs = stairsList[random.randrange(len(stairsList))]

    def regenerate():
        gettype.floortype = gettype.floorList[random.randrange(len(gettype.floorList))]
        gettype.floorSubColour = gettype.floorSubList[random.randrange(len(gettype.floorSubList))]
        gettype.wall = gettype.wallList[random.randrange(len(gettype.wallList))]
        gettype.wallSubColour = gettype.wallSubList[random.randrange(len(gettype.wallSubList))]
        gettype.window = gettype.windowList[random.randrange(len(gettype.windowList))]
        gettype.windowSubColour = gettype.windowSubList[random.randrange(len(gettype.windowSubList))]
        gettype.rooftype = gettype.rooftypeList[random.randrange(len(gettype.rooftypeList))]
        gettype.rooftypeSubColour = gettype.rooftypeSubList[random.randrange(len(gettype.rooftypeSubList))]
        gettype.door = gettype.doorList[random.randrange(len(gettype.doorList))]
        gettype.stairs = gettype.stairsList[random.randrange(len(gettype.stairsList))]


def floor(pos, width, length):
    mc.setBlocks(pos.x, pos.y-1, pos.z, pos.x+width, pos.y, pos.z+length, gettype.floortype, gettype.floorSubColour)


def frontWall(pos, width, length, height, swap):
    if swap == False: 
        # front wall
        mc.setBlocks(pos.x+1, pos.y+1, pos.z, pos.x+width-1, pos.y+height-1, pos.z, gettype.wall)
        mc.setBlocks(pos.x, pos.y+1, pos.z, pos.x, pos.y+height-1, pos.z, gettype.wall)
        mc.setBlocks(pos.x+width, pos.y+1, pos.z, pos.x+width, pos.y+height-1, pos.z, gettype.wall)
        mc.setBlocks(pos.x+1, pos.y+1, pos.z+length, pos.x+width-1, pos.y+height-1, pos.z+length, gettype.wall)  
        # front door
        if (height > 2):
            mc.setBlock(pos.x+(width//2), pos.y+1, pos.z, 0, 0)
            mc.setBlock(pos.x+(width//2), pos.y+2, pos.z, 0, 0)

        # front windows
        if (width > 3 and height > 2):
            mc.setBlock(pos.x+(width//2 - 2), pos.y+2, pos.z, gettype.window)
            mc.setBlock(pos.x+(width//2 + 2), pos.y+2, pos.z, gettype.window)
    elif swap == True:
        mc.setBlocks(pos.x+1, pos.y+1, pos.z, pos.x+width-1, pos.y+height, pos.z, gettype.wall)
        mc.setBlocks(pos.x, pos.y+1, pos.z, pos.x, pos.y+height, pos.z, gettype.wall)
        mc.setBlocks(pos.x+width, pos.y+1, pos.z, pos.x+width, pos.y+height, pos.z, gettype.wall)
        mc.setBlocks(pos.x+1, pos.y+1, pos.z+length, pos.x+width-1, pos.y+height, pos.z+length, gettype.wall)  

def backWall(pos, width, length, height, swap):
    if swap == False: 
        mc.setBlocks(pos.x, pos.y+1, pos.z+length, pos.x, pos.y+height-1, pos.z+length, gettype.wall)
        mc.setBlocks(pos.x+width, pos.y+1, pos.z+length, pos.x+width, pos.y+height-1, pos.z+length, gettype.wall)
        mc.setBlocks(pos.x, pos.y+height, pos.z, pos.x+width, pos.y+height, pos.z, gettype.wall)
        mc.setBlocks(pos.x, pos.y+height, pos.z+length, pos.x+width, pos.y+height, pos.z+length, gettype.wall)

    elif swap == True:
        mc.setBlocks(pos.x, pos.y+1, pos.z+length, pos.x, pos.y+height-1, pos.z+length, gettype.wall)
        mc.setBlocks(pos.x+width, pos.y+1, pos.z+length, pos.x+width, pos.y+height-1, pos.z+length, gettype.wall)
        mc.setBlocks(pos.x, pos.y+height, pos.z, pos.x+width, pos.y+height, pos.z, gettype.wall)
        mc.setBlocks(pos.x, pos.y+height, pos.z+length, pos.x+width, pos.y+height, pos.z+length, gettype.wall)

        #south door
        mc.setBlock(pos.x+(width//2), pos.y+1, pos.z+length, 0, 0)
        mc.setBlock(pos.x+(width//2), pos.y+2, pos.z+length, 0, 0)
        # south windows
        mc.setBlock(pos.x+(width//2 - 2), pos.y+2, pos.z+length, gettype.window)
        mc.setBlock(pos.x+(width//2 + 2), pos.y+2, pos.z+length, gettype.window)
        
def sideWalls(pos, width, length, height):
    # left wall
    mc.setBlocks(pos.x, pos.y+1, pos.z+1, pos.x, pos.y+height-1, pos.z+length-1, gettype.wall)
    mc.setBlocks(pos.x+width, pos.y+1, pos.z+1, pos.x+width, pos.y+height-1, pos.z+length-1, gettype.wall)
    
    # right wall
    mc.setBlocks(pos.x, pos.y+height, pos.z, pos.x, pos.y+height, pos.z+length, gettype.wall)
    mc.setBlocks(pos.x+width, pos.y+height, pos.z, pos.x+width, pos.y+height, pos.z+length, gettype.wall)
    
    # windows
    windowSpacing = 3
    for windows in range((length-4) // windowSpacing + 1):
        mc.setBlock(pos.x, pos.y+2, pos.z+2+windows*windowSpacing, gettype.window)
        mc.setBlock(pos.x+width, pos.y+2, pos.z+2+windows*windowSpacing, gettype.window)
    
def roof(pos, width, length, height):
    if (height >= 6):
        for rooftypeLayer in range(width // 2):
            mc.setBlocks(pos.x + rooftypeLayer + 1, pos.y + height + rooftypeLayer + 3, pos.z, pos.x + width - rooftypeLayer - 1, pos.y + height + rooftypeLayer + 1, pos.z, gettype.rooftype)
            mc.setBlocks(pos.x + rooftypeLayer + 1, pos.y + height + rooftypeLayer + 3, pos.z+length, pos.x + width - rooftypeLayer - 1, pos.y + height + rooftypeLayer + 1, pos.z+length, gettype.rooftype)
        for rooftypeLayer in range(width // 2 + 2):
            mc.setBlocks(pos.x-1+rooftypeLayer, pos.y+height+rooftypeLayer + 3, pos.z-1, pos.x-1+rooftypeLayer, pos.y+height+rooftypeLayer, pos.z+length+1, gettype.rooftype)
            mc.setBlocks(pos.x+width+1-rooftypeLayer, pos.y+height+rooftypeLayer + 3, pos.z-1, pos.x+width+1-rooftypeLayer, pos.y+height+rooftypeLayer, pos.z+length+1, gettype.rooftype)

    if (height < 6):
        #rooftype
        mc.setBlocks(pos.x-1, pos.y+height , pos.z-1,  pos.x+width+1, pos.y+height, pos.z+length+1, gettype.rooftype)
        mc.setBlocks(pos.x, pos.y+height+1, pos.z,  pos.x+width, pos.y+height+1, pos.z+length, gettype.rooftype)
        mc.setBlocks(pos.x+1, pos.y+height+2 , pos.z+1,  pos.x+width-1, pos.y+height+2, pos.z+length-1, gettype.rooftype)
        mc.setBlocks(pos.x+2, pos.y+height+3, pos.z + 2,  pos.x+width-2, pos.y+height+3, pos.z+length-2, gettype.rooftype)
 
def secondstory(pos, width, length, height):
    if height >= 6 and length > 5 and width > 5:
        SECOND_FLOOR_HEIGHT = height - 2 
        SECOND_FLOOR_LEVEL = pos.y + SECOND_FLOOR_HEIGHT
        #second floor
        mc.setBlocks(pos.x, SECOND_FLOOR_LEVEL, pos.z,  pos.x+width, SECOND_FLOOR_LEVEL, pos.z+length, gettype.floortype)
        #front windows
        if (height > 5):
            mc.setBlock(pos.x+(width//2 - 2), pos.y+height, pos.z, gettype.window)
            mc.setBlock(pos.x+(width//2 + 2), pos.y+height, pos.z, gettype.window)
            mc.setBlock(pos.x+(width//2 - 2), pos.y+height, pos.z+length, gettype.window)
            mc.setBlock(pos.x+(width//2 + 2), pos.y+height, pos.z+length, gettype.window)

        #side windows
        windowSpacing = 3
        for windows in range((length-4) // windowSpacing + 1):
            mc.setBlock(pos.x, pos.y+height - 1, pos.z+2+windows*windowSpacing, gettype.window)
            mc.setBlock(pos.x+width, pos.y+height - 1, pos.z+2+windows*windowSpacing, gettype.window)

        #hole in top floor for stairs
        mc.setBlocks(pos.x + width - 1, SECOND_FLOOR_LEVEL,  pos.z + length - 2, pos.x + width - 4, SECOND_FLOOR_LEVEL, pos.z + length - 2, 0)
        #staircase
        for i in range(height - 2):
            x = pos.x + width - SECOND_FLOOR_HEIGHT + i
            y = pos.y + 1 + i
            z = pos.z + length - 2
            mc.setBlock(x, y, z, gettype.stairs)

        #torch
        torchSpacing = 5
        for torch in range((length-2) // torchSpacing + 1):
            mc.setBlock(pos.x+1, pos.y+height + 1, pos.z+1+torch*torchSpacing, 50)
            mc.setBlock(pos.x+width-1, pos.y+ height + 1, pos.z+1+torch*torchSpacing, 50)

def room(pos, width, length, height, swap):
    SECOND_FLOOR_HEIGHT = height - 2 
    SECOND_FLOOR_LEVEL = pos.y + SECOND_FLOOR_HEIGHT

    if (width <= 9 and length < 13 and height <=5 ):
        if swap == False:
            chairpos = Vec3(pos.x+(width//2) + 1, pos.y+1, pos.z + length - 1)
            chair = Furniture.Chair(chairpos, length = width-3, rotation=Furniture.Orientation.NORTH)
            chair.build()

        elif swap == True:
            chairpos = Vec3(pos.x+(width//2), pos.y+1, pos.z + 1)
            chair = Furniture.Chair(chairpos, length = width-3, rotation=Furniture.Orientation.SOUTH)
            chair.build()

    if (width >= 10 and width <= 13 and length >= 6 and length <= 13 and height <= 5):
            #wall
        mc.setBlocks(pos.x + (width //4) + 2 , pos.y+1, pos.z+1, pos.x + (width //4) + 2, pos.y+height - 1, pos.z+length-1, gettype.wall)
            #hole in wall for door
        mc.setBlocks(pos.x+(width //4) + 2 , pos.y+1, pos.z+4,   pos.x+(width //4) + 2, pos.y+3, pos.z+5, 0)
        
        tablepos = Vec3(pos.x + 1 ,pos.y+1, pos.z + (length //4) - 1)
        table = Furniture.Table(tablepos, size=(1,1))
        table.build()
        chairpos = Vec3(pos.x + 2 , pos.y+1, pos.z + (length //4) +  0.75 - 1)
        chair = Furniture.Chair(chairpos, rotation=Furniture.Orientation.WEST)
        chair.build()
        


    if (width <= 14 and length > 13 and height <=5 ):
        mc.setBlocks(pos.x + 1 , pos.y+1, pos.z + (length //4) + 4 , pos.x + width - 1, pos.y + height - 1 , pos.z + (length //4) + 4, gettype.wall)

        mc.setBlocks(pos.x + 4 , pos.y+1, pos.z + (length //4) + 4, pos.x + 5, pos.y + 3 , pos.z + (length //4) + 4, 0)

        if swap == False:
            chairpos = Vec3(pos.x+(width//2) + 1, pos.y+1, pos.z + length - 1)
            chair = Furniture.Chair(chairpos, length = width-3, rotation=Furniture.Orientation.NORTH)
            chair.build()

        elif swap == True:
            chairpos = Vec3(pos.x+(width//2) + 1, pos.y+1, pos.z + 1)
            chair = Furniture.Chair(chairpos, length = width-3, rotation=Furniture.Orientation.SOUTH)
            chair.build()
    
    if (width > 14 and length > 13 and height <=5 ):
        mc.setBlocks(pos.x + 1 , pos.y+1, pos.z + (length //4) + 4 , pos.x + width - 1, pos.y + height - 1 , pos.z + (length //4) + 4, gettype.wall)

        mc.setBlocks(pos.x + 4 , pos.y+1, pos.z + (length //4) + 4, pos.x + 5, pos.y + 3 , pos.z + (length //4) + 4, 0)
    

    if (width >= 14 and length > 13 and height >=6 or length >= 10 and height >= 6):
        mc.setBlocks(pos.x + 1 , SECOND_FLOOR_LEVEL, pos.z + (length //4) + 2, pos.x + width - 1, SECOND_FLOOR_LEVEL + 5, pos.z + (length //4) + 2, gettype.wall)

        mc.setBlocks(pos.x + 4 , SECOND_FLOOR_LEVEL, pos.z + (length //4) + 2, pos.x + 5, SECOND_FLOOR_LEVEL + 3 , pos.z + (length //4) + 2, 0)

        tablepos = Vec3(pos.x + 2 , SECOND_FLOOR_LEVEL + 1, pos.z + (length //4) - 1)
        table = Furniture.Table(tablepos, size=(1,1), rotation=Furniture.Orientation.EAST)
        table.build()
        chairpos = Vec3(pos.x + 3 , SECOND_FLOOR_LEVEL + 1, pos.z + (length //4) + 0.75 - 1)
        chair = Furniture.Chair(chairpos, rotation=Furniture.Orientation.WEST)
        chair.build()
        lamppos = Vec3(pos.x + width - 3 , SECOND_FLOOR_LEVEL + 1, pos.z + (length //4) + 0.75 - 1)
        lamp = Furniture.Lamp(lamppos, height = 2)
        lamp.build()
    

#### additional stuff #####   
def torches(pos, width, length):
    torchSpacing = 5
    for torch in range((length-2) // torchSpacing + 1):
        mc.setBlock(pos.x+1, pos.y+1, pos.z+1+torch*torchSpacing, 50)
        mc.setBlock(pos.x+width-1, pos.y+1, pos.z+1+torch*torchSpacing, 50)

def bookshelf(pos, width, length):
    mc.setBlocks(pos.x+width - 1, pos.y+1, pos.z+ 1, pos.x +width - 1, pos.y+2, pos.z + 1, 47)


def house(pos, width, length, height, swap=False):
    gettype.regenerate()
    floor(pos, width, length)
    frontWall(pos, width, length, height, swap)
    backWall(pos, width, length, height, swap)
    sideWalls(pos, width, length, height)
    roof(pos, width, length, height)
    torches(pos, width, length)
    bookshelf(pos, width, length)
    room(pos, width, length, height, swap)
    secondstory(pos, width, length, height)

mc = Minecraft.create()
pos = mc.player.getPos()
pos.x = pos.x+3

# housepos = Vec3(pos.x, mc.getHeight(pos.x,pos.z), pos.z)

# house(pos, random.randint(7,25), random.randint(6,25), random.randint(4,13))