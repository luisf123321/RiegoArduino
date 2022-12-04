
class DispositivoMedida:
    def __init__(self,id, medida, fecha, dispositivo) -> None:
        self._id = id
        self._medida = medida
        self._fecha = fecha
        self._dispositivo = dispositivo
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def medida(self):
        return self._medida
    
    @medida.setter
    def medida(self,medida):
        self._medida = medida

    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self,fecha):
        self._fecha = fecha
    
    @property
    def dispositivo(self):
        return self._dispositivo
    
    @dispositivo.setter
    def dispositivo(self,dispositivo):
        self._dispositivo = dispositivo
    
    def __str__(self) -> str:
        return f'''
            Id dispositivo medida: {self._id}, medida: {self._medida} ,
            fecha: {self._fecha}, dispositivo: {self._dispositivo}
        '''