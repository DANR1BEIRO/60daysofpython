def even_or_odd():
    """
    Function that takes a number and returns whether
    it is even or odd
    """
    while True:
        try: 
            number = int(input("Enter a number: "))
            if number % 2 == 0:
                print("It's an even number")
            else:
                print("It's an odd number")
            break
        except ValueError:
            print("The enter must be a number!")

if __name__=="__main__":
    even_or_odd()