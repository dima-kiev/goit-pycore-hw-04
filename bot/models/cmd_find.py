from models.abstract_cmd import Abstract_cmd


class Cmd_find(Abstract_cmd):
    CMD_NAME = 'find'

    def __init__(self, storage):
        super().__init__()
        self.storage = storage

    def action(self):
        try:
            find_cmd, name = self.user_input.split(" ")
            phone = self.storage.get(name)
            if phone is None:
                return f"not found record for {name}"
            return f"entry found {name} -> {phone}"
        except ValueError:
            return "Something went wrong. Should be find NAME, but was: " + self.user_input
