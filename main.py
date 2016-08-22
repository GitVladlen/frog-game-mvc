from model import Model
# from view import View
from view_tkinter import View
from controller import Controller


def main():
    print " = Frog Game = "
    model = Model()
    model.resetGame()  # tkinter

    controller = Controller(model)
    view = View(model, controller)

    view.pack()  # tkinter
    view.mainloop()  # tkinter

    # model.run()
    pass

if __name__ == "__main__":
    main()
    pass

