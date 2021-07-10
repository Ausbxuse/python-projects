import time
from cube import cube

def R(c):
    wtl = c.state[0][0]
    wtr = c.state[1][1]
    wbl = c.state[0][2]
    wbr = c.state[1][3]

    gtl = c.state[1][0]
    gtr = c.state[2][1]
    gbl = c.state[1][2]
    gbr = c.state[2][3]

    ytl = c.state[2][0]
    ytr = c.state[3][1]
    ybl = c.state[2][2]
    ybr = c.state[3][3]

    btl = c.state[3][0]
    btr = c.state[0][1]
    bbl = c.state[3][2]
    bbr = c.state[0][3]

    otl = c.state[4][0]
    otr = c.state[4][1]
    obl = c.state[4][2]
    obr = c.state[4][3]

    rtl = c.state[5][2]
    rtr = c.state[5][0]
    rbl = c.state[5][3]
    rbr = c.state[5][1]
    newcube = cube((
        (wtl, wtr,
         wbl, wbr),
        (gtl, gtr,
         gbl, gbr),
        (ytl, ytr,
         ybl, ybr),
        (btl, btr,
         bbl, bbr),
        (otl, otr,
         obl, obr),
        (rtl, rtr,
         rbl, rbr),
    ))
    return newcube
def R2(c):
    tmp = R(c)
    return R(tmp)
def RP(c):
    tmp = R(c)
    tmp2 = R(tmp)
    return R(tmp2)

def U(c):
    wtl = c.state[0][2]
    wtr = c.state[0][0]
    wbl = c.state[0][3]
    wbr = c.state[0][1]

    gtl = c.state[5][0]
    gtr = c.state[5][1]
    gbl = c.state[1][2]
    gbr = c.state[1][3]

    ytl = c.state[2][0]
    ytr = c.state[2][1]
    ybl = c.state[2][2]
    ybr = c.state[2][3]

    btl = c.state[3][0]
    btr = c.state[3][1]
    bbl = c.state[4][1]
    bbr = c.state[4][0]

    otl = c.state[1][0]
    otr = c.state[1][1]
    obl = c.state[4][2]
    obr = c.state[4][3]

    rtl = c.state[3][3]
    rtr = c.state[3][2]
    rbl = c.state[5][2]
    rbr = c.state[5][3]
    newcube = cube((
        (wtl, wtr,
         wbl, wbr),
        (gtl, gtr,
         gbl, gbr),
        (ytl, ytr,
         ybl, ybr),
        (btl, btr,
         bbl, bbr),
        (otl, otr,
         obl, obr),
        (rtl, rtr,
         rbl, rbr),
    ))
    return newcube
def U2(c):
    tmp = U(c)
    return U(tmp)
def UP(c):
    tmp = U(c)
    tmp2 = U(tmp)
    return U(tmp2)

def F(c):
    wtl = c.state[0][0]
    wtr = c.state[0][1]
    wbl = c.state[4][3]
    wbr = c.state[4][1]

    gtl = c.state[1][2]
    gtr = c.state[1][0]
    gbl = c.state[1][3]
    gbr = c.state[1][1]

    ytl = c.state[5][2]
    ytr = c.state[5][0]
    ybl = c.state[2][2]
    ybr = c.state[2][3]

    btl = c.state[3][0]
    btr = c.state[3][1]
    bbl = c.state[3][2]
    bbr = c.state[3][3]

    otl = c.state[4][0]
    otr = c.state[2][0]
    obl = c.state[4][2]
    obr = c.state[2][1]

    rtl = c.state[0][2]
    rtr = c.state[5][1]
    rbl = c.state[0][3]
    rbr = c.state[5][3]
    newcube = cube((
        (wtl, wtr,
         wbl, wbr),
        (gtl, gtr,
         gbl, gbr),
        (ytl, ytr,
         ybl, ybr),
        (btl, btr,
         bbl, bbr),
        (otl, otr,
         obl, obr),
        (rtl, rtr,
         rbl, rbr),
    ))
    return newcube
