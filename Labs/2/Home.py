from searching_framework import *

# class Game:

# static:
# grid_size

# dozvoleni nasoki:
# горе, горе-десно и горе-лево VKLUCENI 0, 1 ili 2 skoka

# podvizhni:
# kukja, covece

# nevaldini states:
"""
  da zastane na pole sho ne e zeleno aka vo ovie grupava allowed
  da izleze od tablata
  edinstveno pole na koe moze da zastane coveceto od posledniot red e poleto na kukjickata drugite se zabraneti  
"""


class Game(Problem):

    def __init__(self, initial, allowed_pos, goal=None):
        super().__init__(initial, goal)
        self.init = initial
        self.allowed_pos = allowed_pos
        self.grid_size = [5, 9]

    @staticmethod
    def check_valid(state):
        man_pos = state[1]
        man_x = man_pos[0]
        man_y = man_pos[1]

        house_pos = state[0]

        if not (0 <= man_x < 5 and 0 <= man_y < 9):
            return False

        if man_pos == house_pos:
            return True

        if man_pos not in allowed:
            return False

        return True

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == state[1]

    def successor(self, state):
        successors = dict()

        house_allowed = [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8)]
        house_pos = state[0]
        house_x = house_pos[0]
        house_y = house_pos[1]

        man_pos = state[1]
        man_x = man_pos[0]
        man_y = man_pos[1]

        house_dir = state[2]

        # Stoj

        if house_dir == 'desno':
            new_house_pos = (house_x + 1, house_y)
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, man_pos, house_dir)
                if self.check_valid(new_state):
                    successors["Stoj"] = new_state
            else:
                new_house_pos = (house_x - 1, house_y)
                new_house_dir = "levo"
                if new_house_pos in house_allowed:
                    new_state = (new_house_pos, man_pos, new_house_dir)
                    if self.check_valid(new_state):
                        successors["Stoj"] = new_state
        else:
            new_house_pos = (house_x - 1, house_y)
            new_house_dir = "levo"
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, man_pos, new_house_dir)
                if self.check_valid(new_state):
                    successors["Stoj"] = new_state
            else:
                new_house_pos = (house_x + 1, house_y)
                new_house_dir = "desno"
                if new_house_pos in house_allowed:
                    new_state = (new_house_pos, man_pos, new_house_dir)
                    if self.check_valid(new_state):
                        successors["Stoj"] = new_state

        # Gore 1
        new_man_pos = (man_x, man_y + 1)
        if house_dir == 'desno':
            new_house_pos = (house_x + 1, house_y)
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, new_man_pos, house_dir)
                if self.check_valid(new_state):
                    successors["Gore 1"] = new_state
            else:
                new_house_pos = (house_x - 1, house_y)
                new_house_dir = "levo"
                if new_house_pos in house_allowed:
                    new_state = (new_house_pos, new_man_pos, new_house_dir)
                    if self.check_valid(new_state):
                        successors["Gore 1"] = new_state
        else:
            new_house_pos = (house_x - 1, house_y)
            new_house_dir = "levo"
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, new_man_pos, new_house_dir)
                if self.check_valid(new_state):
                    successors["Gore 1"] = new_state
            else:
                new_house_pos = (house_x + 1, house_y)
                new_house_dir = "desno"
                if new_house_pos in house_allowed:
                    new_state = (new_house_pos, new_man_pos, new_house_dir)
                    if self.check_valid(new_state):
                        successors["Gore 1"] = new_state

        # Gore-desno 1

        new_man_pos = (man_x + 1, man_y + 1)
        if house_dir == 'desno':
            new_house_pos = (house_x + 1, house_y)
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, new_man_pos, house_dir)
                if self.check_valid(new_state):
                    successors["Gore-desno 1"] = new_state
            else:
                new_house_pos = (house_x - 1, house_y)
                new_house_dir = "levo"
                new_state = (new_house_pos, new_man_pos, new_house_dir)
                if self.check_valid(new_state):
                    successors["Gore-desno 1"] = new_state
        else:
            new_house_pos = (house_x - 1, house_y)
            new_house_dir = "levo"
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, new_man_pos, new_house_dir)
                if self.check_valid(new_state):
                    successors["Gore-desno 1"] = new_state
            else:
                new_house_pos = (house_x + 1, house_y)
                new_house_dir = "desno"
                new_state = (new_house_pos, new_man_pos, new_house_dir)
                if self.check_valid(new_state):
                    successors["Gore-desno 1"] = new_state

        # Gore-levo 1

        new_man_pos = (man_x - 1, man_y + 1)
        if house_dir == 'desno':
            new_house_pos = (house_x + 1, house_y)
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, new_man_pos, house_dir)
                if self.check_valid(new_state):
                    successors["Gore-levo 1"] = new_state
            else:
                new_house_pos = (house_x - 1, house_y)
                new_house_dir = "levo"
                if new_house_pos in house_allowed:
                    new_state = (new_house_pos, new_man_pos, new_house_dir)
                    if self.check_valid(new_state):
                        successors["Gore-levo 1"] = new_state
        else:
            new_house_pos = (house_x - 1, house_y)
            new_house_dir = "levo"
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, new_man_pos, new_house_dir)
                if self.check_valid(new_state):
                    successors["Gore-levo 1"] = new_state
            else:
                new_house_pos = (house_x + 1, house_y)
                new_house_dir = "desno"
                if new_house_pos in house_allowed:
                    new_state = (new_house_pos, new_man_pos, new_house_dir)
                    if self.check_valid(new_state):
                        successors["Gore-levo 1"] = new_state

        # Gore 2

        new_man_pos = (man_x, man_y + 2)
        if house_dir == 'desno':
            new_house_pos = (house_x + 1, house_y)
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, new_man_pos, house_dir)
                if self.check_valid(new_state):
                    successors["Gore 2"] = new_state
            else:
                new_house_pos = (house_x - 1, house_y)
                new_house_dir = "levo"
                if new_house_pos in house_allowed:
                    new_state = (new_house_pos, new_man_pos, new_house_dir)
                    if self.check_valid(new_state):
                        successors["Gore 2"] = new_state
        else:
            new_house_pos = (house_x - 1, house_y)
            new_house_dir = "levo"
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, new_man_pos, new_house_dir)
                if self.check_valid(new_state):
                    successors["Gore 2"] = new_state
            else:
                new_house_pos = (house_x + 1, house_y)
                new_house_dir = "desno"
                if new_house_pos in house_allowed:
                    new_state = (new_house_pos, new_man_pos, new_house_dir)
                    if self.check_valid(new_state):
                        successors["Gore 2"] = new_state

        # Gore-desno 2

        new_man_pos = (man_x + 2, man_y + 2)
        if house_dir == 'desno':
            new_house_pos = (house_x + 1, house_y)
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, new_man_pos, house_dir)
                if self.check_valid(new_state):
                    successors["Gore-desno 2"] = new_state
            else:
                new_house_pos = (house_x - 1, house_y)
                new_house_dir = "levo"
                if new_house_pos in house_allowed:
                    new_state = (new_house_pos, new_man_pos, new_house_dir)
                    if self.check_valid(new_state):
                        successors["Gore-desno 2"] = new_state
        else:
            new_house_pos = (house_x - 1, house_y)
            new_house_dir = "levo"
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, new_man_pos, new_house_dir)
                if self.check_valid(new_state):
                    successors["Gore-desno 2"] = new_state
            else:
                new_house_pos = (house_x + 1, house_y)
                new_house_dir = "desno"
                if new_house_pos in house_allowed:
                    new_state = (new_house_pos, new_man_pos, new_house_dir)
                    if self.check_valid(new_state):
                        successors["Gore-desno 2"] = new_state

        # Gore-levo 2
        new_man_pos = (man_x - 2, man_y + 2)
        if house_dir == 'desno':
            new_house_pos = (house_x + 1, house_y)
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, new_man_pos, house_dir)
                if self.check_valid(new_state):
                    successors["Gore-levo 2"] = new_state
            else:
                new_house_pos = (house_x - 1, house_y)
                new_house_dir = "levo"
                if new_house_pos in house_allowed:
                    new_state = (new_house_pos, new_man_pos, new_house_dir)
                    if self.check_valid(new_state):
                        successors["Gore-levo 2"] = new_state
        else:
            new_house_pos = (house_x - 1, house_y)
            new_house_dir = "levo"
            if new_house_pos in house_allowed:
                new_state = (new_house_pos, new_man_pos, new_house_dir)
                if self.check_valid(new_state):
                    successors["Gore-levo 2"] = new_state
            else:
                new_house_pos = (house_x + 1, house_y)
                new_house_dir = "desno"
                if new_house_pos in house_allowed:
                    new_state = (new_house_pos, new_man_pos, new_house_dir)
                    if self.check_valid(new_state):
                        successors["Gore-levo 2"] = new_state

        return successors

    def h(self, node):
        man_pos = node.state[1]
        man_x = man_pos[0]
        man_y = man_pos[1]

        house_pos = node.state[0]
        house_x = house_pos[0]
        house_y = house_pos[1]

        # return (man_x - house_x) + (man_y - house_y)

        return (man_y - house_y) / 2


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4),
               (2, 4), (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    covece = input()
    kukjicka = input()

    covece = covece.split(",")
    kukjicka = kukjicka.split(",")

    covece = tuple([int(covece[0]), int(covece[1])])
    kukjicka = tuple([int(kukjicka[0]), int(kukjicka[1])])

    pocetna_nasoka = input()

    init = (kukjicka, covece, pocetna_nasoka)
    game = Game(init, allowed)

    astar = astar_search(game)

    if astar is not None:
        print(astar.solution())
