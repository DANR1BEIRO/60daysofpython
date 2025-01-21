class calculate_bmi:
    def __init__(self):
        self.height = self.get_height()
        self.weight = self.get_weight()
        self.bmi = self.get_bmi()
        
    BMI_categories = {
        
        "underweight": (0, 18.4),
        "normal weight": (18.5, 24.9),
        "overweight": (25.0, 29.9),
        "obesity": (30, float('inf')),  
    }
    
    def get_height(self):
        while True:
            try:
                height = float(input("Enter your height(m): "))
                if 0 < height:
                    return height
                else: 
                    print("Height can't be negative or zero")
            except ValueError:
                print("Enter a valid number")

    def get_weight(self):
        while True: 
            try:
                weight = float(input("Enter your weight(kg): "))
                if 0 < weight:
                    return weight
                else:
                    print("Weight can't be negative or zero")
            except ValueError:
                print("Enter a valid number")
                
    def get_bmi(self):
        
        bmi = self.weight / (self.height ** 2)
        
        for category, (low, high) in self.BMI_categories.items():
            if low <= bmi <= high:
                print(f"\nAccording your BMI {round(bmi, 2)}, you're classified as {category}.")
                return bmi
            
if __name__=="__main__": 
    calculate_bmi()
        