from models.abstract_cmd import Abstract_cmd


class Cmd_exit(Abstract_cmd):
    CMD_NAME = 'exit'

    def __init__(self):
        super().__init__()

    def action(self):
        exit(1)
