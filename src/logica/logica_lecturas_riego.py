from src.dao.admin_riego_dao import AdminRiegoDao
from src.dao.dispositivo_dao import DispositivoDao
from src.models.dispositivo_medida import DispositivoMedida
from src.dao.dispositivo_medida import DispositivoMedidaDao
from src.dao.sectores_dao import SectoresDao
import json
from datetime import date
from src.logica.arduino_base import ArduinoBase
from src.logica.logica_riego import LogicaRiego
from src.dao.finca_dao import FincaDao
from src.dao.notificaciones_dao import NotificacionesDao
from src.models.notificaciones import Notificaciones
from datetime import datetime
class LogicaLecturasRiego:
    @classmethod
    def lecturaHumedad(cls):        
        with open("src/logica/riego.json") as riego: 
            resultado = json.load(riego)
            print(resultado)
            print(resultado['finca'])
            finca = FincaDao.buscarFincaPorId(resultado['finca'])
            if finca is not None :
                sectores = SectoresDao.seleccionarByFinca(finca)
                if sectores is not None:
                    for sec in sectores:
                        lectura = dict({"nodo":sec.nodo , "pin":"A0" , "command":"ON"})
                        response = ArduinoBase.lecturaSensorHumedad(lectura)
                        cls.activacionRiego(response, sec,finca)
                        cls.guardarLecturaHumedad(lectura=lectura,sector=sec)
                else:
                    message = "no se encontraron sectores asociados a la finca con el id = " +  resultado['finca']
                    notificacion = Notificaciones(usuario=finca.usuario, mensaje=message,estado=False, fechaOrigen=datetime.now())                   
                    NotificacionesDao.insertar(notificacion)
            else:
                message = "no se encontro la finca con el id = " +  resultado['finca']       

            
            """
            nodos=resultado["nodos"]
            for n in nodos:
                nodo = n["nodo"]
                sector = n["sector"]
                lectura = dict({"nodo":nodo , "pin":"A0" , "command":"ON"})
                response = ArduinoBase.lecturaSensorHumedad(lectura)
                cls.activacionRiego(response, sector)
            """
    @classmethod
    def activacionRiego(cls, lectura, sector, finca):
        lectura = json.loads(lectura)
        adminRiego = AdminRiegoDao.buscarSector(sector.id)
        nap = adminRiego.nad
        if nap >= lectura["value"]:
            tiempo = LogicaRiego.logicaRiego(sector)
            LogicaRiego.activacionRiego(sector.nodo, tiempo)
            message = "Se ha realizado la activacion del riego en el sector " +  sector.nombre + " de la finca " + finca.nombre + "durante "+ tiempo + " minutos"
            notificacion = Notificaciones(usuario=finca.usuario, mensaje=message,estado=False, fechaOrigen=datetime.now())                   
            NotificacionesDao.insertar(notificacion)

    @classmethod
    def guardarLecturaHumedad(cls, lectura, sector): 
        dispositivo = DispositivoDao.seleccionarDispositivoSector(sector)
        lectura = json.loads(lectura)
        dispositivo_medida = DispositivoMedida(medida = lectura["value"],fecha = date , dispositivo=dispositivo.id)
        DispositivoMedidaDao.insertar(dispositivo_medida)

    



