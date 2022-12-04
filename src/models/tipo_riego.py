

class TipoRiego:
    def __init__(self, id = None, nombre=None, efectividad=None,description=None) -> None:
        self._id = id
        self._nombre = nombre
        self._efectividad = efectividad
        self._description = description

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,id):
        self._id = id

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def descripcion(self):
        return self._description

    @descripcion.setter
    def descripcion(self, description):
        self._description = description 
    
    @property
    def efectividad(self):
        return self._efectividad
    
    @efectividad.setter
    def efectividad(self, efectividad):
        self._efectividad = efectividad
    
    def __str__(self) -> str:
        return f'''
            Id : {self._id}, nombre: {self._nombre} , descripcion : {self._description}, efectividad: {self._efectividad}       
        '''