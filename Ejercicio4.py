cantidadPayasos = int(input("Ingrese la cantidad de payasos del pedido: "))
cantidadMunecas = int(input("Ingrese la cantidad de muñecas del pedido: "))
pesoPayasos = cantidadPayasos * 112
pesoMunecas = cantidadMunecas * 75
pesoTotal = pesoPayasos + pesoMunecas

print("Peso de los payasos:", pesoPayasos)
print("Peso de las muñecas:", pesoMunecas)
print("El peso total del paquete es de", pesoTotal, "gramos.")