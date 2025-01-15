def fibonacci():
    while True:
        try:
            term = int(input("Enter the fobinacci term: "))
            if 0 < term:
                break
        except ValueError:
            print("Fibonacci term must be an integer number!")

    if term <= 2:
        return [] if term <= 0 else [0] if term == 1 else [0, 1]

    sequence = [0, 1]

    for i in range(2, term):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

if __name__=="__main__":
    result = fibonacci()
    print(f"The fibonacci sequence up to {len(result)} is {result}")