#We use a factory because is easier to manage the more pipelines
class Factory:
    workers = None
    def __init__(self, workers):
        self.workers = workers

    def start_shift(self, workers_group, p): #starts a pipeline
        p.attach_workers(workers_group)
        p.start()

