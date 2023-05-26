class Federado:
    __apellido: str
    __nombre: str
    __DNI: int
    __edad: int
    __club_que_representa: str

    def __init__(self,apellido,nombre,dni,edad,club) -> None:
        self.__apellido = apellido
        self.__nombre = nombre
        self.__DNI = dni
        self.__edad = edad
        self.__club_que_representa = club
        pass

    def getedad(self):
        return self.__edad
    
    def getnombrecompleto(self):
        return self.__apellido+ ' ' +self.__nombre
    
    def getdni(self):
        return self.__DNI
    
    def getclub(self):
        return self.__club_que_representa
    
    def mostrar(self):
        return print('Apellido y Nombre: {}, Edad: {}, Dni: {}, Club que representa: {}' .format(self.getnombrecompleto(),self.getedad(),self.getdni(),self.getclub()))
    
