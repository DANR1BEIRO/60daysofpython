class CalculateBMI:
    
    BMI_CATEGORIES = {
        "Underweight": (0, 18.4),
        "Normal weight": (18.5, 24.9),
        "Overweight": (25.0, 29.9),
        "Obesity": (30, float('inf')),
    }
    
    def __init__(self, height=None, weight=None):

        """
        Initialize the CalculateBMI class.
        If height and weight are not provided, prompt the user for input
        """
        
        self.height = height if height is not None else self.get_input("Enter your height (m): ", "height")
        self.weight = weight if weight is not None else self.get_input("Enter your weight (kg): ", "weight")
        self.bmi = self.calculate_bmi()
        self.category = self. get_bmi_category()

    def get_input(self, prompt, input_type):
        """
        Method to get valid user input for height ow weight
        """
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print(f"{input_type.capitalize()} must be a positive number.")
                else:
                    return value
            except ValueError:
                print("Enter a valid number")
                
    def calculate_bmi(self):
        """
        Calculate BMI using the formula: BMI = weight / (height ** 2).
        """
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        """
        Determine the BMI category based on the calculate BMI
        """
        for category, (low, high) in self.BMI_CATEGORIES.items():
            if low <= self.bmi <= high:
                return category
        return "Unknown"

    def display_results(self):
        """
        Display the BMI and its category.
        """
        print(f"\nYour BMI is {round(self.bmi, 2)}.")
        print(f"You are classified as {self.category}.")

    def __str__(self):
        return f"\nCalculateBMI:\nHeight = {self.height}\nWeight = {self.weight}\nBMI = {round(self.bmi, 2)}\nCategory = {self.category}"

if __name__=="__main__":
    
    bmi = CalculateBMI(1.73, 87)
    bmi.display_results()
    print(bmi)
 

