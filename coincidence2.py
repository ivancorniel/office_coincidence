import sys
from datetime import datetime


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
        for i in cls.coincidences:
            print(i, cls.coincidences[i])                

    def __repr__(self) -> str:
        return self.worker + ' ' + str(self.time_in) + ' ' + str(self.time_out)


def main():
    with open(sys.argv[1], 'r') as file:
        schedules = file.readlines()

        for line in schedules:
            sched = line.split('=')
            sched[1] = sched[1].split(',')
            for i in sched[1]:
                day = i[:2]
                time_in = datetime.strptime(i[2:7], '%H:%M').time()
                time_out = datetime.strptime(i[8:13], '%H:%M').time()
                key = sched[0] + day
                key = Schedule(sched[0], day, time_in, time_out)
    
    Schedule.get_coincidences()


if __name__ == '__main__':
    main()