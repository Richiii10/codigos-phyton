def rec_area (altura, ancho):
    area = altura * ancho
    return area

alto = float(input("ingrese el largo: "))
ancho = float(input("ingrese el ancho: "))

print(f"su area es: {round(rec_area(alto,ancho))}")