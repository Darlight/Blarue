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
				if self.robot.x == x and self.robot.y == y:
					mapa_completo += self.robot.dibujar()
				elif self.contar_ficha(x, y) > 0:
					mapa_completo += str(self.contar_ficha(x, y))
				else:
					mapa_completo += " "
			mapa_completo += "\n"
		return mapa_completo

	def agregar_ficha(self,ficha):
		self.fichas.append(ficha)

	def quitar_ficha(self):
		for f in range(len(self.fichas)):
			if self.fichas[f].x == self.robot.x and self.fichas[f].y == self.robot.y:
				self.fichas.pop(f)
				break

	def contar_ficha(self, x, y):
		contador = 0
		for ficha in self.fichas:
			if ficha.x == x and ficha.y == y:
				contador += 1
		return contador

	def hay_ficha(self):
		hay = False
		for y in range(self.altura):
			for x in range(self.ancho):
				if self.robot.x == x and self.robot.y == y:
					hay = True
					break
		return hay 

