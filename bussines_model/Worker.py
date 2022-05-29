class Worker:
    __name = None
    __id = None
    __job = None
    state_types = {"B": "Busy",
                   "A": "Available"}
    state = state_types["A"]  # by default is available

    def __init__(self, name, id, job):
        self.__name = name
        self.__id = id
        self.__job = job

    def get_job(self):
        return self.__job

    def get_name(self):
        return self.__name

    def set_state(self, state):
        self.state = self.state_types[state]

    def get_state(self):
        return self.state
