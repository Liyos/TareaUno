n = int(input("Ingresar primer número: "))
m = int(input("Ingresar segundo núemro: "))

c, r = divmod(n, m)

print("La división entre", n, "y", m, "da un cociente de",c, "y un residuo de", r)
