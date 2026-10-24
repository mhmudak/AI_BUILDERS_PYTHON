# while condition is True:
#     execute this block of code

# i = 1

# while i < 6:
#     print(i)
#     if i==3:
#         break # exit loop
#     i += 1
    
y = 0

while y < 6:
    y += 1
    if y == 3:
        continue # skip the rest of the code in the loop when y is 3
    print(y)