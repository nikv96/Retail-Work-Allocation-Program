import define

'''This script provides functions for pretty printing'''

def pretty_print_weekly(assigned_days):
	print ("Day\t\t" + "Workers")
	print ("===========================")
	for day in define.days:
		print day[:3].upper() + "\t\t" + str(assigned_days[day])

def pretty_print_namewise(assigned_names):
	print ("Workers\t\t" + "Days")
	print ("===========================")
	for name in assigned_names.keys():
		print name + "\t\t" + str(assigned_names[name])

def pretty_print_name(assigned_names, name):
	print ("Workers\t\t" + "Days")
	print ("===========================")
	print name + "\t\t" + str(assigned_names[name])
