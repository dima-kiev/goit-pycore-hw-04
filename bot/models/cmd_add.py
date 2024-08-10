from models.abstract_cmd import Abstract_cmd


class Cmd_add(Abstract_cmd):
    CMD_NAME = 'add'

    def __init__(self, storage):
        super().__init__()
        self.storage = storage

    def action(self):
        try:
            add_cmd, name, phone = self.user_input.split(" ")
            self.storage.put(name, phone)
            return f"entry {name} -> {phone} was successfully added"
        except ValueError:
            return "Something went wrong. Should be add NAME PHONE, but was: " + self.user_input
