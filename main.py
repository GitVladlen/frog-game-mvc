from model import Model
from view import View
from controller import Controller


def main():
    print " = Frog Game = "
    model = Model()

    controller = Controller(model)
    view = View(model, controller)

    pass

if __name__ == "__main__":
    main()
    pass

