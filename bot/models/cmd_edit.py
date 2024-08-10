from models.abstract_cmd import Abstract_cmd


class Cmd_edit(Abstract_cmd):
    CMD_NAME = 'edit'

    def __init__(self, storage):
        super().__init__()
        self.storage = storage

    def action(self):
        try:
            edit_cmd, name, new_phone = self.user_input.split(" ")
            old_phone = self.storage.get(name)
            if old_phone is None:
                self.storage.put(name, new_phone)
                return f"not found for {name}. created new record for {name} -> {new_phone}"
            self.storage.put(name, new_phone)
            return f"found {old_phone} for {name}. replaced to new record for {name} -> {new_phone}"
        except ValueError:
            return "Something went wrong. Should be edit NAME NEW_PHONE, but was: " + self.user_input
