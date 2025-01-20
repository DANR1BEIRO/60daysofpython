def grade_average(grades):
    """
    Calculate the average of a list of grades
    If the list is empty, return 0
    
    Parameters:
    grades (list of float or int)
    
    Returns:
    Float: The average of the grades
    
    """
    if not grades:
        return 0
    return sum(grades) / len(grades)

grades = [80, 90, 50]
average = round(grade_average(grades), 2)
print(f"The average is {average}")


