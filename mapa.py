class Mapa(object):
	def __init__(self, ancho, altura):
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
				if ficha.x == x and ficha.y == y:
					mapa_completo += ficha
				elif robot.x == x and robot.y == y:
					mapa_completo += "^"
				else:
					mapa_completo += " "
			mapa_completo += "\n"
		return mapa_completo

	def agregar_ficha(self,ficha):
		self.fichas.append(ficha)

	def quitar_ficha(self,x,y):
		for f in fichas:
			if ficha.x == self.x and ficha.y == self.y:
				self.fichas.pop(ficha)
				break

	def contar_ficha(self, x, y):
		contador = 0
		for f in ficha:
			if ficha.x == x and ficha.y == y:
				contador += ficha
		return contador

	def hay_ficha(self,x,y):
		hay = False
		for y in range(self.altura):
			for x in range(self.ancho):
				if self.x == x and self.y == y:
					hay = True
					break
		return hay 

