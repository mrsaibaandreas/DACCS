import arch.Pipeline as pipeline
import arch.Filter as filter
class Process:
    jobs = None
    workers = None
    def __init__(self):
        self.jobs = {'CS': 'Cut Seat',
                'AF': 'AssembleFeet',
                'AB': 'AssembleBackrest',
                'AS': 'AssembleStabilizer',
                'P': 'Package'}

    def attach_workers(self, workers):
        self.workers = workers

    def new_proc(self, initial, name):
        self.jobs[initial] = name #update dictionary

    def start_assemble(self, pipes):
        pipes.set_pipel_state("B")
        for pipe_nr in range(len(pipes.filter_list)):
            if pipes.pipeline_position == 0:
                pipes.write_in_pipe()
            else:
                pipes.pipeline_position = pipe_nr
                pipes.write_in_pipe()
            if pipe_nr + 1 >= len(pipes.filter_list):
                break
            print("working on " + pipes.filter_list[pipes.pipeline_position].actual_pipe)

            pipe_nr += 1
        pipes.set_pipel_state("PR")



    def start(self):
        pipes = pipeline.Pipeline()
        index = 0
        for job in self.workers:
            pipes.filter_list.append(filter.Filter(job.get_job()))
            index += 1
        pipes.set_pipelist()
        self.start_assemble(pipes)
