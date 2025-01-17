def get_word(prompt):
    """
    Count the number of words in a given string
    
    Parameters:
    Input string (str): The string whose words need to be counted
    
    returns:
    int: The number of words in the input string """
    while True:
        text = input(prompt)
        if text.strip():
            return text
        print("can't be a empty text")

def word_counter():
    text = get_word("Enter a text: ")
    count = text.split()
    return len(count)

if __name__=="__main__":

    print(f"The text had {word_counter()} words")