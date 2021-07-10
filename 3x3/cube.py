import numpy as np
from math import cos, sin, pi

class Corner:
    def __init__(self, stickers, ori):
        # stickers
        self.stickers = stickers

    def counter(self):
        self.stickers = self.stickers[-1:] + self.stickers[:1] + self.stickers[1:-1]

    def clock(self):
        self.stickers = self.stickers[1:-1] + self.stickers[-1:] + self.stickers[:1]

class Edge:
    def __init__(self, stickers, ori):
        # stickers
        self.stickers = stickers
        # oriantation

    def turn(self):
        self.stickers = self.stickers[-1:] + self.stickers[:1]

class Cube:
    def __init__(self):
        # list of corners
        self.corners = [
            Corner("wbo", 0), Corner("wrb", 0), Corner("wog", 0), Corner("wgr", 0),
            Corner("yob", 0), Corner("ybr", 0), Corner("ygo", 0), Corner("yrg", 0)
        ]
        # list of edges
        self.edges = [
            Edge("wb", 0), Edge("wo", 0), Edge("wr", 0), Edge("wg", 0),
            Edge("bo", 0), Edge("br", 0), Edge("go", 0), Edge("gr", 0),
            Edge("yb", 0), Edge("yo", 0), Edge("yr", 0), Edge("yg", 0)
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
        self.e_coords = (
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

        self.color = {
            "w": "\033[48:2:255:255:255m"+ "  " + "\x1b[0m",
            "g": "\033[48:2:0:255:0m"+ "  " + "\x1b[0m",
            "y": "\033[48:2:255:255:0m"+ "  " + "\x1b[0m",
            "b": "\033[48:2:35:35:255m"+ "  " + "\x1b[0m",
            "o": "\033[48:2:255:165:0m" + "  " + "\x1b[0m",
            "r": "\033[48:2:255:0:0m"+ "  " + "\x1b[0m"
        }
    def print_color(self):
        print("      ", self.color[self.corners[0].stickers[0]] + self.color[self.edges[0].stickers[0]] + self.color[self.corners[1].stickers[0]])
        print("      ", self.color[self.edges[1].stickers[0]] + self.color["w"] + self.color[self.edges[2].stickers[0]])
        print("      ", self.color[self.corners[2].stickers[0]] + self.color[self.edges[3].stickers[0]] + self.color[self.corners[3].stickers[0]])

        print(
              self.color[self.corners[0].stickers[2]] + self.color[self.edges[1].stickers[1]] + self.color[self.corners[2].stickers[1]],
              self.color[self.corners[2].stickers[2]] + self.color[self.edges[3].stickers[1]] + self.color[self.corners[3].stickers[1]],
              self.color[self.corners[3].stickers[2]] + self.color[self.edges[2].stickers[1]] + self.color[self.corners[1].stickers[1]],
              self.color[self.corners[1].stickers[2]] + self.color[self.edges[0].stickers[1]] + self.color[self.corners[0].stickers[1]]
        )
        print(
              self.color[self.edges[4].stickers[1]] + self.color["o"] + self.color[self.edges[6].stickers[1]],
              self.color[self.edges[6].stickers[0]] + self.color["g"] + self.color[self.edges[7].stickers[0]],
              self.color[self.edges[7].stickers[1]] + self.color["r"] + self.color[self.edges[5].stickers[1]],
              self.color[self.edges[5].stickers[0]] + self.color["b"] + self.color[self.edges[4].stickers[0]]
        )
        print(
              self.color[self.corners[4].stickers[1]] + self.color[self.edges[9].stickers[1]] + self.color[self.corners[6].stickers[2]],
              self.color[self.corners[6].stickers[1]] + self.color[self.edges[11].stickers[1]] + self.color[self.corners[7].stickers[2]],
              self.color[self.corners[7].stickers[1]] + self.color[self.edges[10].stickers[1]] + self.color[self.corners[5].stickers[2]],
              self.color[self.corners[5].stickers[1]] + self.color[self.edges[8].stickers[1]] + self.color[self.corners[4].stickers[2]]
        )

        print("      ", self.color[self.corners[6].stickers[0]] + self.color[self.edges[11].stickers[0]] + self.color[self.corners[7].stickers[0]])
        print("      ", self.color[self.edges[9].stickers[0]] + self.color["y"] + self.color[self.edges[10].stickers[0]])
        print("      ", self.color[self.corners[4].stickers[0]] + self.color[self.edges[8].stickers[0]] + self.color[self.corners[5].stickers[0]])

    def index(self, coords, array):
        for i in range(len(coords)):
            if np.array_equal(array, coords[i]):
                return i

    def move(self, direction, angle, lst, lst1):
        theta = angle
        if direction == "xy":
            rMat = np.array([
                [cos(theta), -sin(theta), 0],
                [sin(theta),  cos(theta), 0],
                [         0,           0, 1]
            ])
        elif direction == "yz":
            rMat = np.array([
                [1,          0,           0],
                [0, cos(theta), -sin(theta)],
                [0, sin(theta),  cos(theta)]
            ])

        elif direction == "zx":
            rMat = np.array([
                [ cos(theta), 0, sin(theta)],
                [          0, 1,          0],
                [-sin(theta), 0, cos(theta)]
            ])

        new1, new2, new3, new4 = [rMat.dot(self.c_coords[i]).round().astype(int) for i in lst]
        self.corners[self.index(self.c_coords, new1)], self.corners[self.index(self.c_coords, new2)], self.corners[self.index(self.c_coords, new3)], self.corners[self.index(self.c_coords, new4)] = [self.corners[i] for i in lst]

        new1, new2, new3, new4 = [rMat.dot(self.e_coords[i]).round().astype(int) for i in lst1]
        self.edges[self.index(self.e_coords, new1)], self.edges[self.index(self.e_coords, new2)], self.edges[self.index(self.e_coords, new3)], self.edges[self.index(self.e_coords, new4)] = [self.edges[i] for i in lst1]


    def Rp(self):
        # set positions for corners
        self.move("zx", pi / 2, [1, 3, 5, 7], [2, 5, 7, 10])

        # set orientations for corners
        self.corners[1].clock()
        self.corners[3].counter()
        self.corners[5].counter()
        self.corners[7].clock()

    def R(self):
        # set positions for corners and edges
        self.move("zx", 3 * pi / 2, [1, 3, 5, 7], [2, 5, 7, 10])

        # set orientations for corners
        self.corners[1].clock()
        self.corners[3].counter()
        self.corners[5].counter()
        self.corners[7].clock()

    def R2(self):
        # set positions for corners and edges
        self.move("zx", pi, [1, 3, 5, 7], [2, 5, 7, 10])

    def L(self):
        # set positions
        self.move("zx", pi / 2, [0, 2, 4, 6], [1, 4, 6, 9])

        # set orientations for corners
        self.corners[0].clock()
        self.corners[2].counter()
        self.corners[4].counter()
        self.corners[6].clock()

    def Lp(self):
        # set positions
        self.move("zx", 3 * pi / 2, [0, 2, 4, 6], [1, 4, 6, 9])

        # set orientations for corners
        self.corners[0].clock()
        self.corners[2].counter()
        self.corners[4].counter()
        self.corners[6].clock()

    def L2(self):
        self.move("zx", pi, [0, 2, 4, 6], [1, 4, 6, 9])

    def Up(self):
        # set positions for corners
        self.move("xy", pi / 2, range(4), range(4))

    def U(self):
        # set positions for corners
        self.move("xy", 3 * pi / 2, range(4), range(4))

    def U2(self):
        # set positions for corners
        self.move("xy", pi, range(4), range(4))

    def D(self):
        # set positions
        self.move("xy", pi / 2, range(4, 8), [8, 9, 10, 11])

    def Dp(self):
        # set positions
        self.move("xy", 3 * pi / 2, range(4, 8), [8, 9, 10, 11])

    def D2(self):
        # set positions
        self.move("xy", pi, range(4, 8), [8, 9, 10, 11])

    def Fp(self):
        # set positions for corners
        self.move("yz", pi / 2, [2, 3, 6, 7], [3, 6, 7, 11])

        # set orientations for corners
        self.corners[2].counter()
        self.corners[3].clock()
        self.corners[6].clock()
        self.corners[7].counter()

        # set edge orientations
        for i in [3, 6, 7, 11]:
            self.edges[i].turn()

    def F(self):
        # set positions for corners
        self.move("yz", 3 * pi / 2, [2, 3, 6, 7], [3, 6, 7, 11])

        # set orientations for corners
        self.corners[2].counter()
        self.corners[3].clock()
        self.corners[6].clock()
        self.corners[7].counter()

        # set edge orientations
        for i in [3, 6, 7, 11]:
            self.edges[i].turn()

    def F2(self):
        # set positions for corners
        self.move("yz", pi, [2, 3, 6, 7], [3, 6, 7, 11])

    def B(self):
        # set positions for corners
        self.move("yz", pi / 2, [0, 1, 4, 5], [0, 4, 5, 8])

        # set orientations for corners
        self.corners[0].counter()
        self.corners[1].clock()
        self.corners[4].clock()
        self.corners[5].counter()

        # set edge orientations
        for i in [0, 4, 5, 8]:
            self.edges[i].turn()

    def Bp(self):
        # set positions for corners
        self.move("yz", 3 * pi / 2, [0, 1, 4, 5], [0, 4, 5, 8])

        # set orientations for corners
        self.corners[0].counter()
        self.corners[1].clock()
        self.corners[4].clock()
        self.corners[5].counter()

        # set edge orientations
        for i in [0, 4, 5, 8]:
            self.edges[i].turn()

    def B2(self):
        # set positions for corners
        self.move("yz", pi, [0, 1, 4, 5], [0, 4, 5, 8])

if __name__ == "__main__":
    cube1 = Cube()

    while True:
        move = input("Please enter your move: ")
        if move == "R":
            cube1.R()
            cube1.print_color()
        elif move == "R2":
            cube1.R2()
            cube1.print_color()
        elif move == "R'":
            cube1.Rp()
            cube1.print_color()

        elif move == "U":
            cube1.U()
            cube1.print_color()
        elif move == "U2":
            cube1.U2()
            cube1.print_color()
        elif move == "U'":
            cube1.Up()
            cube1.print_color()

        elif move == "F":
            cube1.F()
            cube1.print_color()
        elif move == "F2":
            cube1.F2()
            cube1.print_color()
        elif move == "F'":
            cube1.Fp()
            cube1.print_color()

        elif move == "B":
            cube1.B()
            cube1.print_color()
        elif move == "B2":
            cube1.B2()
            cube1.print_color()
        elif move == "B'":
            cube1.Bp()
            cube1.print_color()

        elif move == "L":
            cube1.L()
            cube1.print_color()
        elif move == "L2":
            cube1.L2()
            cube1.print_color()
        elif move == "L'":
            cube1.Lp()
            cube1.print_color()

        elif move == "D":
            cube1.D()
            cube1.print_color()
        elif move == "D2":
            cube1.D2()
            cube1.print_color()
        elif move == "D'":
            cube1.Dp()
            cube1.print_color()

        elif move == "q":
            break
    quit(0)
