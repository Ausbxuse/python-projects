class cube:
    def __init__(self, state):
        self.state = state
        self.color = {
            "w": "\033[48:2:255:255:255m" + "  " + "\x1b[0m",
            "g": "\033[48:2:0:255:0m" + "  " + "\x1b[0m",
            "y": "\033[48:2:255:255:0m" + "  " + "\x1b[0m",
            "b": "\033[48:2:35:35:255m" + "  " + "\x1b[0m",
            "o": "\033[48:2:255:165:0m" + "  " + "\x1b[0m",
            "r": "\033[48:2:255:0:0m" + "  " + "\x1b[0m"
        }

    def __eq__(self, other):
        if not isinstance(other, cube):
            return NotImplemented
        return self.state == other.state

    def __hash__(self):
        return hash((self.state))

    def check_face(self, n):
        if any([all(self.state[n][i] == "w" for i in range(4)),
           all(self.state[n][i] == "g" for i in range(4)),
           all(self.state[n][i] == "y" for i in range(4)),
           all(self.state[n][i] == "b" for i in range(4)),
           all(self.state[n][i] == "o" for i in range(4)),
           all(self.state[n][i] == "r" for i in range(4))]):
            return True
        else:
            return False

    def print_state(self):
        print("   ", self.state[0][0], self.state[0][1])
        print("   ", self.state[0][2], self.state[0][3])
        print(self.state[4][0], self.state[4][1], self.state[1][0],
              self.state[1][1], self.state[5][0], self.state[5][1])
        print(self.state[4][2], self.state[4][3], self.state[1][2],
              self.state[1][3], self.state[5][2], self.state[5][3])
        print("   ", self.state[2][0], self.state[2][1])
        print("   ", self.state[2][2], self.state[2][3])
        print("   ", self.state[3][0], self.state[3][1])
        print("   ", self.state[3][2], self.state[3][3])
        print()

    def print_color(self):
        print("   ", self.color[self.state[0][0]] +
              self.color[self.state[0][1]])
        print("   ", self.color[self.state[0][2]] +
              self.color[self.state[0][3]])
        print(self.color[self.state[4][0]] + self.color[self.state[4][1]] + self.color[self.state[1][0]] +
              self.color[self.state[1][1]] + self.color[self.state[5][0]] + self.color[self.state[5][1]])
        print(self.color[self.state[4][2]] + self.color[self.state[4][3]] + self.color[self.state[1][2]] +
              self.color[self.state[1][3]] + self.color[self.state[5][2]] + self.color[self.state[5][3]])
        print("   ", self.color[self.state[2][0]] +
              self.color[self.state[2][1]])
        print("   ", self.color[self.state[2][2]] +
              self.color[self.state[2][3]])
        print("   ", self.color[self.state[3][0]] +
              self.color[self.state[3][1]])
        print("   ", self.color[self.state[3][2]] +
              self.color[self.state[3][3]])
        print()
