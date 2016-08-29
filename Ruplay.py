#Niveles o plataformas con diferentes objetivos
def cargar_mapa(nombre):
	mapa = open(nombre, "r")
	lineas = []
	construccion_de_mapa = ""
	for linea in mapa:
		lineas.append(list(linea))
	for i in range(len(lineas)):
		for j in range(len(lineas[i])):
			if lineas[i][j] == "*":
				construccion_de_mapa += "^"
			elif lineas[i][j] == "0":
				construccion_de_mapa += " "
			elif lineas [i][j] == "\n":
				construccion_de_mapa += "\n"
			else:
				construccion_de_mapa += lineas[i][j]
				
	return construccion_de_mapa





print(cargar_mapa("mapas/mapa1.txt"))

#Instrucciones(programa por default para ganar un mapa)
def cargar_instrucciones(nombre):
	instruccion = open(nombre, "r")
	lineas_2 = []
	for linea in instruccion:
		lineas_2.append(linea.strip())
	return lineas_2

print(cargar_instrucciones("Instrucciones/instruccion1.txt"))

