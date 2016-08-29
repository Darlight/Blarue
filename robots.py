from mapa import Mapa
class Robot(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.fichas = 0
		self.rotacion = "UP"
		self.mapa = None

	def mover_robot(self, pasos):
		pass

	def colocar_en_mapa(self, mapa):
		self.mapa = mapa

	def rotar_posicion(self):
		if self.rotacion = "UP":
			return "^"
		elif self.rotacion = "RIGHT":
			return ">"
		elif self.rotacion = "DOWN":
			return "v"
		elif self.rotacion = "LEFT":
			return "<"
	
	def recoger_ficha(self):
		pass


	


