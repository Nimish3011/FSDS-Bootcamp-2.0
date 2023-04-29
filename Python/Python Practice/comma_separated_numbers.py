# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

value = input("Input some comma seprated numbers : ")
list = value.split(",")
tuple = tuple(list)

print("List: ",list)
print("Tuple: ",tuple)