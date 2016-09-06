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

	def recoger_fichas(self, x ,y ):
		if self.mapa.hay_ficha():
			self.fichas += 1

	def mover(self):
		if self.rotacion == 0:
			self.y -= 1
			if self.y < 0:
				self.y = 0
		elif self.rotacion == 1:
			self.x += 1
			if self.x > 79:
				self.x = 79
		elif self.rotacion == 2:
			self.y += 1
			if self.y > 24:
				self.y = 24
		elif self.rotacion == 3:
			self.x -= 1 
			if self.x < 0:
				self.x = 0


 


