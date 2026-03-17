from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()
lista = figlet.getFonts()

if len(sys.argv) == 1:
    mensaje = input("Input: ").strip()
    aletorio = figlet.setFont(font = choice(lista))
    print(f"Output:\n{figlet.renderText(mensaje)}")

elif len(sys.argv) == 3:
    palabras = ["-f", "--font"]
    if sys.argv[1] in palabras and sys.argv[2] in lista:
        mensaje = input("Input: ").strip()
        figlet.setFont(font = sys.argv[2])
        print(f"Output:\n{figlet.renderText(mensaje)}")

    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

