from src.dao.admin_riego_dao import AdminRiegoDao
from src.models.admin_riego import AdminRiego
from src.models.cultivo import Cultivo
from src.models.sectores import Sector
from src.models.tipo_suelo import TipoSuelo
from src.dao.tipo_suelo_dao import TipoSueloDao
from src.dao.tipo_cultivo_dao import TipoCultivoDao
from src.dao.dispositivo_dao import DispositivoDao
from src.models.dispositivo_medida import DispositivoMedida
from src.dao.dispositivo_medida import DispositivoMedidaDao
import json
from datetime import date
from src.logica.arduino_base import ArduinoBase
from src.logica.logica_riego import LogicaRiego

class LogicaLecturasRiego:
    @classmethod
    def lecturaHumedad(cls):
        with open("src/logica/riego.json") as riego: 
            resultado = json.load(riego)
            print(resultado)
            nodos=resultado["nodos"]
            for n in nodos:
                nodo = n["nodo"]
                sector = n["sector"]
                lectura = dict({"nodo":nodo , "pin":"A0" , "command":"ON"})
                response = ArduinoBase.lecturaSensorHumedad(lectura)
                cls.activacionRiego(response, sector)
    @classmethod
    def activacionRiego(cls, lectura, sector, nodo):
        lectura = json.loads(lectura)
        adminRiego = AdminRiegoDao.buscarSector(sector)
        nap = adminRiego.nad
        if nap >= lectura["value"]:
            tiempo = LogicaRiego.logicaRiego(sector)
            LogicaRiego.activacionRiego(nodo, tiempo)

    @classmethod
    def guardarLecturaHumedad(cls, lectura, sector): 
        dispositivo = DispositivoDao.seleccionarDispositivoSector(sector)
        lectura = json.loads(lectura)
        dispositivo_medida = DispositivoMedida(medida = lectura["value"],fecha = date , dispositivo=dispositivo.id)
        DispositivoMedidaDao.insertar(dispositivo_medida)

    



