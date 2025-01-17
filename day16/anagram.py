def get_word(prompt):
    """
    Prompt the user to enter a word, ensuring the input contains only letters
    
    Parameters:
    prompt(str): The message displayed to the user when asking for input
    
    returns:
    str: A cleaned and lowercase version of the input, with spaces removed
    """
    while True:
        word = input(prompt).replace(" ", "").lower()
        if word.isalpha():
            return word
        else:
            print("Only letters are allowed for word")

def anagram(word1, word2):
    """
    Check if two words are anagrams of each other

    Parameters:
    word1 (str): The first word to compare
    word2 (str): The second word to compare
    
    returns:
    bool: True if the words are anagrams, False otherwise.
    
"""
    return sorted(word1) == sorted(word2)

def main():
    """
    Main function to handle user input and check for anagrams.

    This function prompts the user for two words, checks if they are anagrams
    using the `anagram` function, and prints the result.
    """
    word1 = get_word("\nEnter the first word: ")
    word2 = get_word("Enter the second word: ")

    if anagram(word1, word2):
        print(f"\n{word1} and {word2} are anagrams!")
    else:
        print(f"\n{word1} and {word2} aren't anagrams!")

if __name__=="__main__":
    main()