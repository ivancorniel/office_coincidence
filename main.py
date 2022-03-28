import sys
from datetime import datetime
from coincidence2 import Schedule


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