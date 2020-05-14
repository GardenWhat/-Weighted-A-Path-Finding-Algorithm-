# rect = [(2,1), (2,6), (17,1), (17,6)]
# pentagon = [(1,9), (0,14), (6,19), (9,15), (7,8)]
# tri1 = [(12,15), (10,8), (14,8)]
# rhombus = [(14,19), (18,20), (14,13), (20,17)]
# tri2 = [(18,10), (19,3), (23,6)]
# rect2 = [(22,19), (28,19), (22,9), (28,9)]
# poly = [(29,17), (31,19), (34,16), (32,8)]
# hexagon = [(29,8), (31,6), (31,2), (28,1), (25,2), (25,6)]
# start = (1,3)
# goal = (34,19)
import math
import time
import pygame
from pip._vendor.distlib.compat import raw_input

pygame.init()


class Node:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.parent = None
        self.H = 0
        self.G = 0
        self.children = []

    def cost(self):
        if self.parent:
            return int(math.sqrt((self.x - self.parent.x) ** 2) + math.sqrt(
                (self.y - self.parent.y) ** 2))
        else:
            return 0


def ED(current, goal):
    if not current == goal:
        return int(math.sqrt((goal.x - current.x) ** 2) + math.sqrt((goal.y - current.y) ** 2))
    else:
        return 0


def aStar(start, goal, costBound):
    openList = set()
    closedList = set()
    current = start

    # sets the start nodes heuristic
    current.H = ED(current, goal)

    # adds start to open list
    openList.add(current)

    # while there are nodes in the open list
    while openList:

        # set the current node to the max u(n)
        current = max(openList, key=lambda o: (costBound - o.G) / o.H)

        # removes current from open list
        openList.remove(current)

        # adds current to closed list
        closedList.add(current)

        # If found a solution below the bound - return it
        if current == goal and current.G <= costBound:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]

        # for each child
        for node in current.children:
            # Duplicate detection and updating g(n`)
            if node in closedList and node.G <= current.G + node.cost():
                continue
            if node in openList and node.G <= current.G + node.cost():
                continue
            if current.parent:
                current.G = current.parent.G + current.cost()

            # Prune nodes over the bound
            if node.G + node.H >= costBound:
                continue
            if node in openList:
                new_g = current.G + node.cost()
                if node.G > new_g:
                    node.G = new_g
                    node.parent = current
            else:
                node.parent = current
                node.G = current.G + node.cost()
                if not node == goal:
                    node.H = ED(node, goal)
                else:
                    node.H = 1
                openList.add(node)
    print("no solution exists that is under the cost bound C")
    return None


GRID_SIZE = 30
GRID_X = 35
GRID_Y = 20
screen = pygame.display.set_mode((GRID_X * GRID_SIZE, GRID_Y * GRID_SIZE))
pygame.display.set_caption('A* Algorithm')
WHITE = (255, 255, 255)

