class Evaluacion:
    __dni: int
    __estilo: str
    __puntaje1: float
    __puntaje2: float
    __puntaje3: float

    def __init__(self,dni,estilo,p1,p2,p3) -> None:
        self.__dni = dni
        self.__estilo = estilo
        self.__puntaje1 = p1
        self.__puntaje2 = p2
        self.__puntaje3 = p3
        pass

    def getdni(self):
        return self.__dni
    
    def getestilo(self):
        return self.__estilo
    
    def getpuntajes(self):
        return str(self.__puntaje1) + ' - ' + str(self.__puntaje2) + ' - ' + str(self.__puntaje3)
    
    def getpuntaje1(self):
        return self.__puntaje1
    
    def getpuntaje2(self):
        return self.__puntaje2
    
    def getpuntaje3(self):
        return self.__puntaje3
    
    def calcularpuntaje(self):
        promedio = float((self.getpuntaje1() + self.getpuntaje2() + self.getpuntaje3())/3)
        return promedio

    def __gt__(self,otro):
        return self.calcularpuntaje() > otro
    
    def mostrar(self):
        print('Dni: {}, Estilo: {}, Puntaje 1, 2 y 3: |{}|'.format(self.getdni(),self.getestilo(),self.getpuntajes()))
