def linear_search(sequence, target):
    """
    Search a number in a list using linear search
    parameter sequence (list): a list of numbers to search within
    parameter target(int or float): the number to search for
    """
    # The enumerate() function in Python is a built-in tool that simplifies looping
    # Through a sequence (list, tuple, string) while keep track of both the index
    # and the value of each element
    
    # Syntax: enumerate(iterable, start=0)
    # iterable: The sequence you want to loop over (list, or string)
    # Start: Optional. The starting index for enumeration (default is 0)
     
    for index, value in enumerate(sequence, start=1): # start at index 1
        if value == target:
            return index # target found at this index
    return -1 # target not found

my_list = [10, 2, 4, 6, 7, 8, 11]
target = 10 

result = linear_search(my_list, target)

if result != -1:
    print(f"Number {target} found at index {result}")
else:
    print(f"Number {target} not found in the list")
    
# The index where it will start can be changed
# Examples:

fruits = ["banana", "apple", "orange"]
print("\nStarts at index 0 (default)")
for index, value in enumerate(fruits):
    print(f"Index: {index}, Fruit: {value}")
    
fruits = ["banana", "apple", "orange"]
print("\nStarts at index 1")
for index, value in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {value}")