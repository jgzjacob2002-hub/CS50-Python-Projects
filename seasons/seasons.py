from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    fecha = cumpleanos(input("Date of Birth: "))
    print(fecha)


def cumpleanos(s):
    try:
        estilo = date.fromisoformat(s)
        hoy = date.today()
        dias = hoy - estilo
        minutos = 24 * 60 * dias.days
        palabras = p.number_to_words(minutos, andword = "")
        return f"{palabras.capitalize()} minutes"

    except ValueError:
        sys.exit("Invalid date")




if __name__ == "__main__":
    main()
    def estrella(self):
        self.set_line_width(1)
        self.set_fill_color(r=255, g=255, b=0)
        self.star(x=105, y=175, r_in=5, r_out=15, rotate_degrees=180, corners=5, style="FD")
