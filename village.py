from mcpi.minecraft import Minecraft
from pillar import Plots, Pillar
from pathClass import Path
from house import house
import random
import math
# Assignment 1 main file
# Feel free to modify, and/or to add other modules/classes in this or other files

mc = Minecraft.create()
mc.postToChat("Hello world")


# build the plots
build_pos = (random.randint(-5000, 5000), random.randint(-5000, 5000))
mc.player.setPos(build_pos[0], 128, build_pos[1])


plots = Plots()
plots.setCenter(build_pos[0], build_pos[1])
plots.build()



HOUSE_HEIGHT_MIN = 4
HOUSE_HEIGHT_MAX = 10
doors = []
for plot, north in plots.getAllPlots():
    housePos = plot.getPos()
    houseSize = plot.getPosSize()[2:]
    houseHeight = min(houseSize[0], random.randint(HOUSE_HEIGHT_MIN, HOUSE_HEIGHT_MAX))

    house(housePos, houseSize[0]-1,houseSize[1]-1, houseHeight, north)
    doorZ = housePos.z + houseSize[1]-1 if north else housePos.z
    doorPos = (housePos.x + math.floor(houseSize[0] / 2) + (0 if houseSize[0] & 1 else -1),
        housePos.y + 1,
        doorZ
        )
    print(f"door position: {doorPos}")
    mc.postToChat(f"door position: {doorPos}")
    doors.append(doorPos
    )


# time.sleep(1)
path = Path(doors)
path.build()