while True:
    pygame.event.get()
    screen.fill(WHITE)
    pygame.display.update()
    isOriginal = True
    while True:
        temp = raw_input("Enter o for Original or n for New environment: ")
        if temp == "o":
            break
        if temp == "n":
            isOriginal = False
            break
    costBound = int(raw_input("Enter a cost bound: "))
    pygame.display.update()

    if isOriginal:
        # start
        S = Node(1, 3, "S")

        # goal
        G = Node(34, 19, "G")

        # ORIGINAL (3.31 graph)
        # /////////////////////////////////////////////////////////////////////////////////////////////////
        # rect = [(2,1), (2,6), (17,1), (17,6)]
        A1 = Node(2, 1, "A1")
        A2 = Node(2, 6, "A2")
        A3 = Node(17, 6, "A3")
        A4 = Node(17, 1, "A4")

        # pentagon = [(1,9), (0,14), (6,19), (9,15), (7,8)]
        B1 = Node(1, 9, "B1")
        B2 = Node(0, 14, "B2")
        B3 = Node(6, 19, "B3")
        B4 = Node(9, 15, "B4")
        B5 = Node(7, 8, "B5")

        # tri1 = [(12,15), (10,8), (14,8)]
        C1 = Node(12, 15, "C1")
        C2 = Node(10, 8, "C2")
        C3 = Node(14, 8, "C3")

        # rhombus = [(14,19), (18,20), (14,13), (20,17)]
        D1 = Node(14, 19, "D1")
        D2 = Node(18, 20, "D2")
        D3 = Node(20, 17, "D3")
        D4 = Node(14, 13, "D4")

        # tri2 = [(18,10), (19,3), (23,6)]
        E1 = Node(18, 10, "E1")
        E2 = Node(19, 3, "E2")
        E3 = Node(23, 6, "E3")

        # rect2 = [(22,19), (28,19), (22,9), (28,9)]
        F1 = Node(22, 19, "F1")
        F2 = Node(28, 19, "F2")
        F3 = Node(28, 9, "F3")
        F4 = Node(22, 9, "F4")

        # poly = [(29,17), (31,19), (34,16), (32,8)]
        G1 = Node(29, 17, "G1")
        G2 = Node(31, 19, "G2")
        G3 = Node(34, 16, "G3")
        G4 = Node(32, 8, "G4")

        # hexagon = [(29,8), (31,6), (31,2), (28,1), (25,2), (25,6)]
        H1 = Node(29, 8, "H1")
        H2 = Node(31, 6, "H2")
        H3 = Node(31, 2, "H3")
        H4 = Node(28, 1, "H4")
        H5 = Node(25, 2, "H5")
        H6 = Node(25, 6, "H6")

        S.children = [A1, A2, B1, B2]
        A1.children = [S, A2, A4]
        A2.children = [S, A1, A3, B1, B5, C2, C3]
        A3.children = [A2, A4, C2, C3, D4, E1, E2]
        A4.children = [A1, A3, E1, E2, F3, H4, H5, H6]
        B1.children = [S, A2, B2, B5]
        B2.children = [S, B1, B3]
        B3.children = [B2, B4, C1, D1]
        B4.children = [B3, B5, C1, C2, D1]
        B5.children = [B1, B4, A2, C1, C2]
        C1.children = [B3, B4, B5, C2, C3, D1, D4]
        C2.children = [A2, A3, B4, B4, B5, C1, C3]
        C3.children = [A2, A3, C1, C2, D3, D4, E1]
        D1.children = [B3, B4, C1, D2, D4]
        D2.children = [D1, D3, F1]
        D3.children = [D2, D4, C3, E1, F1, F4]
        D4.children = [A3, C1, C3, E1, E2, F4, D3, D1]
        E1.children = [A3, C3, D4, D3, F4, E2, E3]
        E2.children = [A3, A4, D4, E1, E3, H4, H5, H6]
        E3.children = [E1, E2, F4, F3, H1, H5, H6]
        F1.children = [D2, D3, F2, F4]
        F2.children = [F1, F3, G1, G2]
        F3.children = [E3, F2, F4, G1, G4, H1, H6]
        F4.children = [D3, D4, E1, E3, F1, F3, H1, H6]
        G1.children = [F2, F3, G2, G4, H1, H2]
        G2.children = [F2, G1, G3, G]
        G3.children = [G2, G4, G]
        G4.children = [F3, G1, G3, H1, H2, H3]
        H1.children = [E3, F3, F4, G1, G4, H2, H6]
        H2.children = [F2, G1, G4, H1, H3]
        H3.children = [H2, H4]
        H4.children = [A3, E3, H3, H5]
        H5.children = [A3, E2, E3, H4, H6]
        H6.children = [A3, E2, E3, F4, F3, H1, H5]

        path = aStar(S, G, costBound)
        start = pygame.draw.circle(screen, (0, 255, 0), (S.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - S.y * GRID_Y), 7)

        # RECTANGLE1
        pygame.draw.line(screen, 0, (A1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A1.y * GRID_Y),
                         (A2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A2.y * GRID_Y))
        pygame.draw.line(screen, 0, (A2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A2.y * GRID_Y),
                         (A3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A3.y * GRID_Y))
        pygame.draw.line(screen, 0, (A3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A3.y * GRID_Y),
                         (A4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A4.y * GRID_Y))
        pygame.draw.line(screen, 0, (A4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A4.y * GRID_Y),
                         (A1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - A1.y * GRID_Y))

        # PENTAGON
        pygame.draw.line(screen, 0, (B1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B1.y * GRID_Y),
                         (B2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B2.y * GRID_Y))
        pygame.draw.line(screen, 0, (B2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B2.y * GRID_Y),
                         (B3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B3.y * GRID_Y))
        pygame.draw.line(screen, 0, (B3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B3.y * GRID_Y),
                         (B4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B4.y * GRID_Y))
        pygame.draw.line(screen, 0, (B4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B4.y * GRID_Y),
                         (B5.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B5.y * GRID_Y))
        pygame.draw.line(screen, 0, (B5.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B5.y * GRID_Y),
                         (B1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - B1.y * GRID_Y))

        # TRI1
        pygame.draw.line(screen, 0, (C1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - C1.y * GRID_Y),
                         (C2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - C2.y * GRID_Y))
        pygame.draw.line(screen, 0, (C2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - C2.y * GRID_Y),
                         (C3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - C3.y * GRID_Y))
        pygame.draw.line(screen, 0, (C3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - C3.y * GRID_Y),
                         (C1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - C1.y * GRID_Y))

        # RHOMBUS
        pygame.draw.line(screen, 0, (D1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D1.y * GRID_Y),
                         (D2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D2.y * GRID_Y))
        pygame.draw.line(screen, 0, (D2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D2.y * GRID_Y),
                         (D3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D3.y * GRID_Y))
        pygame.draw.line(screen, 0, (D3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D3.y * GRID_Y),
                         (D4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D4.y * GRID_Y))
        pygame.draw.line(screen, 0, (D4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D4.y * GRID_Y),
                         (D1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - D1.y * GRID_Y))

        # TRI1
        pygame.draw.line(screen, 0, (E1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - E1.y * GRID_Y),
                         (E2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - E2.y * GRID_Y))
        pygame.draw.line(screen, 0, (E2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - E2.y * GRID_Y),
                         (E3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - E3.y * GRID_Y))
        pygame.draw.line(screen, 0, (E3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - E3.y * GRID_Y),
                         (E1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - E1.y * GRID_Y))

        # RECTANGLE2
        pygame.draw.line(screen, 0, (F1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F1.y * GRID_Y),
                         (F2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F2.y * GRID_Y))
        pygame.draw.line(screen, 0, (F2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F2.y * GRID_Y),
                         (F3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F3.y * GRID_Y))
        pygame.draw.line(screen, 0, (F3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F3.y * GRID_Y),
                         (F4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F4.y * GRID_Y))
        pygame.draw.line(screen, 0, (F4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F4.y * GRID_Y),
                         (F1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - F1.y * GRID_Y))

        # POLYGON
        pygame.draw.line(screen, 0, (G1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G1.y * GRID_Y),
                         (G2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G2.y * GRID_Y))
        pygame.draw.line(screen, 0, (G2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G2.y * GRID_Y),
                         (G3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G3.y * GRID_Y))
        pygame.draw.line(screen, 0, (G3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G3.y * GRID_Y),
                         (G4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G4.y * GRID_Y))
        pygame.draw.line(screen, 0, (G4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G4.y * GRID_Y),
                         (G1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G1.y * GRID_Y))

        # HEXAGON
        pygame.draw.line(screen, 0, (H1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H1.y * GRID_Y),
                         (H2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H2.y * GRID_Y))
        pygame.draw.line(screen, 0, (H2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H2.y * GRID_Y),
                         (H3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H3.y * GRID_Y))
        pygame.draw.line(screen, 0, (H3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H3.y * GRID_Y),
                         (H4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H4.y * GRID_Y))
        pygame.draw.line(screen, 0, (H4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H4.y * GRID_Y),
                         (H5.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H5.y * GRID_Y))
        pygame.draw.line(screen, 0, (H5.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H5.y * GRID_Y),
                         (H6.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H6.y * GRID_Y))
        pygame.draw.line(screen, 0, (H6.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H6.y * GRID_Y),
                         (H1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - H1.y * GRID_Y))
        # /////////////////////////////////////////////////////////////////////////////////////////////////
        # END OF ORIGINAL
    else:
        # start
        S = Node(1, 3, "S")

        # goal
        G = Node(34, 19, "G")

        # NEW
        # /////////////////////////////////////////////////////////////////////////////////////////////////
        # rect = [(2,1), (2,6), (17,1), (17,6)]
        I1 = Node(2, 1, "I1")
        I2 = Node(2, 17, "I2")
        I3 = Node(9, 17, "I3")
        I4 = Node(9, 1, "I4")

        # tri1 = [(12,15), (10,8), (14,8)]
        J1 = Node(12, 18, "J1")
        J2 = Node(20, 11, "J3")
        J3 = Node(10, 11, "J2")

        # rhombus = [(14,19), (18,20), (14,13), (20,17)]
        K1 = Node(14, 20, "K1")
        K2 = Node(18, 27, "K2")
        K3 = Node(20, 22, "K3")
        K4 = Node(14, 18, "K4")

        # tri2 = [(18,10), (19,3), (23,6)]
        L1 = Node(17, 1, "L1")
        L2 = Node(22, 6, "L3")
        L3 = Node(22, 1, "L2")

        # rect2 = [(22,19), (28,19), (22,9), (28,9)]
        M1 = Node(22, 19, "M1")
        M2 = Node(31, 19, "M2")
        M3 = Node(31, 9, "M3")
        M4 = Node(22, 9, "M4")

        S.children = [I1, I2]
        I1.children = [I2, I4]
        I2.children = [I1, I3, J1, K1, K2]
        I3.children = [I2, I4, J1, J3, K1, K2]
        I4.children = [I1, I3, J2, J3, L1, L2, M4]
        J1.children = [J2, J3, I3, K1, K2, K4]
        J2.children = [J1, J3, K3, K4, L1, L2, M1, M4]
        J3.children = [J1, J2, I3, I4, L1, L2]
        K1.children = [K2, K4, I2, I3, J1]
        K2.children = [K1, K3, I2, I3, J1, M1, M2, G]
        K3.children = [K2, K4, J2, L2, M1, M4, G]
        K4.children = [K1, K3, J1, J2, M1, M4]
        L1.children = [L2, L3, I4, J2, J3, M4]
        L2.children = [L1, L3, I4, J2, J3, K3, M3, M4]
        L3.children = [L1, L2, M3]
        M1.children = [M2, M4, J2, K2, K3, K4]
        M2.children = [M1, M3, G]
        M3.children = [M2, M4, L2, L3, G]
        M4.children = [M1, M3, J2, J3, K3, K4, L1, L2]

        path = aStar(S, G, costBound)
        start = pygame.draw.circle(screen, (0, 255, 0), (S.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - S.y * GRID_Y), 7)

        # RECTANGLE1
        pygame.draw.line(screen, 0, (I1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - I1.y * GRID_Y),
                         (I2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - I2.y * GRID_Y))
        pygame.draw.line(screen, 0, (I2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - I2.y * GRID_Y),
                         (I3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - I3.y * GRID_Y))
        pygame.draw.line(screen, 0, (I3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - I3.y * GRID_Y),
                         (I4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - I4.y * GRID_Y))
        pygame.draw.line(screen, 0, (I4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - I4.y * GRID_Y),
                         (I1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - I1.y * GRID_Y))

        # TRI1
        pygame.draw.line(screen, 0, (J1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - J1.y * GRID_Y),
                         (J2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - J2.y * GRID_Y))
        pygame.draw.line(screen, 0, (J2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - J2.y * GRID_Y),
                         (J3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - J3.y * GRID_Y))
        pygame.draw.line(screen, 0, (J3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - J3.y * GRID_Y),
                         (J1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - J1.y * GRID_Y))

        # RHOMBUS
        pygame.draw.line(screen, 0, (K1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - K1.y * GRID_Y),
                         (K2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - K2.y * GRID_Y))
        pygame.draw.line(screen, 0, (K2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - K2.y * GRID_Y),
                         (K3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - K3.y * GRID_Y))
        pygame.draw.line(screen, 0, (K3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - K3.y * GRID_Y),
                         (K4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - K4.y * GRID_Y))
        pygame.draw.line(screen, 0, (K4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - K4.y * GRID_Y),
                         (K1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - K1.y * GRID_Y))

        # TRI2
        pygame.draw.line(screen, 0, (L1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - L1.y * GRID_Y),
                         (L2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - L2.y * GRID_Y))
        pygame.draw.line(screen, 0, (L2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - L2.y * GRID_Y),
                         (L3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - L3.y * GRID_Y))
        pygame.draw.line(screen, 0, (L3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - L3.y * GRID_Y),
                         (L1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - L1.y * GRID_Y))

        # RECTANGLE2
        pygame.draw.line(screen, 0, (M1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - M1.y * GRID_Y),
                         (M2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - M2.y * GRID_Y))
        pygame.draw.line(screen, 0, (M2.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - M2.y * GRID_Y),
                         (M3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - M3.y * GRID_Y))
        pygame.draw.line(screen, 0, (M3.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - M3.y * GRID_Y),
                         (M4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - M4.y * GRID_Y))
        pygame.draw.line(screen, 0, (M4.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - M4.y * GRID_Y),
                         (M1.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - M1.y * GRID_Y))
        # /////////////////////////////////////////////////////////////////////////////////////////////////
        # END OF NEW

    # GOAL POINT
    goal = pygame.draw.circle(screen, (255, 0, 0), (G.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - G.y * GRID_Y), 7)

    if path is not None:
        for p in path:
            if not p == S:
                print(p.name + ': ' + str(p.G))
                pygame.draw.line(screen, (255, 0, 0),
                                 (p.parent.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - p.parent.y * GRID_Y),
                                 (p.x * GRID_SIZE, (GRID_SIZE * GRID_Y) - p.y * GRID_Y))
                pygame.display.update()
                # time.sleep(.2)
    while True:
        temp = raw_input("Quit? Enter y or n: ")
        if temp == "y":
            pygame.quit()
            quit()
        else:
            break
