# Loop for and loop while

for x in range(1, 11):
    print(x, end=", ") if x < 10 else print(f"{x}.")
    
x = 1
while x < 11:
    print(x, end=", ") if x < 10 else print(f"{x}.")
    x += 1