from mapa import Mapa
class Robot(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.fichas = 0
		self.rotacion = 0
		self.mapa = None

	def rotar(self):
		self.rotacion = (self.rotacion + 1 ) % 4

	def dibujar(self):
		if self.rotacion == 0:
			return "^"

		elif self.rotacion == 1:
			return ">"

		if self.rotacion == 2:
			return "v"

		else:
			return "<"

	def colocar_en_mapa(self,mapa):
		self.mapa = mapa

	def recoger_fichas(self,x ,y ):



