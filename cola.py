class _Nodo():

	def __init__(self,dato,prox = None):
		self.dato = dato
		self.prox = prox

	def __str__(self):

		return str(self.dato)

class Cola():

	def __init__(self):

		self.frente = None
		self.ultimo = None

	def encolar(self,dato):

		nuevonodo = _Nodo(dato)

		if self.esta_vacia():		
			self.frente = nuevonodo
			self.ultimo = nuevonodo
			return

		self.ultimo.prox = nuevonodo
		self.ultimo = nuevonodo

	def desencolar(self):

		if self.esta_vacia():
			raise IndexError("La cola esta vacia")

		devolver = self.frente.dato
		self.frente = self.frente.prox

		if not self.frente:
			self.ultimo = None

		return devolver

	def ver_frente(self):

		if self.esta_vacia():
			raise IndexError("La cola esta vacia")

		return self.frente.dato

	def esta_vacia(self):

		if not self.frente and not self.ultimo:
			return True
		return False