# a == b
# a != b
# a > b
# a < b
# a >= b
# a <= b


# if condition is true:
#     execute this block of code

# a = 10
# b = 10

# if a > b:
#     print("a is greater than b")
# elif a < b:
#     print("a is less than b")

# else:
#     print("a is equal to b")

# x = 41
# if x > 10:
#     print("x is greater than 10")
#     if x > 20:
#         print("and also greater than 20")
#     if x > 30:
#         print("and also greater than 20 and 30")
#     else:
#         print("but is not greater than 20")
# else :
#     print("x is not greater than 10")


age = 23
has_license = True

if age >= 18:
    if has_license:
        print("u can drive")
    else:
        print("u need a license to drive")
        
else:
    print("u r too young to drive")
    
if age >= 18 and has_license:
    print("u can drive")