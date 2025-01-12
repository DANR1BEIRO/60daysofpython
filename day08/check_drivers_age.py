def check_drivers_age():
    """
    Function that takes the user's age and returns whether the user can drive
    """
    while True:
        try:
            age = int(input("Enter the age: "))
            print("You can drive") if age >= 18 else print("You can't drive")
            break
        
        except ValueError:
            print("Only integer numbers are allowed for age!")
            
if __name__=="__main__":
    check_drivers_age()
