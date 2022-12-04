

class Riego:
    def __init__(self, id, canLiqCalendario, canLiqAplicada, fechaInicio, fechaFinal, estado, canLiqCalculado, sector,cultivo) -> None:
        self._id = id
        self._cultivo = cultivo
        self._sector = sector
        self._canLiqCalculado = canLiqCalculado
        self._canLiqCalendario = canLiqCalendario
        self._canLiqAplicada = canLiqAplicada
        self._fechaInicio = fechaInicio
        self._fechaFinal = fechaFinal
        self._estado = estado

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def cultivo(self):
        return self._cultivo
    
    @cultivo.setter
    def cultivo(self, cultivo):
        self._cultivo = cultivo
    
    @property
    def sector(self):
        return self.sector
    
    @sector.setter
    def sector(self,sector):
        self._sector = sector
    
    @property
    def canLiqCalculado(self):
        return self._canLiqCalculado
    
    @canLiqCalculado.setter
    def canLiqCalculado(self,canLiqCalculado):
        self._canLiqCalculado = canLiqCalculado
    
    @property
    def canLiqAplicada(self):
        return self._canLiqAplicada
    
    @canLiqAplicada.setter
    def canLiqAplicada(self,canLiqAplicada):
        self._canLiqAplicada = canLiqAplicada
    
    @property
    def canLiqCalendario(self):
        return self._canLiqCalendario
    
    @canLiqCalendario.setter
    def canLiqCalendario(self, canLiqCalendario):
        self._canLiqCalendario = canLiqCalendario
    
    @property
    def fechaInicio(self):
        return self._fechaInicio
    
    @fechaInicio.setter
    def fechaInicio(self,fechaInicio):
        self._fechaInicio = fechaInicio
    
    @property
    def fechaFinal(self):
        return self._fechaFinal

    @fechaFinal.setter
    def fechaFinal(self,fechaFinal):
        self._fechaFinal = fechaFinal
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self,estado):
        self._estado = estado
    
    def __str__(self) -> str:
        return f'''
            Id riego: {self._id}, canLiqCalendario: {self._canLiqCalendario} , canLiqCalculado : {self._canLiqCalculado}           
        '''