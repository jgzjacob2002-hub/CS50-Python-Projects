import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    try:
        pizzas = []

        response = sys.argv[1]
        if not response.endswith(".csv"):
            sys.exit("Not a CSV file")
        with open(response) as file:
            reader = csv.DictReader(file)
            for fila in reader:
                pizzas.append(fila)
        print(tabulate(pizzas, headers = "keys", tablefmt = "grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")
