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
		if self.rotacion >= "UP":
			self.rotacion = 1
		elif self.rotacion = 1:
			return "▲"
		elif self.rotacion = 2:
			return "►"
		elif self.rotacion = 3:
			return "▼"
		elif self.rotacion = 4:
			return "◄"
	
	def recoger_ficha(self):
		if hay_ficha(self.posicion_x, self.posicion_y):
			mapa.recoger_ficha(self.x, self.y)
			self.fichas += 1


	


