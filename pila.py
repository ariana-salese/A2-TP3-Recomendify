from nodo import _Nodo

class Pila():

	def __init__(self):

		self.tope = None

	def apilar(self,dato):

		nuevotope = _Nodo(dato,self.tope)
		self.tope = nuevotope

	def desapilar(self):

		if self.esta_vacia():
			raise IndexError("La pila está vacía")

		devolver = self.tope.dato
		self.tope = self.tope.prox

		return devolver

	def ver_tope(self):

		if self.esta_vacia():
			raise IndexError("La pila está vacía")

		return self.tope.dato

	def esta_vacia(self):

		if self.tope: 
			return False

		return True

	def eliminar_desordenados(self):

		pila_aux = Pila()

		while not self.esta_vacia():

			elemento = self.desapilar()
			#print(f"prox num es {elemento}")
			while (not pila_aux.esta_vacia()) and elemento > pila_aux.ver_tope():
				#print(f"desapilo {pila_aux.ver_tope()}")
				pila_aux.desapilar()

			#print(f"apilo {elemento}")
			pila_aux.apilar(elemento)

		while not pila_aux.esta_vacia():
			self.apilar(pila_aux.desapilar())



