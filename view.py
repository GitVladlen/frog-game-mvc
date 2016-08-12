"""
    This is VIEW
"""


class View(object):
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller

        self.symbols = {
            self.model.EMPTY: "*",
            self.model.FROG_LEFT: "L",
            self.model.FROG_RIGHT: "R"
            }

        self.model.EventMakeTurn.addObserver(self._onEventMakeTurn)
        self.model.EventGameOver.addObserver(self._onEventGameOver)
        pass

    def _printStones(self):
        for stone in self.model.stones:
            print self.symbols[stone],
            pass
        print
        for index in range(len(self.model.stones)):
            print index,
            pass
        print
        pass

    def _onEventMakeTurn(self):
        self._printStones()

        while True:
            try:
                position = input()
                pass
            except Exception:
                continue
                pass

            if position == 9:
                self.controller.restart()
                pass
            else:
                self.controller.turn(position)
                pass
            break
            pass
        pass

    def _onEventGameOver(self):
        self._printStones()
        print " = Game Over ="
        pass

    def __str__(self):
        return "[view]"
        pass
    pass
