from src.logica.logica_calculo_riego import LogicaCalculoRiego
from src.logica.arduino_base import ArduinoBase
import time
class LogicaRiego:
    @classmethod
    def logicaRiego(cls, sector):
        lrn = LogicaCalculoRiego.calcular_lrn(sector)
        lrb = LogicaCalculoRiego.calcular_lrb(lrn, sector)
        lrb_etapa = LogicaCalculoRiego.calcular_lrb_etapa(lrb, sector)
        tiempo_riego = LogicaCalculoRiego.tiempo_riego(lrb_etapa, sector)
        return tiempo_riego
    @classmethod
    def activacionRiego(cls, nodo, tiempo_riego):
        activar = dict({"nodo":nodo , "pin":"D8" , "command":"ON"})
        response = ArduinoBase.activarValvula(activar)
        time.sleep(tiempo_riego)
        desactivar = dict({"nodo":nodo , "pin":"D8" , "command":"OFF"})
        desresponse = ArduinoBase.activarValvula(desactivar)
    