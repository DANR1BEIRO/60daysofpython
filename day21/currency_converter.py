
class converter:
    def __init__(self):
        self.currency = self.get_currency()
        self.value = self.get_amount()
        
    conversionType = {
        1: "Real to Dollar",
        2: "Dollar to Real"
    }
        
    def get_currency(self):
        while True:
            try:
                choice = int(input("Type of conversion:\n[1] Real to dollar\n[2] Dollar to real\n"))
                if choice in self.conversionType:
                    return choice 
                else:
                    print("Select one of the two available options")    
            except ValueError: 
                print("Only integer numbers are allowed")
                
    def get_amount(self):
        while True:
            try:
                amount = float(input(f"Enter how much in {'Real: R$' if self.currency == 1 else 'Dollar: U$'} "))
                if amount > 0:
                    return amount
                else:
                    print("Can't be zero or negative")
            except ValueError:
                print("Must be a number")

    def get_converter(self): 
        if self.currency == 1:
            converted_value = round(self.value / 6.04, 2)
            print(f"R${self.value} is equivalent to U${converted_value}")
            
        elif self.currency == 2: 
            converted_value = round(self.value * 6.04, 2)  
            print(f"U${self.value} is equivalent to R${converted_value}")
            
if __name__=="__main__":
    converter().get_converter()