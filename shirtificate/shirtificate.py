from fpdf import FPDF


class PDF():
    def __init__(self, name):
        self._archivo = FPDF()
        self._archivo.add_page()
        self._archivo.set_font("helvetica", "B", 30)
        self._archivo.cell(0, 40, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self._archivo.image("shirtificate.png", w=self._archivo.epw)
        self._archivo.set_font("Times", size=36)
        self._archivo.set_text_color(255, 255, 255)
        ancho_texto = self._archivo.get_string_width(name)
        ancho_pagina = self._archivo.w
        x = (ancho_pagina - ancho_texto)/2

        self._archivo.text(x, y=140, text = name)

    def estrella(self):
        self._archivo.set_line_width(1)
        self._archivo.set_fill_color(r=255, g=255, b=0)
        self._archivo.star(x=105, y=175, r_in=5, r_out=15, rotate_degrees=180, corners=5, style="FD")

    def crear(self, archivo):
        self._archivo.output(archivo)




name = input(("Name: ")).strip() + " took CS50"
pdf = PDF(name)
pdf.estrella()
pdf.crear("shirtificate.pdf")



