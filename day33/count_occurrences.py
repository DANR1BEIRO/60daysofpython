from collections import Counter

def count_occurrences(_list):
    """
    Counting occurrences of each element in a list
    
    returns:
    Counter: An object of type Counter containing the count of each element
    """
    container = Counter(_list)
    for element, amount in container.items():
        print(f"{element}: {amount}")
    
    return "Counter successfull"

if __name__=="__main__":
    array = [1, 2, 3, 3, 4, 4, 5, 6, 7, 1]
    print(count_occurrences(array))
    print(Counter(array))
    
    
    