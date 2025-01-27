import random

def random_number_generator():
    
    random_numbers = []

    for _ in range(10):
        number = random.randint(1, 100)# generate a random number between 1 to 100
        random_numbers.append(number)
        
    print("Random number generator:")
    for i, number in enumerate(random_numbers, start=1):
        print(f"Number {i}: {number}")

if __name__=="__main__":
    random_number_generator()
    
    