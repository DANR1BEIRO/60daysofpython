# Takes a user specified number of random integer inputs and
# sorts them in ascending and descending order

def ascending_order(numbers):
    """
    Function that takes a list of numbers and sort the list in ascending order (smallest to largest)
    """
    ascending_ordered_number = sorted(numbers)
    return ascending_ordered_number
    
def descending_order(numbers):
    """
    Function that takes a list of numbers and sort the list in descending order (largest to smallest)
    """
    descending_ordered_number = sorted(numbers, reverse=True)
    return descending_ordered_number

def quantity_of_numbers():
    """
    A function that asks how many numbers the user's list must have
    """
    while True:
        try: 
            amount_numbers = int(input("Enter how many numbers you want in your list: "))
            if amount_numbers > 0:
                return amount_numbers
            else:
                print("The number must be greater than zero!")
        except ValueError:
            print("Only integer numbers are allowed!")

def users_input():
    """
    Function that collects a user specified number of 
    integer inputs and returns them as a list.
    """
    numbers = [] # start an empty list
    limit = quantity_of_numbers() # 

    while len(numbers) < limit: # loop to continue prompting until the list contains limit
        try:
            num_input = int(input(f"Enter number {len(numbers) + 1}: "))
            numbers.append(num_input) # add the input to the list `numbers`
        except ValueError:
            print("Only integer numbers are allowed!")
    return numbers
          
def main():  
    user_list = users_input()
    print(f"The list in ascending order is: {ascending_order(user_list)}")
    print(f"The list in descending order is: {descending_order(user_list)}")

if __name__=="__main__":
    main()
    