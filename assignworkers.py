import define

'''This script contains the logic for assigning employees'''

def assignWorkers(off_days):
	#Scheduled days and individual schedules are stored in dictionaries
	assigned_days = {}
	assigned_names = {}
	i = 0
	for day in define.weekends:
		assigned_days[day] = []
		i=0
		for name in off_days.keys():
			if day not in off_days[name]:
				assigned_days[day].append(name)
				i = i+1
			if i == 3:
				break
	i = 0
	for day in define.weekdays:
		assigned_days[day] = []
		i=0
		for name in off_days.keys():
			if day not in off_days[name]:
				assigned_days[day].append(name)
				i = i+1
			if i == 2:
				break

	for name in off_days.keys():
		assigned_names[name] = []
		for day in assigned_days.keys():
			if name in assigned_days[day]:
				assigned_names[name].append(day)
	
	return [assigned_days, assigned_names]
