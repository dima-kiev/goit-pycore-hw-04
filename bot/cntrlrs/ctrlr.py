from models.cmd_not_found import Cmd_not_found
from models.cmd_exit import Cmd_exit
from models.cmd_add import Cmd_add
from models.cmd_find import Cmd_find
from models.cmd_edit import Cmd_edit


class Controller:
    def __init__(self, storage):
        self.storage = storage
        self.__init_commands()


    def consume(self, cmd):
        return self.parse(cmd)

    def parse(self, user_inp: str):
        user_inp = user_inp.strip().lower()
        for cmd_name in self.commands:
            if user_inp.find(cmd_name) != -1:
                return self.commands[cmd_name].apply(user_inp)
        return self.commands.get(Cmd_not_found.CMD_NAME).apply(user_inp)

    def __init_commands(self):
        self.commands = dict()
        self.commands[Cmd_not_found.CMD_NAME] = Cmd_not_found()
        self.commands[Cmd_add.CMD_NAME] = Cmd_add(self.storage)
        self.commands[Cmd_find.CMD_NAME] = Cmd_find(self.storage)
        self.commands[Cmd_edit.CMD_NAME] = Cmd_edit(self.storage)
        self.commands[Cmd_exit.CMD_NAME] = Cmd_exit()
        self.commands["close"] = self.commands[Cmd_exit.CMD_NAME]
