def run_timing(minutes_list):
    #print(f"Introduzca el tiempo de carrera de 10 km: {minutes:.2f}")
    total_minutes = len(minutes_list)
    average = sum(minutes_list)/ total_minutes
    return average

one_run = input(f"Introduzca el tiempo de carrera de 10 km: ")
minutes_list = []

while one_run:

    minutes_list.append(float(one_run))
    one_run = input(f"Introduzca el tiempo de carrera de 10 km: ")

final_average = run_timing(minutes_list)

print(f"El promedio total es de: {final_average:.1f}, sobre {len(minutes_list)} vueltas")



