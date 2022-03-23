# class Worker:
#     def __init__(self, MO='00:00-00:00', TU='00:00-00:00', WE='00:00-00:00', TH='00:00-00:00', FR='00:00-00:00', SA='00:00-00:00', SU='00:00-00:00'):
#         self.MO = MO
#         self.TU = TU
#         self.WE = WE
#         self.TH = TH
#         self.FR = FR
#         self.SA = SA
#         self.SU = SU

# RENE= { 'MO':'10:00-12:00',
#         'TU':'10:00-12:00',
#         'TH':'01:00-03:00',
#         'SA':'14:00-18:00',
#         'SU':'20:00- 21:00' }

# ASTRID={'MO':'10:00-12:00',
#         'TH':'12:00-14:00',
#         'SU':'20:00-21:00' }

# ANDRES={'MO':'10:00-12:00',
#         'TH':'12:00-14:00',
#         'SU':'20:00-21:00' }


# RENE='MO10:00-12:00','TU10:00-12:00','TH01:00-03:00','SA14:00-18:00','SU20:00- 21:00'
# ASTRID='MO10:00-12:00','TH12:00-14:00','SU20:00-21:00'
# ANDRES='MO10:00-12:00','TH12:00-14:00','SU20:00-21:00'

from datetime import datetime

def coincidence(**kwargs): 
    if kwargs:
        emp_sched = {k:v for (k,v) in kwargs.items()}
        cleaned_sched = []
        for emp in emp_sched:
            sched = emp_sched[emp].split(',')
            for i in sched:
                day = i[:2]
                time_in = datetime.strptime(i[2:7], '%H:%M').time()
                time_out = datetime.strptime(i[8:], '%H:%M').time()
                emp_ = {'name': emp, 'day': day, 'time_in': time_in, 'time_out': time_out}
                cleaned_sched.append(emp_)


        pairs = {}

        for i in cleaned_sched:
            for j in cleaned_sched:
                if i['day'] == j['day']:
                    if not j['name'] == i['name']:
                        if i['time_in'] <= j['time_out'] and i['time_out'] >= j['time_in']: 
                            if i['name'] + '-' + j['name'] in pairs:
                                pairs[i['name'] + '-' + j['name']] += 1
                            elif j['name'] + '-' + i['name'] in pairs: 
                                pairs[j['name'] + '-' + i['name']] += 1
                            else:
                                pairs.update({i['name']+'-'+j['name']: 1})
        for pair in pairs:
            pairs[pair] = pairs[pair] // 2

        return pairs

    else:
        return 'No arguments were provided'


print(coincidence(
    RENE='MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00', 
    ASTRID='MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
    ANDRES='MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
    JOSE='MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00',
    JUAN='MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
    JOE='MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')
    )



    








