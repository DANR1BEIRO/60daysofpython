def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9)

def main(temperature, conversion_type):
    if conversion_type == "celsius":
        print(f"{temperature} celsius = {celsius_to_fahrenheit(temperature)} fahrenheit")

    elif conversion_type == "fahrenheit":
        print(f"{temperature} fahrenheit = {fahrenheit_to_celsius(temperature)} celsius")
    else:
        return print("Invalid convertion type")


if __name__=="__main__":

    main(0, "celsius")
    main(32, "fahrenheit")