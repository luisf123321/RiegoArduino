

class Sector:
    def __init__(self, id, nombre, area, lote, latitud, longitud, altitud,  suelo,cultivo) -> None:
        self._id = id
        self._nombre = nombre
        self._area = area
        self._latidud = latitud
        self._longitud = longitud
        self._altitud = altitud
        self._lote = lote
        self._suelo = suelo
        self._cultivo = cultivo
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def nombre(self):
        return self.nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
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
    def area(self):
        return self._area

    @area.setter
    def area(self,area):
        self._area = area
    
    @property
    def lote(self):
        return self._lote
    
    @lote.setter
    def lote(self,lote):
        self._lote = lote
    
    @property
    def suelo(self):
        return self._suelo
    
    @suelo.setter
    def suelo(self, suelo):
        self._suelo = suelo
    
    @property
    def cultivo(self):
        return self._cultivo
    
    @cultivo.setter
    def cultivo(self,cultivo):
        self._cultivo = cultivo
    
    def __str__(self) -> str:
        return f'''
            Id sector: {self._id}, nombre: {self._nombre} , suelo : {self._suelo},
            altitud: {self._altitud}, longitud: {self._longitud}, latitud: {self._latidud}, area: {self._area}
        '''