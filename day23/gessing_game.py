import random

class gessing_game:
    """
    A number gessing game where the player has to gess a randomly
    generated number between 1 and 100
    """
    def __init__(self, guess=None):
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        self.guess = guess if guess is not None else self.get_input("Guess the number between 1 to 100: ")
    
    def get_input(self, prompt):
        """
        Prompt the player to enter a guess and provides 
        feedback if it's too low, too high or correct
        
        arg:
        prompt (str): The prompt message displayed to the player.
        
        returns:
        int: the player's guess
        """
        while True:
            try:
                value = int(input(prompt))
                self.attempts += 1
                if self.attempts == 7:
                    print(f"You've reached the maximum number of attempts. The number was {self.random_number}.")
                    break
                else:
                    if value < self.random_number:
                        print("Too low!")
                    elif value > self.random_number:
                        print("Too high!")
                    else:
                        print("You nailed it! ")
                        break
                    
            except ValueError:
                print("Invalid input! Enter a integer number!")

    def __str__(self):
        """
        Provides a string representation of the game's outcome.
        Returns:
        str: A massage indicating whether the player guessed the 
        number and how many attempts were made
        """
        return f"You guess the random number {self.guess} in {self.attempts} attempts" if self.guess == self.random_number else "Better luck next time!"
                
gess_game = gessing_game()
print(gess_game)
                    
                    
        
    
