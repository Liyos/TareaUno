import math

cantidadDinero = int(input("Ingrese cantidad de dinero en cuenta: "))
primeraño = cantidadDinero * (4 / 100 + 1) ** 1
segundoaño = cantidadDinero * (4 / 100 + 1) ** 2
terceraño = cantidadDinero * (4 / 100 + 1) ** 3

print("Cantidad de ahorro en el primer año:", round(primeraño,2))
print("Cantidad de ahorro en el segundo año:", round(segundoaño,2))
print("Cantidad de ahorro en el tercer año:", round(terceraño,2))
