▲import Ruplay
import robots
import moneda
class Mapa(object):
	def __init__(self, altura, ancho):
		self.altura = altura
		self.ancho = ancho
		self.fichas = []
		self.robot = None

	def ubicar_robot(self,robot):
		self.robot = robot

	def dibujar(self):
		mapa_completo = ""
		for y in range(self.altura):
			for x in range(self.ancho):
				if moneda.x == x and moneda.y == y:
					mapa_completo += moneda
				elif robot.x == x and robot.y == y:
					mapa_completo += robot
				else:
					mapa_completo += " "
			mapa_completo += "\n"
		return mapa_completo


	def agregar_ficha(self,ficha):
		self.fichas.append(ficha)
		if ficha.x == robot.x and ficha.y == robot.y:
			
			return 

	def quitar_ficha(self,x,y):
		if 
