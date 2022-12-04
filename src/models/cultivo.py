

class Cultivo:
    def __init__(self, id=None, cultivoNombre=None, tipoCultivo=None,
                 fechaInicio=None, fechaFinal=None,
                 cultivoEstado=None, user=None,
                 fechaDesarrollo=None, fechaMaduracion=None, fechaSiembra=None) -> None:
        self._id = id
        self._cultivoNombre = cultivoNombre
        self._tipoCultivo = tipoCultivo
        self._fechaInicio = fechaInicio
        self._fechaFinal = fechaFinal
        self._cultivoEstado = cultivoEstado
        self._user = user
        self._fechaDesarrollo = fechaDesarrollo
        self._fechaMaduracion = fechaMaduracion
        self._fechaSiembra = fechaSiembra

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def cultivoNombre(self):
        return self._cultivoNombre

    @cultivoNombre.setter
    def cultivoNombre(self, cultivoNombre):
        self._cultivoNombre = cultivoNombre

    @property
    def tipoCultivo(self):
        return self._tipoCultivo

    @tipoCultivo.setter
    def tipoCultivo(self, tipoCultivo):
        self._tipoCultivo = tipoCultivo

    @property
    def fechaInicio(self):
        return self._fechaInicio

    @fechaInicio.setter
    def fechaInicio(self, fechaInicio):
        self._fechaInicio = fechaInicio

    @property
    def fechaFinal(self):
        return self._fechaFinal

    @fechaFinal.setter
    def fechaFinal(self, fechaFinal):
        self._fechaFinal = fechaFinal

    @property
    def cultivoEstado(self):
        return self._cultivoEstado

    @cultivoEstado.setter
    def cultivoEstado(self, estado):
        self._cultivoEstado = estado

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def fechaDesarrollo(self):
        return self._fechaDesarrollo
    
    @fechaDesarrollo.setter
    def fechaDesarrollo(self, fechaDesarrollo):
        self._fechaDesarrollo = fechaDesarrollo
    
    @property
    def fechaMaduracion(self):
        return self._fechaMaduracion
    
    @fechaMaduracion.setter
    def fechaMaduracion(self, fechaMaduracion):
        self._fechaMaduracion = fechaMaduracion
    
    @property
    def fechaSiembra(self):
        return self._fechaSiembra
    
    @fechaSiembra.setter
    def fechaSiembra(self, fechaSiembra):
        self._fechaSiembra = fechaSiembra

    def __str__(self) -> str:
        return f'''
            Id cultivo: {self._id}, Nombre cultivo: {self._cultivoNombre} , 
            tipo cultivo: {self._tipoCultivo}, Fecha inicio: {self._fechaInicio}, fecha final: {self._fechaFinal}, Estado : {self._cultivoEstado}
        '''
