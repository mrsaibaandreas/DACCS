from time import sleep


class Pipe:
    # we treat pipe like C syscall process communication pipes
    __read = False
    __write = False
    __pipe_data = ""
    empty = True


    def __init__(self):
        print("Initialized")

    def read_pipe(self):
        if self.__read is True:
            print("Sending data")
            return self.__pipe_data
        else:
            print("Pipe cannot be used for reading")
            return -1

    def write_pipe(self, information):
        if self.__write is True:
            self.empty = False
            self.__pipe_data = information
        else:
            print("Pipe cannot be used for writing")
            return -1

    # This method is manipulated by the programmer
    # The input should can be only R or W or O or C
    # Because we use a dictionaries with these two values
    def set_state(self, descriptor, state):
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
    obj = Pipe()
    return obj


class Pipeline:
    pipe_list = []
    filter_list = []
    pipeline_position = 0
    data = None

    __pipe_status = {"B": "Busy",
                   "A": "Available",
                   "PR": "Product ready"}
    __pipe_state = __pipe_status["A"]  # by default available
    def __init__(self):
        print("Pipeline init")

    def set_pipel_state(self, state):
        self.__pipe_state = self.__pipe_status[state]


    def set_pipelist(self):
        self.pipe_list = [initialize_pipe(x) for x in range(len(self.filter_list))]

    def write_in_pipe(self):
        #check if worker is available
        if self.filter_list[self.pipeline_position].get_state() == "Busy":
            sleep(5)
            self.filter_list[self.pipeline_position].set_state("A") #mocking the unavailability

        # make the worker not available anymore
        self.filter_list[self.pipeline_position].set_state("B")

        if self.pipeline_position == 0:
            if self.pipe_list[self.pipeline_position].set_state("O", "W") != -1:  # Open for writing
                self.pipe_list[self.pipeline_position].write_pipe(
                    self.filter_list[self.pipeline_position].actual_pipe)
                self.filter_list[self.pipeline_position].previous_pipe = None
            else:
                return -1
            if self.pipe_list[self.pipeline_position].set_state("C",
                                                                "W") == -1:  # Closing for writing
                return -1
        else:
            if self.pipe_list[self.pipeline_position - 1].set_state("O", "R") != -1:  # Open for reading
                self.filter_list[self.pipeline_position].previous_pipe += " "
                self.filter_list[self.pipeline_position].previous_pipe += self.pipe_list[
                    self.pipeline_position - 1].read_pipe()
                if self.pipe_list[self.pipeline_position - 1].set_state("C",
                                                                        "R") != -1:  # Closed for reading
                    if self.pipe_list[self.pipeline_position].set_state("O",
                                                                        "W") != -1:  # Open for writing
                        self.pipe_list[self.pipeline_position].write_pipe(
                            self.filter_list[self.pipeline_position].actual_pipe)
                    if self.pipe_list[self.pipeline_position].set_state("C",
                                                                        "W") == -1:  # Closed for writing
                        return -1
        self.pipeline_position += 1

