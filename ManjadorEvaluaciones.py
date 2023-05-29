from Evaluaciones import Evaluacion
import csv
class ManejaEvaluaciones:
    __lista: list
    def __init__(self) -> None:
        self.__lista = []
        pass

    def initme(self):
        with open('evaluacion.csv', 'r', encoding='utf8') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                dni = int(fila[0])
                estilo = str(fila[1])
                puntaje1 = float(fila[2])
                puntaje2 = float(fila[3])
                puntaje3 = float(fila[4])
                evaluacion = Evaluacion(dni,estilo,puntaje1,puntaje2,puntaje3)
                self.agregarevaluacion(evaluacion)
    
    def agregarevaluacion(self,evaluacion):
        self.__lista.append(evaluacion)

    def test(self):
        for e in range(len(self.__lista)):
            self.__lista[e].mostrar()

    def Aa(self,mf):
        estilo = str(input('Ingrese estilo:'))
        edad = int(input('Ingrese edad:'))
        print('\n')
        i = 0
        while i < len(self.__lista):
            if estilo == self.__lista[i].getestilo():
                dni = self.__lista[i].getdni()
                mf.buscarpatinador(dni,edad)
                i+=1
            else: i+=1

    def Ab(self,mf):
        self.__lista.sort(reverse=True)
        self.test()
        print('\n')
        print('Patinador:')
        dni = self.__lista[0].getdni()
        mf.buscarpordni(dni)
        prom = self.__lista[0].calcularpuntaje()
        print('Mejor puntaje: {:.2}' .format(prom))
        
    def Ac(self,mf):
        i = 0
        a = 0
        while i < len(self.__lista):
            if self.__lista[i].getestilo() == 'E':
                dni = self.__lista[i].getdni()
                while a < len(self.__lista):
                    if self.__lista[a].getestilo() == 'L' and dni == self.__lista[a].getdni():
                        print('Patinador que participo en estilo Libre y en estilo Escuela:')
                        mf.buscarpordni(dni)
                        i+=1
                        a=len(self.__lista)
                    else: a+=1
                a = 0
            else: i+=1
                
    def Ad(self):
        dni = int(input('Ingrese dni:'))
        estilo = str(input('Ingrese estilo:'))
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].getdni() == dni and self.__lista[i].getestilo() == estilo:
                puntajes = self.__lista[i].getpuntajes()
                print('Puntajes: |{}|'.format(puntajes))
                i = len(self.__lista)
            else: i+=1


