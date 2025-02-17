import math

def square_root(number):
    
    if number < 0:
        raise ValueError("Only numbers greater than zero are allowed")
    
    return round(math.sqrt(number), 2)

if __name__=="__main__":
    print(square_root(144))