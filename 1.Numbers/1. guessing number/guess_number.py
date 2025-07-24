'''
Requerimientos:

Ecribir una función que se llame guessing_game que no tome argumentos
Cuando corra la funcion seleccionará un número aleatorio entre 0 y 100 (inclusive)

Entonces le prgunta al usuario que número quiere seleccionar
Cada vez que el usuario ingrese los dato, el programa indicará lo siguiente.
- Muy alto
- Muy bajo
- Muy cerca -- Es mostrar que es igual solución correcta
Si el usuario seleccional el número correcto el programa se cirral, de lo contrato pregunta de nuevo el usuario
El programa solo cierra despues de que el usuario ha adivinado correctamente

EXTRA:

Darle solo 3 chances al usuario y si no acierta se sale del programa
No solo debe elegir un número aleatorio, sino también una base numérica aleatoria, del 2 al 16, en la que el usuario deberá introducir su entrada. Si el usuario introduce "10" como su respuesta, deberá interpretarlo correctamente. "10" podría significar 10 (decimal), 2 (binario) o 16 (hexadecimal).
'''

import random

def guessing_game():
    computer_number = random.randint(1,100)

    user_number = int(input("Ingresa el número que creas que es:"))

    while user_number!= computer_number:

        
        if abs(computer_number - user_number) == 1:
            print("Demasiado cerca")
        elif user_number > computer_number:
            print("Muy alto")
        elif user_number < computer_number:
            print("Muy bajo")
        

        user_number = int(input("Ingresa el número que creas que es:"))

    print("Felicidades adivinaste")

guessing_game()

