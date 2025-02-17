import random

def launch_dice():
    """
    Simulate the roll of a six-sided die
    """
    
    roll = random.randint(1, 6)
    print(f"The die shows: {roll}")

if __name__=="__main__":
    launch_dice()