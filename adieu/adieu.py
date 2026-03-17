import inflect
p = inflect.engine()

names = []

while True:
    try:
        nombre = input("Name: ").strip()
        names.append(nombre)
        juntos = p.join(names, conj = "and")

    except EOFError:
        print(f"\nAdieu, adieu, to {juntos}")
        exit()
