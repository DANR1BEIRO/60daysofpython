def multiply_table(prompt):
    """
    A function that asks the user for a number and returns its multiplication table
    """
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                break
            else:
                print("Number must be greater than 0!")
        except ValueError:
            print("Only integer numbers are allowed!")

    for multiplier in range(1, 11):
        product = multiplier * number
        print(f"{multiplier} x {number} = {product}")

if __name__=="__main__":
    multiply_table("Multiplication table of: ")
    