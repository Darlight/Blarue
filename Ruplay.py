#Niveles o plataformas con diferentes objetivos
def cargar_mapa(nombre):
	mapa = open(nombre, "r")
	lineas = []
	for linea in mapa:
		lineas.append(list(linea.strip()))
	for i in range(len(lineas)):
		espacios = " "
		lineas [i][i]
		espacios += lineas[i][i]
	return espacios


print(cargar_mapa("mapas/mapa1.txt"))

#Instrucciones(programa por default para ganar un mapa)
def cargar_instrucciones(nombre):
	instruccion = open(nombre, "r")
	lineas_2 = []
	for linea in instruccion:
		lineas_2.append(linea.strip())
	return lineas_2

print(cargar_instrucciones("Instrucciones/instruccion1.txt"))

