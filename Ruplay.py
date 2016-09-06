from robots import Robot
from moneda import Ficha
from mapa import Mapa
import time
from uso_utilidades import cargar_mapa, cargar_instrucciones
mapa = Mapa(25,80)
mapa_eligido = "mapas/mapa1.txt"
uso_de_mapa = cargar_mapa(mapa_eligido)

instrucciones_elegidas = "Instrucciones/instruccion1.txt"
uso_de_instrucciones = cargar_instrucciones(instrucciones_elegidas)

for y in range(mapa.altura):
	for x in range(mapa.ancho):
		if [y][x] == "6"
			ficha = Ficha()
