class Schedule:

    instances = []
    coincidences = {}

    def __init__(self, worker, day, time_in, time_out):
        self.worker = worker
        self.day = day
        self.time_in = time_in
        self.time_out = time_out
        Schedule.instances.append(self)
        self.find_coincidences()

    def find_coincidences(self):
        for i in self.instances:
            if self.day == i.day and not self.worker == i.worker:
                if self.time_in <= i.time_out or self.time_out >= i.time_in:
                    k = self.worker + '-' + i.worker + ':'
                    k2 = i.worker + '-' + self.worker + ':'
                    if k in Schedule.coincidences or k2 in Schedule.coincidences:
                        Schedule.coincidences[k] += 1
                    else:
                        Schedule.coincidences.update({k : 1})

    @classmethod
    def get_coincidences(cls):
        return cls.coincidences

    def __repr__(self) -> str:
        return self.worker + ' ' + str(self.time_in) + ' ' + str(self.time_out)


