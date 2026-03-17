groceries = {}
lista = []
while True:
    try:
        cosas = input().strip().upper()
        lista.append(cosas)

    except EOFError:
        lista.sort()
        for palabras in lista:
            if palabras in groceries:
                groceries[palabras] += 1
            else:
                groceries[palabras] = 1

        for imprimir in groceries:
            print(f"{groceries[imprimir]} {imprimir}")


        exit()

