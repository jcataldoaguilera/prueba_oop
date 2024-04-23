# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-22
# RLAB-23-02-09-0044-2
#

class Error(Exception):
    pass

class LargoExcedidoError(Error):
    pass

class SubTipoInvalidoError(Error):
    def __init__(self, mensaje, subtipo):
        self.mensaje = mensaje
        self.subtipo = subtipo