def get_palindrome(prompt):
    """
    Prompts the user for input, remove spaces, and converts the input to lowercase.
    Keep asking for input until a non empty string is provided
    """
    while True:
        text = input(prompt).replace(" ", "").lower()
        if text.strip(): # remove whitespaces and ensure that the string isn't empty
            return text
        else:
            print("A empty input can't be used")
    
def main():
    """
    Check if the input is a palindrome 
    
    returns: a message indicating whether the input is a palindrome or not"""
    
    palindrome = get_palindrome("\nEnter something to check if its a palindrome: ")
    
    if palindrome == palindrome[::-1]:
        return f"{palindrome} is a palindrome"
    return f"{palindrome} isn't a palindrome"

if __name__=="__main__":
    print(main())


   
    
 