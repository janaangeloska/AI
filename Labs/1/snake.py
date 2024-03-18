from searching_framework.uninformed_search import *

class Snake(Problem):
    def __init__(self, initial, niza_crveni):
        super().__init__(initial)
        self.niza_crveni = niza_crveni
        self.grid_size = [10, 10]

    @staticmethod
    def check_valid(state, r_apples):
        snake_body = state[0]
        snake_head = snake_body[-1]
        snake_head_x, snake_head_y = snake_head[0], snake_head[1]

        if not (0 <= snake_head_x < 10 and 0 <= snake_head_y < 10):
            return False
        if snake_head in r_apples:
            return False
        if snake_head in snake_body[:-1]:
            return False
        return True

    def successor(self, state):
        successors = dict()

        snake_body = state[0]
        snake_head = snake_body[-1]
        sn_h_x, sn_h_y = snake_head[0], snake_head[1]

        green_apples = state[1]
        direction = state[2]

        if direction == 'dolu':
            # levo
            sn_h_new = (sn_h_x + 1, sn_h_y)
            sn_b_new = snake_body + (sn_h_new,)
            if self.check_valid((sn_b_new, green_apples, direction), self.niza_crveni):
                direction = 'desno'
                new_state1 = self.is_apple_eaten((sn_b_new, green_apples, direction))
                successors["SvrtiLevo"] = new_state1
            # desno
            sn_h_new = (sn_h_x - 1, sn_h_y)
            sn_b_new = snake_body + (sn_h_new,)
            if self.check_valid((sn_b_new, green_apples, direction), self.niza_crveni):
                direction = 'levo'
                new_state1 = self.is_apple_eaten((sn_b_new, green_apples, direction))
                successors["SvrtiDesno"] = new_state1
            # pravo
            sn_h_new = (sn_h_x, sn_h_y - 1)
            sn_b_new = snake_body + (sn_h_new,)
            if self.check_valid((sn_b_new, green_apples, direction), self.niza_crveni):
                direction = 'dolu'
                new_state1 = self.is_apple_eaten((sn_b_new, green_apples, direction))
                successors["ProdolzhiPravo"] = new_state1

        elif direction == 'gore':
            # levo
            sn_h_new = (sn_h_x - 1, sn_h_y)
            sn_b_new = snake_body + (sn_h_new,)
            if self.check_valid((sn_b_new, green_apples, direction), self.niza_crveni):
                direction = 'levo'
                new_state1 = self.is_apple_eaten((sn_b_new, green_apples, direction))
                successors["SvrtiLevo"] = new_state1
            # desno
            sn_h_new = (sn_h_x + 1, sn_h_y)
            sn_b_new = snake_body + (sn_h_new,)
            if self.check_valid((sn_b_new, green_apples, direction), self.niza_crveni):
                direction = 'desno'
                new_state1 = self.is_apple_eaten((sn_b_new, green_apples, direction))
                successors["SvrtiDesno"] = new_state1
            # pravo
            sn_h_new = (sn_h_x, sn_h_y + 1)
            sn_b_new = snake_body + (sn_h_new,)
            if self.check_valid((sn_b_new, green_apples, direction), self.niza_crveni):
                direction = 'gore'
                new_state1 = self.is_apple_eaten((sn_b_new, green_apples, direction))
                successors["ProdolzhiPravo"] = new_state1

        elif direction == 'levo':
            # levo
            sn_h_new = (sn_h_x, sn_h_y - 1)
            sn_b_new = snake_body + (sn_h_new,)
            if self.check_valid((sn_b_new, green_apples, direction), self.niza_crveni):
                direction = 'dolu'
                new_state1 = self.is_apple_eaten((sn_b_new, green_apples, direction))
                successors["SvrtiLevo"] = new_state1
            # desno
            sn_h_new = (sn_h_x, sn_h_y + 1)
            sn_b_new = snake_body + (sn_h_new,)
            if self.check_valid((sn_b_new, green_apples, direction), self.niza_crveni):
                direction = 'gore'
                new_state1 = self.is_apple_eaten((sn_b_new, green_apples, direction))
                successors["SvrtiDesno"] = new_state1
            # pravo
            sn_h_new = (sn_h_x - 1, sn_h_y)
            sn_b_new = snake_body + (sn_h_new,)
            if self.check_valid((sn_b_new, green_apples, direction), self.niza_crveni):
                direction = 'levo'
                new_state1 = self.is_apple_eaten((sn_b_new, green_apples, direction))
                successors["ProdolzhiPravo"] = new_state1

        #         desno

        else:
            # levo
            sn_h_new = (sn_h_x, sn_h_y + 1)
            sn_b_new = snake_body + (sn_h_new,)
            if self.check_valid((sn_b_new, green_apples, direction), self.niza_crveni):
                direction = 'gore'
                new_state1 = self.is_apple_eaten((sn_b_new, green_apples, direction))
                successors["SvrtiLevo"] = new_state1
            # desno
            sn_h_new = (sn_h_x, sn_h_y - 1)
            sn_b_new = snake_body + (sn_h_new,)
            if self.check_valid((sn_b_new, green_apples, direction), self.niza_crveni):
                direction = 'dolu'
                new_state1 = self.is_apple_eaten((sn_b_new, green_apples, direction))
                successors["SvrtiDesno"] = new_state1
            # pravo
            sn_h_new = (sn_h_x + 1, sn_h_y)
            sn_b_new = snake_body + (sn_h_new,)
            if self.check_valid((sn_b_new, green_apples, direction), self.niza_crveni):
                direction = 'desno'
                new_state1 = self.is_apple_eaten((sn_b_new, green_apples, direction))
                successors["ProdolzhiPravo"] = new_state1

        return successors

    def goal_test(self, state):
        return len(state[1]) == 0

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    @staticmethod
    def is_apple_eaten(state):
        snake_body = state[0]
        green_apples = state[1]
        snake_head = snake_body[-1]
        new_green_apples = tuple(apple for apple in green_apples if apple != snake_head)
        if len(new_green_apples) != len(green_apples):
            snake_body = list(snake_body)
            snake_body.append(snake_head)
            snake_body = tuple(snake_body)
        else:
            snake_body = list(snake_body)
            new_snake_body = snake_body[1:]
            # new_snake_body.append(snake_head)
            snake_body = tuple(new_snake_body)
        local_state = (snake_body, new_green_apples, state[2])
        return local_state


if __name__ == '__main__':

    n_zeleni = int(input())
    nizaZeleni = []
    for i in range(0, n_zeleni):
        inp = input().split(",")
        nizaZeleni.append(tuple([int(inp[0]), int(inp[1])]))

    n_crveni = int(input())
    nizaCrveni = []
    for i in range(0, n_crveni):
        inpc = input().split(",")
        nizaCrveni.append(tuple([int(inpc[0]), int(inpc[1])]))

    start_pos = ((0, 9), (0, 8), (0, 7))
    init = (start_pos, tuple(nizaZeleni), 'dolu')
    snake = Snake(init, tuple(nizaCrveni))

    bfs = breadth_first_graph_search(snake)

    if bfs is not None:
        print(bfs.solution())
