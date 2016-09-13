#Niveles o plataformas con diferentes objetivos
def cargar_mapa(nombre):
	mapa = open(nombre, "r")
	lineas = []
	for linea in mapa:
		lineas.append(list(linea.strip()))
	return lineas


#Instrucciones(programa por default para ganar un mapa)
def cargar_instrucciones(nombre):
	instruccion = open(nombre, "r")
	lineas_2 = []
	for linea in instruccion:
		lineas_2.append(linea.strip())
	return lineas_2
#Saca el len de las filas
def sacar_ancho(nombre):
	lista = cargar_mapa(nombre)
	return (len(lista[0]))
#Saca el len de las columnas
def sacar_altura(nombre):
	lista = cargar_mapa(nombre)
	return (len(lista))