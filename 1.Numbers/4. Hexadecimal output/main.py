def hex_output(number):
    decimal_result = 0

    for index, caracter in enumerate(reversed(number)):
        decimal_result += int(caracter, 16) * (16 ** index)
    
    return decimal_result


hex_number = input("Ingresa tu número hexadecimal: ")
print(hex_output(hex_number))