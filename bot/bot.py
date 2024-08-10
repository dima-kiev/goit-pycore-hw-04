from srvces.storage import Storage
from views.view import View
from cntrlrs.ctrlr import Controller


def main():
    storage = Storage()
    controller = Controller(storage)
    view = View(controller)
    view.start()


if __name__ == '__main__':
    main()