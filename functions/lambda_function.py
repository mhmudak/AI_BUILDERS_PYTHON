# lambda arguments expression

my_lambda = lambda x: x * 2
print(my_lambda(5)) # prints 10


# multiple arguments
x = lambda a, b : a* b
print(x (5, 6))

plus = lambda k, j: k + j
print(plus(8, 6))

is_even = lambda x: x % 2 == 0
print(is_even(7))

def my_function(n):
    return lambda a : a * n

my_doubler = my_function(2)
my_tripler = my_function(3)

print(my_doubler(5)) # prints 10
print(my_tripler(5)) # prints 10

words = ["apple", "kiwi", "Mango", "strawberry", "banana"]
sorted_words = sorted(words, key = lambda x: len(x)) # sorts the list of words by their length
print(sorted_words)