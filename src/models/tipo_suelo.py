

class TipoSuelo:
    def __init__(self, id, nombre,velocidad ,pmp,cp) -> None:
        self._id = id
        self._nombre = nombre
        self._velocidad = velocidad
        self._pmp = pmp
        self._cp = cp
    
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
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad
    
    @property
    def pmp(self):
        return self._pmp
    
    @pmp.setter
    def pmp(self,pmp):
        self._pmp = pmp
    
    @property
    def cp(self):
        return self._cp
    
    @cp.setter
    def cp(self,cp):
        self._cp = cp
    
    def __str__(self) -> str:
        return f'''
            Id tipo suelo: {self._id}, nombre: {self._nombre} , velocidad : {self._velocidad} ,
            punto marchites: {self._pmp}, capacidad de campo: {self._cp} 
        '''