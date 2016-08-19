def cargar_mapa(nombre):
	mapa = open(nombre, "r")
	lineas = []
	for linea in mapa:
		lineas.append(list(linea.strip()))
	return lineas

print(cargar_mapa("mapas/mapa1.txt"))

