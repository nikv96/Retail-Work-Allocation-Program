from assignworkers import assignWorkers
from fileRead import fileRead
import prettyprint

#File Read to compute the days off for people
off_days = fileRead()

#Logic of assignments
assign = assignWorkers(off_days)

#Assigned days and names  - Global Variables
assigned_days = assign[0]
assigned_names = assign[1]

#Menu of Choices
print("Welcome to the Retail Workers Module\n")
choice = 0
while choice != 4:
	print("\nChoose a query from the following menu: ")
	choice = input("1. Display weekly schedule\n2. Search individual schedule by name\n3. Display all individual schedules \n4. Exit\nPlease your Enter choice(1,2,3,4): ")
	if (choice not in [1,2,3,4]):
		choice = input("Please enter a valid input: ")
	if choice == 1:
		prettyprint.pretty_print_weekly(assigned_days)
	elif choice ==2:
		name = str(raw_input("Please enter a name: "))
		if(name not in assigned_names.keys()):
			print("Name unavailable")
			continue
		prettyprint.pretty_print_name(assigned_names, name)
	elif choice==3:
		prettyprint.pretty_print_namewise(assigned_names)

print("Thank you for using this application")
				
	
