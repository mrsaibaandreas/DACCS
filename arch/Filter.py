class Filter:
    previous_pipe = ""
    actual_pipe = None

    def __init__(self, actual_pipe):
        self.actual_pipe = actual_pipe
        print(self.actual_pipe)

