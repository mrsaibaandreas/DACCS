class Worker:
    __name = None
    __id = None
    __job = None

    def __init__(self, name, id, job):
        self.__name = name
        self.__id = id
        self.__job = job

    def work(self, job):
        print("Worker " + self.__name + "_" + self.__id + "started working")
        print("He is working on " + job)

