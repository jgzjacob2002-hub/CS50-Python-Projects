def main ():
    Emociones = convert(input().strip())
    print(Emociones)


def convert(Cara2):
    Cara2 = Cara2.replace(":)", "🙂")
    Cara2 = Cara2.replace(":(", "🙁")
    return Cara2



main()
