#Esta es la parte del main
def main ():
    Emociones = convert(input().strip())
    print(Emociones)

#Esta es la parte de definir la funcion
def convert(Cara2):
    Cara2 = Cara2.replace(":)", "🙂")
    Cara2 = Cara2.replace(":(", "🙁")
    return Cara2



main()
