from nodo import Nodo

class ListaDoble():
    #ESTA LISTA DOBLE LA IMPLEMENTO COMO UNA COLA
    def __init__(self) :
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia (self):
        return self.primero == None

    def insertarFinal(self, dato):
        if self.vacia():
            self.primero= self.ultimo = Nodo(dato)
        else:
            aux= self.ultimo
            self.ultimo= aux.siguiente = Nodo(dato)
            self.ultimo.anterior= aux
        self.size+=1

    def insertarIncio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux

    def eliminarInicio(self):
        if self.vacia():
            print("Ya no hay pedidos")
        elif self.primero.siguiente == None:
            self.primero= self.ultimo =None
            self.size = 0
        else:
            print("SE ENTREGO EL PEDIDO "+self.primero.dato)
            self.primero= self.primero.siguiente
            self.primero = self.ultimo =  None
            self.size -=1


    def eliminarFinal(self):
        if self.vacia():
            print("Ya no hay pedidos")
        elif self.primero.siguiente == None:
            print("SE ENTREGO EL PEDIDO "+self.ultimo.dato)
            self.primero = self.ultimo = None
            self.size =0
        else:
            print("SE ENTREGO EL PEDIDO "+self.ultimo.dato)
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -=1
   
    def recorrerNormarl(self):
        aux = self.primero
        while aux:
            print("["+aux.dato+"]")
            aux = aux.siguiente

    def recorrerCola(self):
        aux = self.ultimo
        while aux:
            print("["+aux.dato+"]")
            aux = aux.anterior

    def Size(self):
        return self.size