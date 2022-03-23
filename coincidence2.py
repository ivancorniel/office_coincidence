import sys
from datetime import datetime


class schedule:
    def __init__(self, worker, day, time_in, time_out):
        self.worker = worker
        self.day = day
        self.time_in = time_in
        self.time_out = time_out
    


        
with open(sys.argv[1], 'r') as file:
    schedules = file.readlines()

    x = {}

    for line in schedules:
        sched = line.split('=')
        sched[1] = sched[1].split(',')
        for i in sched[1]:
            day = i[:2]
            time_in = datetime.strptime(i[2:7], '%H:%M').time()
            time_out = datetime.strptime(i[8:13], '%H:%M').time()
            key = sched[0] + day

            key = schedule(sched[0], day, time_in, time_out)

            print(key.__getattribute__('time_in'))
