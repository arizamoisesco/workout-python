def hex_output():
    decnum = 0
    hexnum = input("Ingresa un numero hexadecimal a convertir: ")
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)

hex_output()