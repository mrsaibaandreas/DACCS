class Pipe:
    # we treat pipe like C syscall process communication pipes
    __read = False
    __write = False
    __pipe_data = None

    empty = True

    def read_pipe(self):
        if self.__read is True:
            print("Sending data")
            return self.__pipe_data
        else:
            print("Pipe cannot be used for reading")
            return -1

    def write_pipe(self, information):
        if self.__write is True:
            self.__empty = False
            self.__pipe_data = information
        else:
            print("Pipe cannot be used for writing")
            return -1

    # This method is manipulated by the programmer
    # The input should can be only R or W or O or C
    # Because we use a dictionaries with these two values
    def set_pipe_state(self, descriptor, state):
        if descriptor == "O":
            if state == "R":
                self.__read = True
            elif state == "W":
                self.__write = True
        elif descriptor == "C":
            if state == "R":
                self.__read = False
            elif state == "W":
                self.__write = False


def initialize_pipe(obj):
    obj = Pipe
    return obj


class Pipeline:
    pipe_list = []
    filter_list = []

    def __init__(self):
        self.pipe_list = [initialize_pipe(x) for x in range(len(self.filter_list))]

