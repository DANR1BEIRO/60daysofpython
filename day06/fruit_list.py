# Doing a fruit list

fruit_list = []

while True:
    fruit = input("Enter a fruit (q to quit): ").capitalize().strip()
    if fruit == "Q":
        break
    elif fruit.isalpha():
        fruit_list.append(fruit)
    else:
        print("Only letters are allowed to fruit")
    
print(f"Here's your fruit list:\n{fruit_list}")