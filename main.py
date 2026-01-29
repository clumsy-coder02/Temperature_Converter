print() # spacing
print("Interactive Temperature Converter")
print() # spacing

# begin conversion
def conversion():
    # Enter current readings
    temp = float(input("Enter temperature readings: "))
    print("Enter unit for temperature readings 'f' for fahrenheit and 'c' for celsius")
    unit = str(input("Enter unit for temperature readings: "))
    
    if unit == "f" or unit == "F":
        # convert from degree fahrenheit to degree celsius
        celsius = (temp - 32) * 5/9
    
        print() # spacing
        # display results
        readings = f"Current readings: {temp:.2f}F\nTemperature in degrees celsius: {celsius:.2f}C"
        # .2f = two digits after the decimal point
    elif unit == "c" or unit == "C":
        # convert from degree celsius to degree fahrenheit
        fahrenheit = (temp * 9/5) + 32

        print() # spacing
        # display results
        readings = f"Current readings: {temp:.2f}C\nTemperature in degrees fahrenheit: {fahrenheit:.2f}F"
        # .2f = two digits after the decimal point
    else:
        readings = "Enter the right reading with the unit"
    return print(readings)


if __name__ == "__main__":
    conversion()

