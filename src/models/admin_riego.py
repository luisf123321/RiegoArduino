

from bdb import effective


class AdminRiego:
    def __init__(self,id=None,tipoRiego=None,nad=None,efectividad=None,caudal=None,distancia=None, radio=None,sector=None) -> None:
        self._id = id
        self._tipoRiego = tipoRiego
        self._nad = nad
        self._efectividad = efectividad
        self._caudal = caudal
        self._distancia = distancia
        self._radio = radio
        self._sector = sector


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,id):
        self._id = id

    @property
    def tipoRiego(self):
        return self._tipoRiego

    @tipoRiego.setter
    def tipoRiego(self,tipoRiego):
        self._tipoRiego = tipoRiego

    @property
    def nad(self):
        return self._nad

    @nad.setter
    def nad(self, nad):
        self._nad = nad

    @property
    def efectividad(self):
        return self._efectividad
    
    @efectividad.setter
    def efectividad(self, efectividad):
        self._efectividad = efectividad
    
    @property
    def caudal(self):
        return self._caudal
    
    @caudal.setter
    def caudal(self, caudal):
        self._caudal = caudal
    
    @property
    def distancia(self):
        return self._distancia
    
    @distancia.setter
    def distancia(self, distancia):
        self._distancia = distancia
    
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, radio):
        self._radio = radio
    
    @property
    def sector(self):
        return self._sector
    
    @sector.setter
    def sector(self, sector):
        self._sector = sector
    

    def __str__(self) -> str:
        return f'''
            Id admin_riego: {self._id}, Tipo riego: {self._tipoRiego} , nad: {self._nad}, sector:{self._sector}
            Efectividad: {self._efectividad}, caudal: {self._caudal}, distancia: {self._distancia}, radio : {self._radio}
        '''