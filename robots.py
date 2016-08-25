from mapa import Mapa
class Robot(object):

	def __init__(self, rotacion, movimiento, pick, posicion_x, posicion_y,mapa,fichas):
		self.rotacion = rotacion
		self.movimiento = movimiento
		self.pick = False
		self.posicion_y = posicion_y
		self.posicion_x = posicion_x
		self.mapa = mapa 
		self.fichas = fichas

	def rotar_posicion(self):
		self.rotacion = 1
		if self.rotacion >= 5:
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


	


