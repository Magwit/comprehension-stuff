# What I remember

print("Before")
nuffror = [num for num in range(1, 8)]
print("After")
# print(nuffror)

# List comprehensions + jsonpath = TA for WFE

# Shorthand syntaxt to create a liost from another list

# Multiply numbers > 1 by two
numbers = [1, 3, 5, 7, 9, 12, 13, 16, 17, 20]

multi = [num * 2 for num in numbers if num > 1]
# print(multi)

# Even numbers with Corey

evens = [num for num in numbers if num % 2 == 0]
print(evens)

# Two lists producing a list of tuples
tupla = [(letter, number) for letter in "abcd" for number in range(4)]
# print(tupla)

# Dictionary comprehensions by zipping two lists
names = ["Bruce", "Clark", "Peter", "Diana", "Wade"]
heroes = ["Batman", "Superman", "Spiderman", "Wonder Woman", "Wade"]
superdict = {name: hero for name, hero, in zip(names, heroes)}
# print(superdict)


# Generator expression

my_gen = (n * n for n in numbers)

for i in my_gen:
    print(i)
