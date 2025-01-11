# sum of two numbers
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("The enter must be a number!")
            
def main():
    print("This program calculates the sum of two numbers.")
    
    n1 = get_number("Enter the first number: ")
    n2 = get_number("Enter the second number: ")

    print(f"The sum of {n1} and {n2} is {n1 + n2}")
                        
if __name__=="__main__":
    main()
    
