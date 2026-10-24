fruits = ["banana", "apple", "orange"]

for fruit in fruits:
    print(fruit)
    if fruit == "apple":
        break

# newlist = []    

# for x in fruits:
#     if x != "apple":
#         newlist.append(x)
        
# newlist = [x for x in fruits if x != "apple"] # creates a new list with all fruits except apple
# print(newlist)
    
# for x in "banana":
#     if x == 'n':
#         continue
#     print(x)
    
# for i in range(5):
#     print(i)
    
# adj = ["red", "big", "tasty"]
# fruits = ["banana", "apple", "orange"]

# for x in adj:
#     for y in fruits:
#         print(x, y)

newlist2 = [x for x in range(10) if x < 5]
print(newlist2)