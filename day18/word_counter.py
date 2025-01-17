def get_word(prompt):
    """
    Prompt the user for a non empty string input
    
    Parameters:
    Prompt (str): The message displayed to the user to ask for input
    
    returns:
    str: The non empty string entered by the user"""
    while True:
        text = input(prompt)
        if text.strip(): # ensure that the input isn't empty or just whitespace
            return text
        print("can't be a empty text")

def word_counter():
    """
    Counts the number of words in the given string
    
    returns:
    int: The number of words in the input
    """
    text = get_word("Enter a text: ")
    count = text.split()
    return len(count)

if __name__=="__main__":

    print(f"The text had {word_counter()} words")