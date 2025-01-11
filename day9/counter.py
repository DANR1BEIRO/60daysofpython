def counter():
    while True:
        try:
            limit = int(input("Enter a limit number: "))
            limit += 1
            if limit > 0:
                break
            else: 
                print("Number must be greater than zero!")
        except ValueError:
            print("Enter a integer number!")
            
    for i in range(1, limit):
        print(i, end=".") if i == limit - 1 else print(i, end=", ")
    print("\nThe counter has reached its limit")

if __name__=="__main__":
    counter()