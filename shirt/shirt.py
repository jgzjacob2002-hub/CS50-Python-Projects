import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    try:
        images = []
        extension = [".jpg", ".png", ".jpeg"]

        response = sys.argv[1]
        sender = sys.argv[2]
        dividido1 = os.path.splitext(response)
        dividido2 = os.path.splitext(sender)
        res = dividido1[1]
        sen = dividido2[1]

        if not res in extension or not sen in extension:
            sys.exit("Invalid input")

        if res.lower() != sen.lower():
            sys.exit("Input and output have different extensions")
#Donde vas a SHIRT abierta
        shirt = Image.open("shirt.png")
        size = shirt.size
#Abres sys1 y lo guardas en im y haces las acciones
        with Image.open(response) as im:
#Manda la imagen y la recorta a la medida deseada
            before = ImageOps.fit(im, size)
#Siendo before nuestra anterior imagen, esta se va a unir con la imagen y la mascara de la imagen (shirt,shirt)
            before.paste(shirt, shirt)
#Lo salvas en sender o sys2
        before.save(sender)

    except FileNotFoundError:
        sys.exit("File does not exist")
