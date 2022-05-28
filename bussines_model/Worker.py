class Worker:
    __name = None
    __id = None
    __job = None

    def __init__(self, name, id, job):
        self.__name = name
        self.__id = id
        self.__job = job

    def get_job(self):
        return self.__job

    def get_name(self):
        return self.__name