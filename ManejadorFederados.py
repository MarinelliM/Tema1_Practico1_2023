import csv
from Federados import Federado
class ManejaFederados:
    __lista: list
    def __init__(self) -> None:
        self.__lista = []
        pass

    def initmf(self):
        with open('federados.csv', 'r', encoding='utf8') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                apellido = str(fila[0])
                nombre = str(fila[1])
                dni = int(fila[2])
                edad = int(fila[3])
                club = str(fila[4])
                federado = Federado(apellido,nombre,dni,edad,club)
                self.agregarfederado(federado)
    
    def agregarfederado(self,federado):
        self.__lista.append(federado)

    def test(self):
        for e in range(len(self.__lista)):
            self.__lista[e].mostrar()

    def buscarpatinador(self,dni,edad):
        for e in range(len(self.__lista)):
            if dni == self.__lista[e].getdni() and edad == self.__lista[e].getedad():
                print('Patinadora:')
                self.__lista[e].mostrar()

    def mostrar(self,dni):
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].getdni() == dni:
                return self.__lista[i].mostrar()
            else: i += 1

    def buscarpordni(self,dni):
        e = 0
        while e < len(self.__lista):
            if dni == self.__lista[e].getdni():
                self.__lista[e].mostrar()
                e = len(self.__lista)
            else: e+=1
