import random

class GuessingGame:
    """
    A number guessing game where the player has to gess a randomly
    generated number between 1 and 100
    """
    def __init__(self, max_attempts=7):
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = max_attempts
        self.guess = None
        self.get_start()
    
    def get_start(self):
        """
        Prompt the player to enter a guess and provide feedback
        """
        while self.attempts < self.max_attempts:
            try:
                self.guess = int(input("Guess the number between 1 to 100: "))
                self.attempts += 1
                if self.guess < self.random_number:
                    print("Too low!")
                elif self.guess > self.random_number:
                    print("Too high!")
                else:
                    print("\nGreat! You've nailed it!")
                    break
            except ValueError:
                print("Invalid input! try again.")
        else:
            print(f"You've reached the maximum number of attempts. The number was {self.random_number}.")
     
    def __str__(self):
        """
        Provides a string representation of the game's outcome.
        Returns:
        str: A massage indicating whether the player guessed the 
        number and how many attempts were made
        """
        return f"You guess the random number {self.guess} in {self.attempts} attempts!" if self.guess == self.random_number else "Better luck next time!"
                
game = GuessingGame()
print(game)
                    
                    
        
    
