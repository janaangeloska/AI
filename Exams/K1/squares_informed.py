# vidi klasi od sqares.py

class Squares(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def h(self, node):
        total_distance = 0
        for i in range(5):
            current_square = node.state[i]
            goal_square = self.goal[i]
            distance = abs(current_square[0] - goal_square[0]) + abs(current_square[1] - goal_square[1])
            total_distance += distance
        return total_distance
