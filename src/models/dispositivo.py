
class Dispositivo:
    def __init__(self,id, disNombre, disTipo,disModelo, disSectores, disEstado ) -> None:
        self._id = id
        self._disNombre = disNombre
        self._disTipo = disTipo
        self._disModelo = disModelo
        self._disSectores = disSectores
        self._disEstado = disEstado
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def disNombre(self):
        return self._disNombre

    @disNombre.setter
    def disNombre(self,disNombre):
        self._disNombre = disNombre
    
    @property
    def disTipo(self):
        return self._disTipo 

    @disTipo.setter
    def disTipo(self,disTipo):
        self._disTipo = disTipo
    
    @property
    def disModelo(self):
        return self._disModelo
    
    @disModelo.setter
    def disModelo(self,disModelo):
        self._disModelo = disModelo
    
    @property
    def disSectores(self):
        return self._disSectores
    
    @disSectores.setter
    def disSectores(self, disSectores):
        self._disSectores = disSectores
    
    @property
    def disEstado(self):
        return self._disEstado
    
    @disEstado.setter
    def disEstado(self, disEstado):
        self._disEstado = disEstado
    
    def __str__(self) -> str:
        return f'''
            Id dispositivo: {self._id}, Nombre dispositivo: {self._disNombre} , tipo: {self._disTipo},
            modelo: {self._disNombre}, sectores: {self._disSectores}, Estado : {self._disEstado}
        '''