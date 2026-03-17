import csv
import statistics
from tabulate import tabulate
import sys

def main():
    try:
        event = int(input("Select an event, please just write the number that's before the event \n1 50 freestyle \n2 100 freestyle \n3 200 freestyle \n4 400 freestyle \n5 800 freestyle \n6 1500 freestyle \n7 Exit \n"))
        if event == 7:
            sys.exit("Thank you for use this app")
        while event > 7:
             event = int(input("Please selecta number beetween 1 and 7\n").strip())
    except ValueError:
        while True:
            try:
                event = int(input("This is not a number, please try again\n"))
                break
            except ValueError:
                pass
    try:
        print("\n¿What do you want to do? \n1 Ranking \n2 Statistics \n3 Find a swimmer\n4 Exit")
        operacion = int(input("Please select a number\n").strip())
    except ValueError:
        while True:
            try:
                operacion = int(input("This is not a number, please try again\n"))
                break
            except ValueError:
                pass

    prueba = function_4(event)

    while operacion > 4:
        operacion = int(input("Please just select a number between 1 and 4\n").strip())

    if operacion == 1:
        print(tabulate(function_1(prueba), headers = ["Place", "Name", "Time", "Country"], tablefmt = "grid"))

    if operacion == 2:
        print(function_2(prueba))

    if operacion == 3:
        while True:
            try:
                name = str(input("¿What's the name of the swimmer that you would like to search?\n").strip().title())
                break
            except ValueError:
                print("This is not a string, please try to write a name")

        print(function_3(prueba, name))

    if operacion == 4:
            sys.exit("Thank you for use this app")

def function_1(prueba):
    swimmers = []
    lista = []
    with open(prueba) as file:
        reader = csv.DictReader(file)
        for row in reader:
            time = row["time"].strip()
            name = row["name"].strip()
            country = row["country"].strip()
            if ":" in time:
                minutes, seconds = time.split(":")
                time_changed = float(minutes)*60 + (float(seconds))
            else:
                time_changed = float(time)

            swimmers.append({
                "name": name,
                "time": time,
                "time_seconds": time_changed,
                "country": country
                })

    sorted_swimmers = sorted(swimmers, key=lambda time: time["time_seconds"])

    for list, swimmers in enumerate(sorted_swimmers, start=1):
         lista.append([list, swimmers["name"], swimmers["time"], swimmers["country"]])

    return lista


def function_2(prueba):
    tiempos = []
    swimmers = []
    with open(prueba) as file:
        reader = csv.DictReader(file)
        for row in reader:
            time = row["time"].strip()
            name = row["name"].strip()
            if ":" in time:
                minutes, seconds = time.split(":")
                time_changed = float(minutes)*60 + (float(seconds))
            else:
                time_changed = float(time)

            swimmers.append({
                "name": name,
                "time_seconds": time_changed
                })

    sorted_swimmers = sorted(swimmers, key=lambda time: time["time_seconds"])

    mejor = sorted_swimmers[0]
    peor = sorted_swimmers[-1]

    for i in swimmers:
        tiempos.append(i["time_seconds"])
    promedio = statistics.mean(tiempos)
    mediana = statistics.median(tiempos)

    entero = int(promedio / 60)
    sobrante = float(promedio % 60)

    entero2 = int(mediana / 60)
    sobrante2 = float(mediana % 60)

    if entero > 0:
        promedio = f"{entero}:{sobrante:05.2f}"
    else:
        promedio = f"{sobrante:.2f}"

    if entero2 > 0:
        mediana = f"{entero2}:{sobrante2:05.2f}"
    else:
        mediana = f"{sobrante2:.2f}"

    return f"Best Time: {mejor['name']}\nWorst Time: {peor['name']}\nAverage: {promedio}\nMedian: {mediana}"


def function_3(prueba, name):

    with open(prueba) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if name == row ["name"]:
                return f"This is {row['name']}, the time of your swimmer was {row['time']} and is from {row['country']}"

        else:
            while True:
                print("Your swimmer is not in this list, please try another name")
                try2 = input("Swimmer: ").strip().title()

                with open(prueba) as file2:
                    reader2 = csv.DictReader(file2)
                    for row in reader2:
                        if try2 == row ["name"]:
                            return f"This is {row['name']}, the time of your swimmer was {row['time']} and is from {row['country']}"


def function_4(event):
    if event == 1:
        prueba = "swimmers_50_free.csv"
        return prueba

    elif event == 2:
        prueba = "swimmers_100_free.csv"
        return prueba

    elif event == 3:
        prueba = "swimmers_200_free.csv"
        return prueba

    elif event == 4:
        prueba = "swimmers_400_free.csv"
        return prueba

    elif event == 5:
        prueba = "swimmers_800_free.csv"
        return prueba

    elif event == 6:
        prueba = "swimmers_1500_free.csv"
        return prueba


if __name__ == "__main__":
    main()
