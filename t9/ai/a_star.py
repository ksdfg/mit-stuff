from copy import deepcopy
from typing import List, Optional


class Node:
    def __init__(self, state: List[List[str]], level: int, goal: List[List[str]], parent=None):
        """
        Initialize the node with the state, level of the node and the calculated f-score
        :param state: Matrix representing the given puzzle state
        :param level: level of the node
        :param goal: Matrix representing the goal puzzle state
        :param parent: Parent node
        """
        self.state = state
        self.level = level
        self.goal = goal
        self.parent = parent

        self.h_value = 0
        # iterate through the matrix and calculate number of differences with goal state
        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] != goal[i][j] and state[i][j] != '_':
                    self.h_value += 1

        self.f_score = self.h_value + level

    def __str__(self):
        """
        :return: string representation of the puzzle state this node represents
        """
        return "\n".join([" ".join(row) for row in self.state])

    def __eq__(self, other):
        """
        Specify how equality of two nodes is to be  checked
        :param other: The object we're comparing it to
        :return: True if they're equal, else false
        """
        return self.state == other.state

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
                children.append(Node(child, self.level + 1, self.goal, self))

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

        # Put the start node in the opened list
        node = Node(self.initial, 0, self.goal)
        opened.append(node)

        # loop until difference between state of current node state and goal state is not 0
        while node.h_value != 0:
            # if a node has depth greater than 31, puzzle is unsolvable
            if node.level > 31:
                return []

            # generate child nodes and append them to opened list
            for child in node.generate_children():
                if child not in opened:
                    opened.append(child)

            del opened[0]  # close current node
            opened.sort(key=lambda x: x.f_score)  # sort the opened list based on f value
            node = opened[0]  # set node to next opened node with lowest f-score

        # get path from final node to initial node
        solution = []
        while node is not None:
            solution.append(node)
            node = node.parent
        solution.sort(key=lambda x: x.level)

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
    if solution:
        for i, node in enumerate(solution):
            print(f"\nStep {i}", node, sep="\n")
    else:
        print("Cannot be solved")
