from src.utilities.cursor_pool import CursorPool
from src.models.tipo_riego import TipoRiego
from src.utilities.logger_base import log
import json


class TipoRiegoDao:


    _SELELCT = 'SELECT * FROM tipo_riego ORDER BY id'    
    _INSERT = 'INSERT INTO tipo_riego (nombre, efectividad, descripcion) VALUES (%(str)s,%(int)s,%(str)s)'
    _UPDATE = 'UPDATE tipo_riego SET  nombre=%s, efectividad=%s, descripcion=%s WHERE id=%s'
    _DELETE = 'DELETE FROM tipo_riego WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            tiposRiego = []
            for registro in registros:
                tipoRiego = TipoRiego(registro[0], registro[1], registro[2], registro[3])
                tipoRiego = json.dumps(tipoRiego.__dict__)
                tiposRiego.append(tipoRiego)
                print(registro)
            return tiposRiego
    
    
    
    @classmethod
    def eliminar(cls, tipoRiego):
        with CursorPool() as cursor:
            valores = (tipoRiego.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar tipoRiego, {tipoRiego}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,tipoRiego):
        with CursorPool() as cursor:
            valores = (tipoRiego.nombre, tipoRiego.efectividad,tipoRiego.descripcion )
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar tipoRiego, {tipoRiego}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, tipoRiego):
        with CursorPool() as cursor:
            valores = (tipoRiego.nombre, tipoRiego.efectividad,tipoRiego.descripcion,tipoRiego.id )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar tipoRiego, {tipoRiego}')
            return cursor.rowcount