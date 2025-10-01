# function to convert celsius to fahrenheit with return statemnet

def celsius_to_fahrenheit(celsius):
    fahrenheit= (celsius * 9/5) +32 

    return fahrenheit
temp_f = celsius_to_fahrenheit(25)
print(temp_f)
print("with return:",type(temp_f))



# function to convert celsius to fahrenheit - without returen


def celsius_to_fahrenheit(celsius):
    fahrenheit= (celsius * 9/5) +32 

    print( fahrenheit)

temp_f2 = celsius_to_fahrenheit(50)
print("without return:",type(temp_f2))


