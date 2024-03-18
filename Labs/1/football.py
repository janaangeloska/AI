from searching_framework.uninformed_search import *

class Football(Problem):
    def __init__(self, initial, stat_opponents, goal=None):
        super().__init__(initial, goal)
        self.stat_opponents = stat_opponents
        self.goal_pos = [(7, 2), (7, 3)]

    def goal_test(self, state):
        return state[1] in self.goal_pos

    @staticmethod
    def check_valid(state):
        player_pos = state[0]
        ball_pos = state[1]

        ball_x = ball_pos[0]
        ball_y = ball_pos[1]

        player_x = player_pos[0]
        player_y = player_pos[1]

        opponents_neighbors_pos = [(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (4, 4), (4, 5),
                                   (5, 3), (5, 4), (5, 5), (6, 3), (6, 4), (6, 5)]

        opponents_pos = [(3, 3), (5, 4)]
        if not (0 <= ball_x < 8 and 0 <= ball_y < 6):
            return False

        if not (0 <= player_x < 8 and 0 <= player_y < 6):
            return False

        if (ball_x, ball_y) in opponents_neighbors_pos:
            return False

        if (player_x, player_y) in opponents_pos:
            return False
        return True

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def successor(self, state):
        successors = dict()

        player_posi = state[0]
        player_x = player_posi[0]
        player_y = player_posi[1]

        ball_posi = state[1]
        ball_x = ball_posi[0]
        ball_y = ball_posi[1]

        new_player_posi = (player_x, player_y + 1)
        if new_player_posi != ball_posi and self.check_valid((new_player_posi, ball_posi)):
            successors['Pomesti coveche gore'] = (new_player_posi, ball_posi)

        new_player_posi = (player_x, player_y - 1)
        if new_player_posi != ball_posi and self.check_valid((new_player_posi, ball_posi)):
            successors['Pomesti coveche dolu'] = (new_player_posi, ball_posi)

        new_player_posi = (player_x + 1, player_y)
        if new_player_posi != ball_posi and self.check_valid((new_player_posi, ball_posi)):
            successors['Pomesti coveche desno'] = (new_player_posi, ball_posi)

        new_player_posi = (player_x + 1, player_y + 1)
        if new_player_posi != ball_posi and self.check_valid((new_player_posi, ball_posi)):
            successors['Pomesti coveche gore-desno'] = (new_player_posi, ball_posi)

        new_player_posi = (player_x + 1, player_y - 1)
        if new_player_posi != ball_posi and self.check_valid((new_player_posi, ball_posi)):
            successors['Pomesti coveche dolu-desno'] = (new_player_posi, ball_posi)

        new_player_posi = (player_x, player_y + 1)
        new_ball_posi = (ball_x, ball_y + 1)
        if new_player_posi == ball_posi and self.check_valid((new_player_posi, new_ball_posi)):
            successors['Turni topka gore'] = (new_player_posi, new_ball_posi)

        new_player_posi = (player_x, player_y - 1)
        new_ball_posi = (ball_x, ball_y - 1)
        if new_player_posi == ball_posi and self.check_valid((new_player_posi, new_ball_posi)):
            successors['Turni topka dolu'] = (new_player_posi, new_ball_posi)

        new_player_posi = (player_x + 1, player_y)
        new_ball_posi = (ball_x + 1, ball_y)
        if new_player_posi == ball_posi and self.check_valid((new_player_posi, new_ball_posi)):
            successors['Turni topka desno'] = (new_player_posi, new_ball_posi)

        new_player_posi = (player_x + 1, player_y + 1)
        new_ball_posi = (ball_x + 1, ball_y + 1)
        if new_player_posi == ball_posi and self.check_valid((new_player_posi, new_ball_posi)):
            successors['Turni topka gore-desno'] = (new_player_posi, new_ball_posi)

        new_player_posi = (player_x + 1, player_y - 1)
        new_ball_posi = (ball_x + 1, ball_y - 1)
        if new_player_posi == ball_posi and self.check_valid((new_player_posi, new_ball_posi)):
            successors['Turni topka dolu-desno'] = (new_player_posi, new_ball_posi)

        return successors


if __name__ == '__main__':
    man_pos_init = input().split(",")
    man_pos_x = int(man_pos_init[0])
    man_pos_y = int(man_pos_init[1])
    man_pos_init = tuple((man_pos_x, man_pos_y))

    ball_pos_init = input().split(",")
    ball_pos_x = int(ball_pos_init[0])
    ball_pos_y = int(ball_pos_init[1])
    ball_pos_init = tuple((ball_pos_x, ball_pos_y))

    opponents_static = [(3, 3), (5, 4)]

    football = Football((man_pos_init, ball_pos_init), opponents_static)

    # print(breadth_first_graph_search(football).solution())

    bfs = breadth_first_graph_search(football)

    if bfs is not None:
        print(bfs.solution())
