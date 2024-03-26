from searching_framework import *

# dzidovi na slucajni poz, ne moze da se preskoknuvaat
# zabraneta oz obstacles, zabrenta poz nadvor od matrica
# 4 nasoki:
"""
gore 1
dolu 1
levo 1
desno 2
desno 3
"""


class Maze(Problem):

    def __init__(self, initial, prechki, house, goal=None):
        super().__init__(initial, goal)
        self.init = initial
        self.prechki = prechki
        self.house = house

    @staticmethod
    def check_valid(manche):
        prechki = obstacles

        if manche in prechki:
            return False
        if not (0 <= manche[0] < n and 0 <= manche[1] < n):
            return False
        return True

    def successor(self, state):
        successors = dict()

        coveche_x, coveche_y = state

        # gore 1
        new_pos = (coveche_x, coveche_y + 1)
        if self.check_valid(new_pos):
            successors["Gore"] = new_pos
        # dolu 1
        new_pos = (coveche_x, coveche_y - 1)
        if self.check_valid(new_pos):
            successors["Dolu"] = new_pos
        # levo 1
        new_pos = (coveche_x - 1, coveche_y)
        if self.check_valid(new_pos):
            successors["Levo"] = new_pos
        # desno 2
        new_pos = (coveche_x + 2, coveche_y)
        if self.check_valid(new_pos) and self.check_valid((coveche_x + 1, coveche_y)):
            successors["Desno 2"] = new_pos
        # desno 3
        new_pos = (coveche_x + 3, coveche_y)
        if (self.check_valid(new_pos) and self.check_valid((coveche_x + 1, coveche_y)) and
                self.check_valid((coveche_x + 2, coveche_y))):
            successors["Desno 3"] = new_pos

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.house

    def h(self, node):
        x = node.state[0]
        y = node.state[1]
        x1 = self.house[0]
        y2 = self.house[1]
        return abs(x - x1) / 3 + abs(y - y2)


if __name__ == '__main__':
    # golemina na lavirint
    n = int(input())
    # broj na dzidovi
    m = int(input())
    # lista torki od obstacles
    lista = []
    for i in range(0, m):
        tup = input().split(",")
        lista.append(tuple([int(tup[0]), int(tup[1])]))

    man = input()
    kukjicka = input()

    man = man.split(",")
    kukjicka = kukjicka.split(",")

    man = tuple([int(man[0]), int(man[1])])
    kukjicka = tuple([int(kukjicka[0]), int(kukjicka[1])])

    init = man
    obstacles = lista
    game = Maze(init, obstacles, kukjicka)
    astar = astar_search(game)

    if astar is not None:
        print(astar.solution())
        


