# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-22
# RLAB-23-02-09-0044-2
#

from datetime import date

class Campaña():
    
    def __init__(self, nombre:str, inicio:date, termino:date, anuncios:list):
        self.__nombre = nombre
        self.__fecha_inicio = inicio
        self.__fecha_termino = termino
        self.__anuncios = anuncios
    
    def __in_anuncios(self):
        pass
    
    def getNombre(self):
        return self.__nombre
    
    def getFecha_inicio(self):
        return self.__fecha_inicio
    
    def getFecha_termino(self):
        return self.__fecha_termino
    
    def getAnuncios(self):
        return self.__anuncios
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setFecha_inicio(self, inicio):
        self.__fecha_inicio = inicio
    
    def setFecha_termino(self, termino):
        self.__fecha_termino = termino
    
    def __str__(self) -> str:
        pass