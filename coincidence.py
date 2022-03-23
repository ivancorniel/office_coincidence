import sys
from datetime import datetime


with open(sys.argv[1], 'r') as file:
    schedules = file.readlines()

    week_sched = {}
    pairs = {}

    for line in schedules:
        emp = line.split('=')
        if not emp[0] in week_sched:
            emp[1] = emp[1].split(',')
            for i in emp[1]:
                day = i[:2]
                time_in = datetime.strptime(i[2:7], '%H:%M').time()
                time_out = datetime.strptime(i[8:13], '%H:%M').time()
                key = emp[0] + day
                week_sched[key]={'name' : emp[0], 'day': day, 'time_in': time_in, 'time_out': time_out}

    for i in week_sched:
        for j in week_sched:
            if not week_sched[i]['name'] == week_sched[j]['name'] and week_sched[i]['day'] == week_sched[j]['day']:
                if week_sched[i]['time_in'] <= week_sched[j]['time_out'] and week_sched[i]['time_out'] >= week_sched[j]['time_in']:
                    if week_sched[i]['name'] + '-' + week_sched[j]['name'] in pairs:        
                        pairs[week_sched[i]['name'] + '-' + week_sched[j]['name']] += 1
                    elif week_sched[j]['name'] + '-' + week_sched[i]['name'] in pairs: 
                        pairs[week_sched[j]['name'] + '-' + week_sched[i]['name']] += 1
                    else:
                        pairs.update({week_sched[i]['name']+'-'+week_sched[j]['name']: 1})

    pairs = {k:v // 2 for (k,v) in pairs.items()}
    
    print(week_sched)






    








