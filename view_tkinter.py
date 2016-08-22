"""
    This is VIEW
"""
from Tkinter import *
from Functor import Functor


class View(Frame):
    def __init__( self, model, controller, parent = None ):
        Frame.__init__( self, parent )
        self.model = model
        self.controller = controller

        self.symbols = {
            self.model.EMPTY: "*",
            self.model.FROG_LEFT: "L",
            self.model.FROG_RIGHT: "R"
            }

        self.buttons = []

        self._createButtons()

        self.model.EventGameOver.addObserver(self._onEventGameOver)
        pass

    def _update(self, index):
        # print "update", index, self.model.stones[index]

        self.controller.turn(index)
        self._update_buttons()

        self.model.isGameOver()
        pass

    def _reset(self):
        self.controller.restart()
        self._update_buttons()
        pass

    def _createButtons(self):
        for index, stone in enumerate(self.model.stones):
            btn = Button(self, text=self.symbols[stone], command=Functor(self._update, index))
            btn.grid(row=0, column=index)
            self.buttons.append(btn)
            pass

        btn = Button(self, text="Reset", command=self._reset)
        btn.grid(row=0, column=len(self.model.stones))
        pass

    def _update_buttons(self):
        for btn, stone in zip(self.buttons, self.model.stones):
            btn.config(text=self.symbols[stone])
            pass
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

    def _onEventGameOver(self):
        # self._printStones()
        print " = Game Over ="
        pass

    def __str__(self):
        return "[view]"
        pass
    pass
