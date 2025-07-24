import random

def guessing_game():
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input("What is your guess?"))

        if user_guess == answer:
            print(f"Correcto la respuesta es {user_guess}")
            break

        if user_guess < answer:
            print(f"Tu respuesta {user_guess} es muy baja")

        else:
            print(f"Tu repsuesta {user_guess} es muy alta")

guessing_game()