def convert_temperature(value, from_unit, to_unit):  
    celsies = 0
    if from_unit == "C":
        celsies = value
    elif from_unit == "F":
        celsies = (value-32)/1.8
    elif from_unit == "K":
        celsies = value - 273.15
    else:
        print("error")
        return

    output = 0
    if to_unit == "C":
        output = celsies
    elif to_unit == "F":
        output = (celsies*9/5)+32
    elif to_unit == "K":
        output = celsies + 273.15
    else:
        return "Non"
    return output


print(convert_temperature(100, "C", "F"))
print(convert_temperature(0, "K", "C"))
print(convert_temperature(-40, "C", "F"))
print(convert_temperature(20, "C", "X"))