from datetime import datetime

user_input=input("enter your goal with a deadline separated by a colon\n")
input_list=user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
#calculating the time difference between now and the deadline
print(datetime.now())
time_difference = deadline_date - datetime.now()
print(input_list)
print(deadline_date)
print(time_difference)
print("Dear user! Time Remaining for your goal:"+ goal + " is " + str(time_difference.days) + " days, and " + str(time_difference.seconds//3600) + " hours")
