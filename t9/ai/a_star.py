from copy import deepcopy
from typing import List, Optional


class Node:
    def calc_diff(self) -> int:
        """
        Calculates the difference between the given puzzle state and the goal
        :return: difference between the given puzzle state and the goal
        """
        h_val = 0

        # iterate through the matrix and calculate number of differences with goal state
        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] != self.goal[i][j] and self.state[i][j] != '_':
                    h_val += 1

        return h_val

    def __init__(self, state: List[List[str]], level: int, goal: List[List[str]]):
        """
        Initialize the node with the state, level of the node and the calculated f-score
        :param state: Matrix representing the given puzzle state
        :param level: level of the node
        :param goal: Matrix representing the goal puzzle state
        """
        self.state = state
        self.level = level
        self.goal = goal
        self.f_score = self.calc_diff() + level

    def __str__(self):
        """
        :return: string representation of the puzzle state this node represents
        """
        return "\n".join([" ".join(row) for row in self.state])

    def _find_blank_space(self) -> (int, int):
        """
        Specifically used to find the position of the blank space represented by `_`
        :return: x and y position of blank space
        """
        for x in range(0, len(self.state)):
            for y in range(0, len(self.state)):
                if self.state[x][y] == "_":
                    return x, y

    def _shuffle(self, puzzle: List[List[str]], x1: int, y1: int, x2: int, y2: int) -> Optional[List[List[str]]]:
        """
        Move the blank space in the given direction and if the position value are out of limits the return None
        :param puzzle: the puzzle matrix
        :param x1: initial x position
        :param y1: initial y position
        :param x2: destination x position
        :param y2: destination y position
        :return: Updated matrix,
        """
        if 0 <= x2 < len(self.state) and 0 <= y2 < len(self.state):
            temp_puz = deepcopy(puzzle)
            temp_puz[x2][y2], temp_puz[x1][y1] = temp_puz[x1][y1], temp_puz[x2][y2]
            return temp_puz
        else:
            return None

    def generate_children(self) -> List:
        """
        Generate child nodes from the given node by moving the blank space either in the four directions
        :return: List of child nodes
        """
        # get current position of blank space
        x, y = self._find_blank_space()

        # make list of all positions to shift that blank place into
        positions = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]

        # generate child nodes and append them to list
        children = []
        for i in positions:
            child = self._shuffle(self.state, x, y, i[0], i[1])
            if child is not None:
                children.append(Node(child, self.level + 1, self.goal))

        return children


class Puzzle:
    def __init__(self, initial: List[List[str]], goal: List[List[str]]):
        """
        Initialize the puzzle size by the specified size,initial and closed lists to empty
        :param initial: Matrix representing the initial state
        :param goal: matrix representing the goal state
        """
        self.initial = initial
        self.goal = goal

    def solve(self) -> List[Node]:
        """
        function to actually solve the puzzle using A* algorithm
        :return: List of nodes that comprise of the solution
        """
        opened = []  # list of opened nodes
        solution = []  # list of nodes in solution

        # Put the start node in the opened list
        node = Node(self.initial, 0, self.goal)
        opened.append(node)

        # loop until difference between state of current node state and goal state is not 0
        while node.calc_diff() != 0:
            # add node to solution
            solution.append(node)

            # generate child nodes and append them to opened list
            for child in node.generate_children():
                opened.append(child)

            del opened[0]  # close current node
            opened.sort(key=lambda x: x.f_score)  # sort the opened list based on f value
            node = opened[0]  # set node to next opened node with lowest f-score

        # final node is also part of the solution
        solution.append(node)

        return solution


if __name__ == "__main__":
    # Take input of initial and goal state
    print("Enter the initial state matrix :")
    initial = [input().split(" ") for _ in range(3)]
    print("\nEnter the goal state matrix :")
    goal = [input().split(" ") for _ in range(3)]

    # make puzzle object and solve it
    puzzle = Puzzle(initial, goal)
    solution = puzzle.solve()

    # print solution
    for i, node in enumerate(solution):
        print(f"\nStep {i}", node, sep="\n")
