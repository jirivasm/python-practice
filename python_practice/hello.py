from helper import validate

#program
# print (f"20 days are {20 *calculation_to_units}{name_of_unit}")helper   
'''
#call function
# days_to_units(20)
# days_to_units(35)
# days_to_units(50)
# days_to_units(110)
'''
user_input = ""
#while looping
while user_input != "exit":
    
    user_input = input("hello enter the numbner of days and conversion unit or type exit:\n")
    days_and_unit = user_input.split(":")
    days_and_units_dictionary = {"days":days_and_unit[0], "unit":days_and_unit[1]}
    print(days_and_unit)
    validate(days_and_units_dictionary)
    
    
'''#program
# print (f"20 days are {20 *calculation_to_units}{name_of_unit}")
# print (f"35 days are {35 *calculation_to_units}{name_of_unit}")
# print (f"50 days are {50 *calculation_to_units}{name_of_unit}")
# print (f"110 days are {110 *calculation_to_units}{name_of_unit}")
'''
