# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-22
# RLAB-23-02-09-0044-2
#

from abc import ABC, abstractmethod
from error import SubTipoInvalidoError


class Anuncio(ABC):
    
    def __init__(self, alto:int, ancho:int, url_archivo:str, url_clic:str, sub_tipo:str ):
        self.__alto = alto if alto > 0 else 1
        self.__ancho = ancho if ancho > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
    
    def getAlto(self):
        return self.__alto
    
    def getAncho(self):
        return self.__ancho
    
    def getUrl_archivo(self):
        return self.__url_archivo
    
    def getUrl_clic(self):
        return self.__url_clic
    
    def getSubtipo(self):
        return self.__sub_tipo
    
    def setAlto(self,alto:int):
        self.__alto = alto if alto > 0 else 1
    
    def setAncho(self,ancho:int):
        self.__alto = ancho if ancho > 0 else 1
    
    def setUrl_archivo(self, url_archivo):
        self.__url_archivo = url_archivo
    
    def setUrl_clic(self, url_clic):
        self.__url_clic = url_clic
    
    def setSubtipo(self, sub_tipo):
        try:
            if (isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS or
            isinstance(self, Display) and sub_tipo not in Display.SUB_TIPOS or
            isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS):
                raise SubTipoInvalidoError("No es un subtipo permitido para la instancia",sub_tipo)
            else:
                self.__sub_tipo = sub_tipo
        except SubTipoInvalidoError as stError:
            print(f"Error {stError.mensaje}", stError.subtipo)

    @staticmethod
    def mostrar_formatos():
        print("FORMATO VIDEO")
        print("==========")
        for v in Video.SUB_TIPOS:
            print(f"-{v}")
        
        print("FORMATO DISPLAY:")
        print("==========")
        for d in Display.SUB_TIPOS:
            print(f"-{d}")

        print("FORMATO SOCIAL:")
        print("==========")
        for s in Social.SUB_TIPOS:
            print(f"-{s}")    
    
    @abstractmethod
    def comprimir_anuncio(self):
        pass
    
    @abstractmethod
    def redimensionar_anuncio(self):
        pass

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    
    def __init__(self, url_archivo: str, url_clic: str, subtipo: str, duracion:int):
        super().__init__(1, 1, url_archivo, url_clic, subtipo)
        self.__duracion = duracion if duracion > 0 else 5
        
    def getDuracion(self):
        return self.__duracion
    
    def setDuracion(self,duracion):
        self.__duracion = duracion if duracion > 0 else 5
    
    def setAlto(self,alto:int):
        pass
    
    def setAncho(self,ancho:int):
        pass
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")