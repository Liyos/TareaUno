cantidad = int(input("Ingrese cantidad a invertir: "))
interes = int(input("ingrese interés anual: "))
años = int(input("Ingrese numero de años: "))
capital = cantidad * (interes / 100 + 1)** años

print("El capital obtenido es de: ", capital)
