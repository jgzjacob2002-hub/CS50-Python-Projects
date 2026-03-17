while True:
    try:
        fraction = input("Fraction: ").split("/")
        x = int(fraction[0])
        y = int(fraction[1])
        division = round((x / y)*100)
        if not 0 <= division <= 100:
            continue
        elif 99 <= division <= 100:
            print("F")
            break
        elif 0 <= division <= 1:
            print("E")
            break
        else:
            print(f"{division}%")
            break


    except ZeroDivisionError:
        continue

    except ValueError:
        continue


