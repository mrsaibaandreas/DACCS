class Filter:
    previous_pipe = ""
    actual_pipe = None
    state_types = {"B": "Busy",
                   "A": "Available"}
    state = state_types["A"] #by default is available
    def __init__(self, actual_pipe):
        self.actual_pipe = actual_pipe
        print(self.actual_pipe)

    def set_state(self, state):
        self.state = self.state_types[state]

    def get_state(self):
        return self.state
