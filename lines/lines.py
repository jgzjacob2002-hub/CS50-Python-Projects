import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    try:
        lineas = 0
        response = sys.argv[1]
        if not response.endswith(".py"):
            sys.exit("Not a Python file")

        with open(response, "r") as file:
            lines = file.readlines()

        for numero in lines:
            if numero.lstrip().startswith("#"):
                continue
            elif numero.isspace():
                continue
            lineas += 1

        print(lineas)


    except FileNotFoundError:
        sys.exit("File does not exist")
