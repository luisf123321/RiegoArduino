

class Finca:
    def __init__(self,id=None,nombre=None,direccion=None, latitud=None,longitud=None, altitud=None, usuario=None) -> None:
        self._id = id
        self._nombre = nombre
        self._direccion = direccion
        self._latidud = latitud
        self._longitud = longitud
        self._altitud = altitud
        self._usuario = usuario
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion
    
    @property
    def latitud(self):
        return self._latidud
    
    @latitud.setter
    def latitud(self, latitud):
        self._latidud = latitud
    
    @property
    def longitud(self):
        return self._longitud
    
    @longitud.setter
    def longitud(self, longitud):
        self._longitud = longitud

    @property
    def altitud(self):
        return self._altitud
    
    @altitud.setter
    def altitud(self,altitud):
        self._altitud = altitud
    
    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario
    
    def __str__(self) -> str:
        return f'''
            Id finca: {self._id}, nombre: {self._nombre} , direccion : {self._direccion},
            altitud: {self._altitud}, longitud: {self._longitud}, latitud: {self._latidud}, usuario: {self._usuario}
        '''
