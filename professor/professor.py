import random

def main():
    correctas = 0
    level = get_level()

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problemas =  x + y
        intentos = 0

        while intentos < 3:
            try:
                sumas = int(input(f"{str(x)} + {str(y)} = "))
                if problemas == sumas:
                    correctas += 1
                    break
                else:
                    print ("EEE")
                    intentos += 1
                    continue

            except ValueError:
                print ("EEE")
                intentos += 1
                continue

        if intentos == 3:
            print(f"{str(x)} + {str(y)} = {problemas}")

    print(f"Score: {correctas}")

def get_level():
    while True:
        try:
            nivel = int(input("Level: ").strip())
            if 1 <= nivel <= 3:
                return nivel
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()


