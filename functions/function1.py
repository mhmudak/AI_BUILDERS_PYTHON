def _my_function():
    print("Hello, World!")

_my_function()

tem1 = 77
celsius1 = (tem1 - 32) * 5 / 9
print(celsius1)

tem2 = 100
celsius2 = (tem2 - 32) * 5 / 9
print(celsius2)

tem3 = 32
celsius3 = (tem3 - 32) * 5 / 9
print(celsius3)

def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    return celsius #sends the results back



# parameters vs arguments
    # parameter: variable inside function itself | exmple. def fahrenheit_to_celsius(temp)
    #argument: value passed to the function on call | exmple. fahrenheit_to_celsius(77)
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(100))
print(fahrenheit_to_celsius(32))


def my_name(name, country = "Lebanon"):
    print("Helloo, " + name + " from " + country + "!")
    
my_name("MhMud", "Beirut")