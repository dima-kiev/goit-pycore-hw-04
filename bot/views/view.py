class View:

    def __init__(self, controller):
        self.controller = controller

    def start(self):
        while True:
            prob_command = input("wats`up, Doc? ")
            print(self.controller.consume(prob_command))
