def pedir_edad():
    while True:
        try:
            edad = int(input("ingrese su edad: "))
            return edad
        except:
            print("ERROR. introduce un numero valido")

def verif_mayoria_edad(edad):
    if edad >= 18:
        print("eres mayor de edad")
    else:
        print("eres menor de edad")
        
def main():
    edad = pedir_edad()
    verif_mayoria_edad(edad)

main()