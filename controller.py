"""
    This is CONTROLLER
"""


class Controller(object):
    def __init__(self, model):
        self.model = model
        pass

    def restart(self):
        self.model.resetGame()
        pass

    def turn(self, position):
        self.model.turn(position)
        pass

    def __str__(self):
        return "[controller]"
        pass
    pass
