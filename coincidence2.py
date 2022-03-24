import sys
from datetime import datetime


class schedule:

    instances = []

    def __init__(self, worker, day, time_in, time_out):
        self.worker = worker
        self.day = day
        self.time_in = time_in
        self.time_out = time_out
        schedule.instances.append(self)

    @classmethod
    def find_coincidence(cls):
        MO, TU, WE, TH, FR, SA, SU = [], [], [], [], [], [], []
        pairs = {}
        for i in cls.instances:
            if i.day == 'MO':
                for j in MO:
                    if i.time_in <= j.time_out or i.time_out >= j.time_in:
                        k = i.worker + '-' + j.worker
                        k2 = j.worker + '-' + i.worker
                        if k in pairs or k2 in pairs:
                            pairs[k] += 1
                        else:
                            pairs.update({k : 1})
                else:    
                    MO.append(i)
            elif i.day == 'TU':
                for j in TU:
                    if i.time_in <= j.time_out or i.time_out >= j.time_in:
                        k = i.worker + '-' + j.worker
                        k2 = j.worker + '-' + i.worker
                        if k in pairs or k2 in pairs:
                            pairs[k] += 1
                        else:
                            pairs.update({k : 1})
                else:    
                    TU.append(i)
            elif i.day == 'WE':
                for j in WE:
                    if i.time_in <= j.time_out or i.time_out >= j.time_in:
                        k = i.worker + '-' + j.worker
                        k2 = j.worker + '-' + i.worker
                        if k in pairs or k2 in pairs:
                            pairs[k] += 1
                        else:
                            pairs.update({k : 1})
                else:    
                    WE.append(i)                            
            elif i.day == 'TH':
                for j in TH:
                    if i.time_in <= j.time_out or i.time_out >= j.time_in:
                        k = i.worker + '-' + j.worker
                        k2 = j.worker + '-' + i.worker
                        if k in pairs or k2 in pairs:
                            pairs[k] += 1
                        else:
                            pairs.update({k : 1})
                else:    
                    TH.append(i)                            
            elif i.day == 'FR':
                for j in FR:
                    if i.time_in <= j.time_out or i.time_out >= j.time_in:
                        k = i.worker + '-' + j.worker
                        k2 = j.worker + '-' + i.worker
                        if k in pairs or k2 in pairs:
                            pairs[k] += 1
                        else:
                            pairs.update({k : 1})
                else:    
                    FR.append(i)                            
            elif i.day == 'SA':
                for j in SA:
                    if i.time_in <= j.time_out or i.time_out >= j.time_in:
                        k = i.worker + '-' + j.worker
                        k2 = j.worker + '-' + i.worker
                        if k in pairs or k2 in pairs:
                            pairs[k] += 1
                        else:
                            pairs.update({k : 1})
                else:    
                    SA.append(i)
            elif i.day == 'SU':
                for j in SU:
                    if i.time_in <= j.time_out or i.time_out >= j.time_in:
                        k = i.worker + '-' + j.worker
                        k2 = j.worker + '-' + i.worker
                        if k in pairs or k2 in pairs:
                            pairs[k] += 1
                        else:
                            pairs.update({k : 1})
                else:    
                    SU.append(i)   
                                             
        for k in pairs:
            print(k, ':', pairs[k])
                

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
            key = schedule(sched[0], day, time_in, time_out)


schedule.find_coincidence()