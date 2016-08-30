▲import Ruplay
class Mapa(object):
	def __init__(self, altura, ancho):
		self.altura = altura
		self.ancho = ancho
		self.fichas = []
		self.robot = None

	def ubicar_robot(self,robot):
		self.robot = robot

	def dibujar(self):
		for y in range(self.altura):
			for x in range(self.ancho):

	def agregar_ficha(self,ficha):
		self.fichas.append(ficha)

