def get_prime():
    """
    Prompt the user to enter a number and ensure it's valid for prime number
    """
    while True:
        try:
            number = int(input("Enter a number to check if it's prime: "))
            if number > 1:
                return number
            else:
                print("A prime number can't be equal to or less than 1!")
        except ValueError:
            print("Must be a integer number!")

def is_prime(number):
    """
    Check if the given number is a prime number.
    
    Parameters:
    number (int): The number to check
    
    Returns:
    bool: True if the number is prime, False otherwise."""
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

candidate = get_prime()

if is_prime(candidate):
    print(f"{candidate} is a prime number")
else:
    print(f"{candidate} isn't a prime number")
        
