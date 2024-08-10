class Abstract_cmd:

    CMD_NAME = None

    def __init__(self):
        self.user_input = None
        pass

    def apply(self, user_input):
        self.user_input = user_input
        return self.action()

    def action(self):
        pass
