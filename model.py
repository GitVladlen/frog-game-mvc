"""
    This is MODEL
"""
from Event import Event


class Model(object):
    EMPTY = 0
    FROG_LEFT = 1
    FROG_RIGHT = 2

    def __init__(self):
        super(Model, self).__init__()
        self.stones = None

        self.EventMakeTurn = Event("MakeTurn")
        self.EventGameOver = Event("GameOver")
        pass

    def run(self):
        self.resetGame()

        while self.isGameOver() is False:
            self.EventMakeTurn()
            pass

        pass

    def resetGame(self):
        self.stones = [
            self.FROG_LEFT,
            self.FROG_LEFT,
            self.FROG_LEFT,
            self.EMPTY,
            self.FROG_RIGHT,
            self.FROG_RIGHT,
            self.FROG_RIGHT
            ]
        pass

    def isValidPosition(self, position):
        if position in range(len(self.stones)):
            return True
            pass

        return False
        pass

    def _tryJumpFromTo(self, from_position, to_position):
        if self.stones[from_position] is self.EMPTY:
            return False
            pass

        if self.isValidPosition(to_position) is True and self.stones[to_position] is self.EMPTY:
            frog = self.stones[from_position]
            self.stones[from_position] = self.EMPTY
            self.stones[to_position] = frog

            return True
            pass

        return False
        pass

    def turn(self, position):
        if self.isValidPosition(position) is False:
            # print "[error] position {} is not valid".format(position)
            return
            pass

        if self.stones[position] is self.EMPTY:
            # print "[error] stone on position {} is empty".format(position)
            return
            pass

        if self.stones[position] is self.FROG_RIGHT:
            first_position = position - 1
            second_position = position - 2
            pass

        if self.stones[position] is self.FROG_LEFT:
            first_position = position + 1
            second_position = position + 2
            pass

        if self._tryJumpFromTo(position, first_position) is True:
            # print "[log] jump frog {} from {} to {}".format(self.stones[position], position, first_position)
            return
            pass

        if self._tryJumpFromTo(position, second_position) is True:
            # print "[log] jump frog {} from {} to {}".format(self.stones[position], position, second_position)
            return
            pass

        # print "[error] something goes wrong..."
        pass

    def isGameOver(self):
        win_stones = [
            self.FROG_RIGHT,
            self.FROG_RIGHT,
            self.FROG_RIGHT,
            self.EMPTY,
            self.FROG_LEFT,
            self.FROG_LEFT,
            self.FROG_LEFT,
            ]

        if self.stones == win_stones:
            self.EventGameOver()
            return True
            pass

        return False
        pass

    def __str__(self):
        return "[model]" + str(self.grid)
        pass
    pass
