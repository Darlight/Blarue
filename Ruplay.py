from robots import Robot
from moneda import Ficha
from mapa import Mapa
import time
from uso_utilidades import cargar_mapa, cargar_instrucciones, sacar_ancho, sacar_altura
mapa_eligido = "mapas/mapa1.txt"

mi_mapa = Mapa(sacar_ancho(mapa_eligido),sacar_altura(mapa_eligido))

uso_de_mapa = cargar_mapa(mapa_eligido)

instrucciones_elegidas = "Instrucciones/instruccion1.txt"
uso_de_instrucciones = cargar_instrucciones(instrucciones_elegidas)

for y in range(mi_mapa.altura):
	for x in range(mi_mapa.ancho):
		if uso_de_mapa[y][x] == "*":
			mi_robot = Robot(x,y)
			mi_mapa.ubicar_robot(mi_robot)
			mi_robot.colocar_en_mapa(mi_mapa)
		else:
			cantidad_fichas = int(uso_de_mapa[y][x])
			for i in range(cantidad_fichas):
				ficha = Ficha(x,y)
				mi_mapa.agregar_ficha(ficha)

for i in uso_de_instrucciones:
	if i == "ROTATE":
		mi_robot.rotar()
	elif i == "MOVE":
		mi_robot.mover()
	elif i == "PICK":
		mi_robot.recoger_fichas()
		mi_mapa.quitar_ficha()
	time.sleep(0.5)
	print(mi_mapa.dibujar())
	