def F2(c):
    tmp = F(c)
    return F(tmp)
def FP(c):
    tmp = F(c)
    tmp2 = F(tmp)
    return F(tmp2)

def get_neighbors(cube):
    rcube = R(cube)
    ucube = U(cube)
    fcube = F(cube)
    r2cube = R2(cube)
    u2cube = U2(cube)
    f2cube = F2(cube)
    rpcube = RP(cube)
    upcube = UP(cube)
    fpcube = FP(cube)
    lst = [rcube, ucube, fcube, r2cube, u2cube, f2cube, rpcube, upcube, fpcube]
    return lst
    #return [R(cube), L(cube), U(cube), D(cube), F(cube), B(cube)]
solved = cube((
    ("w","w",
     "w","w"),
    ("g","g",
     "g","g"),
    ("y","y",
     "y","y"),
    ("b","b",
     "b","b"),
    ("o","o",
     "o","o"),
    ("r","r",
     "r","r"),
))

def turn(c, move):
    if move == "R":
        return R(c)
    elif move == "U":
        return U(c)
    elif move == "F":
        return F(c)
    elif move == "R2":
        return R2(c)
    elif move == "U2":
        return U2(c)
    elif move == "F2":
        return F2(c)
    elif move == "R'":
        return RP(c)
    elif move == "U'":
        return UP(c)
    elif move == "F'":
        return FP(c)

color = ("w", "g", "y", "b", "o", "r")
class graph:
    def __init__(self, scrambled):
        self.scrambled = scrambled
        self.parents = {}
        self.level = {}
        self.frontier = []
        self.solution = []

    def set_source(self, scrambled):
        self.parents[scrambled] = None
        self.level[scrambled] = 0
        self.frontier.append(scrambled)

    def search(self, parent):
        begin = time.time()
        i = 1
        found = False
        while self.frontier and not found:
            next = []
            for u in self.frontier:
                if not found:
                    for v in get_neighbors(u):
                        if v not in self.level and not found:
                            self.level[v] = i
                            self.parents[v] = u
                            next.append(v)
                            if all(v.check_face(i) for i in range(6)):
                                print("Solution found! Took ", time.time() - begin, "s", sep = '')
                                print("Your solution is...")
                                while self.parents[v] != None:
                                    if R(self.parents[v]) == v:
                                        self.solution.append("R")
                                    elif U(self.parents[v]) == v:
                                        self.solution.append("U")
                                    elif F(self.parents[v]) == v:
                                        self.solution.append("F")
                                    elif R2(self.parents[v]) == v:
                                        self.solution.append("R2")
                                    elif U2(self.parents[v]) == v:
                                        self.solution.append("U2")
                                    elif F2(self.parents[v]) == v:
                                        self.solution.append("F2")
                                    elif RP(self.parents[v]) == v:
                                        self.solution.append("R'")
                                    elif UP(self.parents[v]) == v:
                                        self.solution.append("U'")
                                    elif FP(self.parents[v]) == v:
                                        self.solution.append("F'")
                                    v = self.parents[v]
                                found = True
                                break
                else:
                    break
            self.frontier = next
            i += 1


if __name__ == "__main__":
    scramble = input("Scramble the cube by entering a sequence of moves(in all caps): ")
    scramble = scramble.replace(" ", "")
    scrambled = solved
    i = 0
    while i < len(scramble):
        if i + 1 < len(scramble):
            if scramble[i + 1] == "'" or scramble[i + 1] == "2":
                ex = scramble[i] + scramble[i+1]
                scrambled = turn(scrambled, ex)
                i += 1
            else:
                scrambled = turn(scrambled, scramble[i])
        elif i + 1 == len(scramble):
            scrambled = turn(scrambled, scramble[i])
        i += 1
    scrambled.print_color()

    print("Finding solution...")
    graph = graph(scrambled)
    graph.set_source(scrambled)
    graph.search(scrambled)

    for i in range(len(graph.solution) - 1, -1, -1):
        print(graph.solution[i], end = ' ')
