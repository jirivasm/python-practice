#switch to functions
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit}"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} {conversion_unit}"
    else:
        return "unsupported unit"

def validate(days_and_units_dictionary):
    ''' if user_input.isdigit():
    #     #change from string to number
    #     user_input_number=int(user_input)
    #     if user_input_number > 0:
    #         #creeating a variable to the days_to_units function
    #         calculated_value = days_to_units(user_input_number)
    #         #printing the function
    #         print (calculated_value )
    #     elif user_input_number==0:
    #         print("entered 0, no conversion sorry")

    # else:
    #     print("no integer positive number please try again")
    '''
    try:
        #change from string to number
        user_input_number=int(days_and_units_dictionary["days"])
        if user_input_number > 0:
            #creeating a variable to the days_to_units function
            calculated_value = days_to_units(user_input_number, days_and_units_dictionary["unit"])
            #printing the function
            print (calculated_value )
        elif user_input_number==0:
            print("entered 0, no conversion sorry")
        else:
            print("positive number, no conversion")
    except ValueError:
        print("no integer positive number please try again")