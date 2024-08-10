from models.abstract_cmd import Abstract_cmd


class Cmd_not_found(Abstract_cmd):
    CMD_NAME = 'NOT_FOUND'

    def __init__(self):
        super().__init__()

    def action(self):
        return """WTF, Doc? valid commands only pleazzzzze!
        - exit
        - close 
        - add <name> <phone> 
        - find <name>
        - edit <name> <phone>
        """
