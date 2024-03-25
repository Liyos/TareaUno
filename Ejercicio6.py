import math

precioBarra = 3.49
porcentajeDescuento = 60
descuento = precioBarra * (porcentajeDescuento / 100)
precioDescuento = precioBarra - descuento

cantidadBarras = int(input("Cantidad de barras vendidas: "))

totalVenta= cantidadBarras * precioDescuento

mensaje = f""" 
El precio habitual de una barra de pan es: {precioBarra}
El descuento por no ser del día es: {round(descuento,2)}
El nuevo precio es de: {round(precioDescuento,2)}
El costo total de la venta  es: {round(totalVenta,2)}
"""
print(mensaje)