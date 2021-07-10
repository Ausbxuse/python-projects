import numpy as np
from math import cos, sin, pi

class Corner:
    def __init__(self, stickers, ori):
        # stickers
        self.stickers = stickers
        # oriantation
        self.ori = ori

class Edge:
    def __init__(self, stickers, ori):
        # stickers
        self.stickers = stickers
        # oriantation
        self.ori = ori

class Cube:
    def __init__(self):
        # list of corners
        self.corners = [
            Corner("wbo", 0), Corner("wrb", 0), Corner("wog", 0), Corner("wgr", 0),
            Corner("yob", 0), Corner("ybr", 0), Corner("ygo", 0), Corner("yrg", 0)
        ]
        # list of edges
        self.edges = [
            Edge("wb", 0), Edge("wo", 0), Edge("wb", 0), Edge("wg", 0),
            Edge("bo", 0), Edge("br", 0), Edge("go", 0), Edge("gr", 0),
            Edge("yb", 0), Edge("yb", 0), Edge("yb", 0), Edge("yb", 0)
        ]
        # index to corner coord
        self.c_coords = (
            np.array([[-1], [-1], [ 1]]),
            np.array([[-1], [ 1], [ 1]]),
            np.array([[ 1], [-1], [ 1]]),
            np.array([[ 1], [ 1], [ 1]]),

            np.array([[-1], [-1], [-1]]),
            np.array([[-1], [ 1], [-1]]),
            np.array([[ 1], [-1], [-1]]),
            np.array([[ 1], [ 1], [-1]])
        )
        # index to edge coord
        self.ie = (
            np.array([[-1], [ 0], [ 1]]),
            np.array([[ 0], [-1], [ 1]]),
            np.array([[ 0], [ 1], [ 1]]),
            np.array([[ 1], [ 0], [ 1]]),

            np.array([[-1], [-1], [ 0]]),
            np.array([[-1], [ 1], [ 0]]),
            np.array([[ 1], [-1], [ 0]]),
            np.array([[ 1], [ 1], [ 0]]),

            np.array([[-1], [ 0], [-1]]),
            np.array([[ 0], [-1], [-1]]),
            np.array([[ 0], [ 1], [-1]]),
            np.array([[ 1], [ 0], [-1]])
        )

    def index(self, coords, array):
        for i in range(len(coords)):
            if np.array_equal(array, coords[i]):
                return i

    def Rp(self):
        # rotation matrix
        theta = pi / 2
        rMat = np.array([
            [ cos(theta), 0, sin(theta)],
            [          0, 1,          0],
            [-sin(theta), 0, cos(theta)]
        ])
        # set positions for corners
        new1, new2, new3, new4 = [*[rMat.dot(self.c_coords[i]).round().astype(int) for i in range(1, 8, 2)]]

        self.corners[self.index(self.c_coords, new1)], self.corners[self.index(self.c_coords, new2)], self.corners[self.index(self.c_coords, new3)], self.corners[self.index(self.c_coords, new4)] = [*[self.corners[i] for i in range(1, 8, 2)]]

        # set orientations
    def Up(self):
        # rotation matrix
        rMat = np.array([
            [cos(theta), -sin(theta), 0],
            [sin(theta),  cos(theta), 0],
            [         0,           0, 1]
        ])
        # set positions 

        # set orientations

cube1 = Cube()
for i in cube1.corners:
    print(i.stickers)

print()
cube1.Rp()
for i in cube1.corners:
    print(i.stickers)


