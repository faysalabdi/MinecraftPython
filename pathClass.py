import time
from mcpi.minecraft import Minecraft
import random
from mcpi import block
from math import sqrt
mc = Minecraft.create()
# Get player's exact coordinates

x, y, z = mc.player.getTilePos()


class Path:
    def __init__(self, doorsxyz=None):
        self.doorsxyz = doorsxyz
        self.doorsxz = []
        self.doorsSorted = []
        self.firstDoor = None
        self.LastDoor = None
        self.nearestFirstDoor = []
        self.nearestLastDoor = []
        self.startOfPath = None
        self.endOfPath = None
        self.startOfPaths = None
        self.endOfPaths = None
        self.extraDist = None
        self.yavg = 0
        self.pathBlocks = []
        self.i = 0
        self.doors1 = self.doorsxyz.copy()
        self.doorToPathBlock = []
        self.tempPathBlocksDist = []

        self.pathBlock = block.STONE_BRICK

    def vec_distance(self, vector1, vector2):
        distance = 0.0
        for cntr in range(len(vector1)):
            distance += (vector1[cntr] - vector2[cntr]) ** 2
        return sqrt(distance)

    def doorsXZ(self):
        for door in self.doorsxyz:
            self.doorsxz.append((door[0], door[-1]))

    def setDoorsSorted(self):

        for i in range(len(self.doorsxz)):
            for j in range(i + 1, len(self.doorsxz) - 1):

                dist = self.vec_distance(self.doorsxz[i], self.doorsxz[j])
                self.doorsSorted.append(
                    ((self.doorsxz[i], self.doorsxz[j]), dist))

        self.doorsSorted = sorted(self.doorsSorted, key=lambda x: (x[-1]))

    def setFirstDoorAndLastDoor(self):
        self.firstDoor = self.doorsSorted[-1][0][0]
        self.lastDoor = self.doorsSorted[-1][0][1]

    def setNearestFirstAndLastDoor(self):

        for i in range(len(self.doorsxz)):
            if self.vec_distance(self.firstDoor, self.doorsxz[i]) > 0:
                self.nearestFirstDoor.append(
                    (self.doorsxz[i], self.vec_distance(self.firstDoor, self.doorsxz[i])))

        self.nearestFirstDoor = sorted(
            self.nearestFirstDoor, key=lambda x: (x[1]))

        for i in range(len(self.doorsxz)):
            if self.vec_distance(self.lastDoor, self.doorsxz[i]) > 0:
                self.nearestLastDoor.append(
                    (self.doorsxz[i], self.vec_distance(self.lastDoor, self.doorsxz[i])))

        self.nearestLastDoor = sorted(
            self.nearestLastDoor, key=lambda x: (x[1]))
        self.nearestLastDoor = self.nearestLastDoor[0][0]
        self.nearestFirstDoor = self.nearestFirstDoor[0][0]

    def setStartAndEndOfPath(self):
        self.startOfPath = (int((self.firstDoor[0] + self.nearestFirstDoor[0]) / 2), int(
            (self.firstDoor[1] + self.nearestFirstDoor[1]) / 2))

        self.endOfPath = (int((self.lastDoor[0] + self.nearestLastDoor[0]) / 2), int(
            (self.lastDoor[1] + self.nearestLastDoor[1]) / 2))

        self.extraDist = max(abs(
            self.startOfPath[0] - self.endOfPath[0]), abs(self.startOfPath[1] - self.endOfPath[1]))
        self.extraDist = int(self.extraDist * 0.05) + 1

        self.startOfPaths = [((self.startOfPath[0] - self.extraDist, self.startOfPath[1]), self.vec_distance((self.startOfPath[0] - self.extraDist, self.startOfPath[1]), self.endOfPath)),
                             ((self.startOfPath[0], self.startOfPath[1] + self.extraDist), self.vec_distance(
                                 (self.startOfPath[0], self.startOfPath[1] + self.extraDist), self.endOfPath)),
                             ((self.startOfPath[0] + self.extraDist, self.startOfPath[1]), self.vec_distance(
                                 (self.startOfPath[0] + self.extraDist, self.startOfPath[1]), self.endOfPath)),
                             ((self.startOfPath[0], self.startOfPath[1] - self.extraDist), self.vec_distance(
                                 (self.startOfPath[0], self.startOfPath[1] - self.extraDist), self.endOfPath))
                             ]
        self.startOfPaths = sorted(self.startOfPaths, key=lambda x: (x[1]))
        self.startOfPath = self.startOfPaths[-1][0]

        self.endOfPaths = [((self.endOfPath[0] - self.extraDist, self.endOfPath[1]), self.vec_distance((self.endOfPath[0] - self.extraDist, self.endOfPath[1]), self.startOfPath)),
                           ((self.endOfPath[0], self.endOfPath[1] + self.extraDist), self.vec_distance(
                               (self.endOfPath[0], self.endOfPath[1] + self.extraDist), self.startOfPath)),
                           ((self.endOfPath[0] + self.extraDist, self.endOfPath[1]), self.vec_distance(
                               (self.endOfPath[0] + self.extraDist, self.endOfPath[1]), self.startOfPath)),
                           ((self.endOfPath[0], self.endOfPath[1] - self.extraDist), self.vec_distance(
                               (self.endOfPath[0], self.endOfPath[1] - self.extraDist), self.startOfPath))
                           ]

        self.endOfPaths = sorted(self.endOfPaths, key=lambda x: (x[1]))
        self.endOfPath = self.endOfPaths[-1][0]

    def setyavg(self):

        for (x, y, z) in self.doorsxyz:
            self.yavg += y
        self.yavg = int(self.yavg / len(self.doorsxyz))

    def getMainPathStrip(self):
        mc.setBlocks(self.startOfPath[0], self.yavg - 20,  self.startOfPath[1]-1,
                     self.endOfPath[0], self.yavg - 1, self.endOfPath[1]+1, block.STONE_BRICK)

    def setPathBlocks(self):
        istart = min(self.startOfPath[0], self.endOfPath[0])
        iend = max(self.startOfPath[0], self.endOfPath[0])
        jstart = min(self.startOfPath[1], self.endOfPath[1])
        jend = max(self.startOfPath[1], self.endOfPath[1])

        for i in range(istart, iend + 1):
            for j in range(jstart, jend + 1):
                self.pathBlocks.append((i, self.yavg, j))

    def setDoorToPathBlocks(self):
        doors1 = self.doorsxyz.copy()
        while doors1:

            door = self.doorsxyz[self.i]

            for pathBlock in self.pathBlocks:
                self.tempPathBlocksDist.append(
                    (door, pathBlock, self.vec_distance(door, pathBlock)))

            self.tempPathBlocksDist = sorted(
                self.tempPathBlocksDist, key=lambda x: (x[-1]))

            temp = (self.tempPathBlocksDist[0][0], (self.tempPathBlocksDist[0][1][0], int(
                self.tempPathBlocksDist[0][1][1] - 1), self.tempPathBlocksDist[0][1][2]), self.tempPathBlocksDist[0][2])

            self.doorToPathBlock.append(temp)
            self.tempPathBlocksDist = []
            doors1.pop(0)
            self.i += 1

        # y

    def Xp1YZ(self, x, y, z):
        return mc.setBlock(x + 1, y, z, self.pathBlock)

    def Xm1YZ(self, x, y, z):
        return mc.setBlock(x - 1, y, z, self.pathBlock)

    def XYZp1(self, x, y, z):
        return mc.setBlock(x, y, z + 1, self.pathBlock)

    def XYZm1(self, x, y, z):
        return mc.setBlock(x, y, z - 1, self.pathBlock)

        #y - 1

    def Xp1Ym1Z(self, x, y, z):
        return mc.setBlock(x + 1, y - 1, z, self.pathBlock)

    def Xm1Ym1Z(self, x, y, z):
        return mc.setBlock(x - 1, y - 1, z, self.pathBlock)

    def XYm1Zp1(self, x, y, z):
        return mc.setBlock(x, y - 1, z + 1, self.pathBlock)

    def XYm1Zm1(self, x, y, z):
        return mc.setBlock(x, y - 1, z - 1, self.pathBlock)

    #y - 2
    def Xp1Ym2Z(self, x, y, z):
        return mc.setBlock(x + 1, y - 2, z, self.pathBlock)

    def Xm1Ym2Z(self, x, y, z):
        return mc.setBlock(x - 1, y - 2, z, self.pathBlock)

    def XYm2Zp1(self, x, y, z):
        return mc.setBlock(x, y - 2, z + 1, self.pathBlock)

    def XYm2Zm1(self, x, y, z):
        return mc.setBlock(x, y - 2, z - 1, self.pathBlock)

    def connectDoorToPathStrip(self):
        for door, path, dist in self.doorToPathBlock:
            count = 0
            walk = door
            print(door)
            print(door)
            
            mc.postToChat(door)
            while self.vec_distance(walk, path) > 0:
                count += 1
                # time.sleep(0.5)
                if count == 100:

                    break
                # y  -  1
                if self.vec_distance((walk[0], walk[1] - 1, walk[2]), path) < self.vec_distance(walk, path):

                    # (x + 1, y - 1, z)
                    if self.vec_distance((walk[0] + 1, walk[1] - 1, walk[2]), path) < self.vec_distance((walk[0], walk[1] - 1, walk[2]),
                                                                                                        path):
                        self.Xp1Ym1Z(walk[0], walk[1], walk[2])
                        walk = (walk[0] + 1, walk[1] - 1, walk[2])

                    # (x - 1, y - 1, z)
                    elif self.vec_distance((walk[0] - 1, walk[1] - 1, walk[2]), path) < self.vec_distance((walk[0], walk[1] - 1, walk[2]),
                                                                                                          path):
                        self.Xm1Ym1Z(walk[0], walk[1], walk[2])
                        walk = (walk[0] - 1, walk[1] - 1, walk[2])

                    # (x , y - 1, z + 1)
                    elif self.vec_distance((walk[0], walk[1] - 1, walk[2] + 1), path) < self.vec_distance((walk[0], walk[1] - 1, walk[2]),
                                                                                                          path):
                        self.XYm1Zp1(walk[0], walk[1], walk[2])
                        walk = (walk[0], walk[1] - 1, walk[2] + 1)

                    # (x , y + 1, z - 1)
                    elif self.vec_distance((walk[0], walk[1] - 1, walk[2] - 1), path) < self.vec_distance((walk[0], walk[1] - 1, walk[2]),
                                                                                                          path):
                        self.XYm1Zm1(walk[0], walk[1], walk[2])
                        walk = (walk[0], walk[1] - 1, walk[2] - 1)

                # y - 2
                elif self.vec_distance((walk[0], walk[1] - 2, walk[2]), path) < self.vec_distance(walk, path):

                    # (x + 1, y - 2, z)
                    if self.vec_distance((walk[0] + 1, walk[1] - 2, walk[2]), path) < self.vec_distance((walk[0], walk[1] - 2, walk[2]),
                                                                                                        path):
                        self.Xp1Ym2Z(walk[0], walk[1], walk[2])
                        walk = (walk[0] + 1, walk[1] - 2, walk[2])

                    # (x - 1, y - 2, z)
                    elif self.vec_distance((walk[0] - 1, walk[1] - 2, walk[2]), path) < self.vec_distance((walk[0], walk[1] - 2, walk[2]),
                                                                                                          path):
                        self.Xm1Ym2Z(walk[0], walk[1], walk[2])
                        walk = (walk[0] - 1, walk[1] - 2, walk[2])

                    # (x , y - 2, z + 1)
                    elif self.vec_distance((walk[0], walk[1] - 2, walk[2] + 1), path) < self.vec_distance((walk[0], walk[1] - 2, walk[2]),
                                                                                                          path):
                        self.XYm2Zp1(walk[0], walk[1], walk[2])
                        walk = (walk[0], walk[1] - 2, walk[2] + 1)

                    # (x , y - 1, z - 1)
                    elif self.vec_distance((walk[0], walk[1] - 2, walk[2] - 1), path) < self.vec_distance((walk[0], walk[1] - 2, walk[2]),
                                                                                                          path):
                        self.XYm2Zm1(walk[0], walk[1], walk[2])
                        walk = (walk[0], walk[1] - 2, walk[2] - 1)

                # y
                else:
                    # (x + 1, y , z)
                    if self.vec_distance((walk[0] + 1, walk[1], walk[2]), path) < self.vec_distance(walk, path):

                        self.Xp1YZ(walk[0], walk[1], walk[2])
                        walk = (walk[0] + 1, walk[1] + 1, walk[2])

                    # (x - 1, y , z)
                    elif self.vec_distance((walk[0] - 1, walk[1], walk[2]), path) < self.vec_distance(walk, path):

                        self.Xm1YZ(walk[0], walk[1], walk[2])
                        walk = (walk[0] - 1, walk[1] + 1, walk[2])

                    # (x , y , z + 1)
                    elif self.vec_distance((walk[0], walk[1], walk[2] + 1), path) < self.vec_distance(walk, path):

                        self.XYZp1(walk[0], walk[1], walk[2])
                        walk = (walk[0], walk[1] + 1, walk[2] + 1)

                    # (x , y , z - 1)
                    elif self.vec_distance((walk[0], walk[1], walk[2] - 1), path) < self.vec_distance(walk, path):

                        self.XYZm1(walk[0], walk[1], walk[2])
                        walk = (walk[0], walk[1] + 1, walk[2] - 1)

    def build(self):
        self.doorsXZ()

        self.setDoorsSorted()
        self.setFirstDoorAndLastDoor()
        self.setNearestFirstAndLastDoor()
        self.setStartAndEndOfPath()
        self.setyavg()
        self.getMainPathStrip()
        self.setPathBlocks()
        self.setDoorToPathBlocks()
        self.connectDoorToPathStrip()
