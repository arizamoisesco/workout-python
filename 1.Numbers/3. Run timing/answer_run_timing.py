def run_timing():

    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input("Ingresa 10 km run time: ")

        if not one_run:
            break

        number_of_runs += 1
        total_time += float(one_run)

    average_time = total_time / number_of_runs

    print(f"Promedio de {average_time}, sobre {number_of_runs} vueltas")

run_timing()