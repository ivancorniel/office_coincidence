from datetime import datetime
import csv
from abc import ABC, abstractmethod


class Schedule:

    instances = []
    coincidences = {}

    def __init__(self, worker: str, day: str, time_in: str, time_out: str)-> None:
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


class Intake(ABC):

    @abstractmethod
    def process_input(self, data: str) -> None:
        pass


class TXTFileInput(Intake):
    
    def process_input(self, data: str) -> None:
        with open(data, 'r') as file:
            schedules = file.readlines()

            for line in schedules:
                sched = line.split('=')
                sched[1] = sched[1].split(',')
                for i in sched[1]:
                    day = i[:2]
                    time_in = datetime.strptime(i[2:7], '%H:%M').time()
                    time_out = datetime.strptime(i[8:13], '%H:%M').time()
                    Schedule(sched[0], day, time_in, time_out)


class CSVFileInput(Intake):
    
    def process_input(self, data: str) -> None:
        with open(data, 'r') as file:
            schedules = csv.DictReader(file)

            for line in schedules:
                name = line['name']
                day = line['day']
                time_in = line['time in']
                time_out = line['time out']
                Schedule(name, day, time_in, time_out)



        



