
def main():
        numero = convert(input("Fraction: "))
        comparacion = gauge(numero)
        print(comparacion)

def convert(fraction):
        try:
            uno, dos = fraction.split("/")
            x = int(uno)
            y = int(dos)
            division = round((x / y)*100)
            if not 0 <= division <= 100:
                raise ValueError
            return division

        except (ZeroDivisionError, ValueError):
            raise


def gauge(porventage):
    if 99 <= porventage <= 100:
        return "F"
    elif 0 <= porventage <= 1:
        return "E"
    else:
        return (f"{porventage}%")

if __name__ == "__main__":
    main()
