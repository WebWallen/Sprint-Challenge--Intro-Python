# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"({self.name}: {self.age})"
        # Note: this is why Uppercase output looked weird -- modified for simpler return statement

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone whose name starts with 'D':
print("Starts with D:")
# Format: object.key for placeholder in array if object.key.conditional('to-sort-by')
a = [human.name for human in humans if human.name.startswith('D')]
print(a)

# Write a list comprehension that creates a list of names of everyone whose name ends in "e".
print("Ends with e:")
b = [human.name for human in humans if human.name.endswith('e')]
print(b)

# Write a list comprehension that creates a list of names of that start with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
letters = ('C', 'D', 'E', 'F', 'G')
# Usually smart to create a variable containing desired conditions when it's more complex than one thing
c = [human.name for human in humans if human.name.startswith(letters)]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
# Math/modifications should go at the start of an LC most of the time
d = [human.age + 10 for human in humans]
print(d)

# Write a list comprehension that creates a list of strings with name joined to age with a hyphen
print("Name hyphen age:")
# Can't add a name and number, so age must be converted to a string
e = [human.name + '-' + str(human.age) for human in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing (name, age)
print("Names and ages between 27 and 32:")
# Specify tuple with (entry1, entry2). Must type object.key for both parts of If Statement or it only registers first.
f = [(human.name, human.age) for human in humans if (human.age < 32 and human.age > 26)]
print(f)

# Write a list comprehension that creates a list of new Humans with uppercase names and ages increased by five years.
print("All names uppercase:")
# Must make call to Human class because we're changing every entry instead of sorting info or doing basic math.
g = [Human(human.name.upper(), (human.age + 5)) for human in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(human.age) for human in humans]
print(h)
