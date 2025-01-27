def write_file(file_name, content):
    """
    A function that writes content to a txt file
    
    Arguments: 
    file_name(str): The name of the file to be created or modified 
    content (str): The text to be written to the file"""

    with open(file_name, 'w') as file: # w = write
        file.write(content)

    print(f"The content was save in the file: {file_name}.")

def read_file(file_name):
    """
    A function that reads content of a txt file
    
    arguments:
    file_name (str): The name of the file to be read
    """
    try:
        with open(file_name, 'r') as file: # r = read
            content = file.read()
        print(f"File content: {content}")
        
    except FileNotFoundError:
        print("The file can't be fount!")
        
def main(file_name, content):
    
    write_file(file_name, content)
    
    read_file(file_name)
    
if __name__=="__main__":
    file = "goku.txt"
    content = "Super sayajin"

    main(file, content)