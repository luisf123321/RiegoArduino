

from pickle import NONE


class TipoCultivo:
    def __init__(self,id=None, nombre=None, variedad=None, referencia=None, total=None, inicial=None, desarrollo = None,maduracion=None,final=None ) -> None:
        self._id = id
        self._nombre = nombre
        self._variedad = variedad
        self._referencia  = referencia
        self._total = total
        self._inicial = inicial
        self._desarrollo = desarrollo
        self._maduracion = maduracion
        self._final = final

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
    def variedad(self):
        return self._variedad
    
    @variedad.setter
    def variedad(self,variedad):
        self._variedad = variedad
    
    @property
    def referencia(self):
        return self._referencia
    
    @referencia.setter
    def referencia(self, referencia):
        self._referencia = referencia
    
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self, total):
        self._total = total

    @property
    def inicial(self):
        return self._inicial    
    
    @inicial.setter
    def inicial(self, inicial):
        self._inicial = inicial

    @property
    def desarrollo(self):
        return self._desarrollo

    @desarrollo.setter
    def desarrollo(self, desarrollo):
        self._desarrollo = desarrollo
    
    @property
    def maduracion(self):
        return self._maduracion
    
    @maduracion.setter
    def maduracion(self, maduracion):
        self._maduracion = maduracion
    
    @property
    def final(self):
        return self._final
    
    @final.setter
    def final(self, final):
        self._final = final

    def __str__(self) -> str:
        return f'''
            Id tipo cultivo: {self._id}, nombre: {self._nombre} , variedad : {self._variedad},
            referencia: {self._referencia}
        '''