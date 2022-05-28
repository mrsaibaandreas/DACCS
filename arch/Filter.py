class Filter:
    previous_pipe = None
    actual_pipe = None
    state = None

    def get_state(self):
        return self.state

