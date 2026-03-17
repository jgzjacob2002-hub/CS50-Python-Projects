def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
#Primera parte todo expecto el loop para detectar medios numeros
    if not(s[0:2].isalpha()):
        return False

    if not(2 <= len(s) <= 6):
        return False

    if not(s.isalnum()):
        return False

#Para que si se detcte un numeor sea al final y sin letras de por medio
    rep = 0
    x = len(s)-1

    while rep < x:
        if s[rep].isnumeric():
            if not s[rep:].isdigit():
                return False
            elif (s[rep] == "0"):
                return False
            else:
                return True
        rep = rep + 1

    return True


main()
