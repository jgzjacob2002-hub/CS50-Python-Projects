meses = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November",
    "December"
]
while True:
    fecha = input("Date: ").strip().title()
    try:
        mes, dia, anyo = fecha.split("/")

        if (0 < int(mes) <= 12) and (0 < int(dia) <= 31):
            print(f"{anyo}-{int(mes):02}-{int(dia):02}")
            break

    except ValueError:
        if "," in fecha:
            try:
                mes1, dia, anyo = fecha.split(" ")
                dia = dia.replace(",", "")
                mes = meses.index(mes1) + 1
                if (0 < int(mes) <= 12) and (0 < int(dia) <= 31):
                    print(f"{anyo}-{int(mes):02}-{int(dia):02}")
                    break
            except ValueError:
                continue
        else:
            continue

