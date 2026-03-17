import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    try:
        students = []

        response = sys.argv[1]
        sender = sys.argv[2]

        if not response.endswith(".csv") and not sender.endswith(".csv") :
            sys.exit("Not a CSV file")
        with open(response, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                surname, name = row["name"].split(",")
                name = name.strip()
                surname = surname.strip()
                students.append({"first": name, "last": surname, "casa": row["house"]})

        with open(sender, "w") as f:
            writer = csv.DictWriter(f, fieldnames = ["first", "last", "house"])
            writer.writeheader()

            for student in students:
                writer.writerow({"first": student["first"], "last": student["last"], "house": student["casa"]})


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")



