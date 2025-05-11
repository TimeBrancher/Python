import math
def Velocidad(g,h):
	return math.sqrt(2*g*h)
def Tiempo(v,h):
	return math.sqrt(v/g)
def Potencial(m,g,h):
	return m * g * h
def Fuerza(m,g):
	return m*g
def Energia_Cinetica(m,v):
	return 0.5*m*(v**2)
def momentum (m,v):
	return m*v
h = float(input("Ingresa la altura desde la que cae el cuerpo: "))
m = float(input("Ingresa la masa del cuerpo: "))
g = 9.8


print("La altura inicial es {}".format(h))
print("La altura final es {}".format(0))
print("La velocidad inicial es {}".format(0))
print("La velocidad final es {}".format(Velocidad(g,h)))
print("La aceleracion es {}".format(g))
print("El tiempo que toma en caer es {}".format(Tiempo(Velocidad(g,h),h)))
print("La distancia recorrida es {}".format(h))
print("La masa del cuerpo es {}".format(m))
print("La energia potencial en un principio es {}".format((Potencial(m,g,h))))
print("La fuerza es {}".format(Fuerza(m,g)))
print("La energia cinetica es {}".format(Energia_Cinetica(m,Velocidad(g,h))))
print("El momentum es {}".format(momentum(m,Velocidad(g,h))))

