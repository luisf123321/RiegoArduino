

from src.utilities.cursor_pool import CursorPool
from src.models.tipo_cultivo import TipoCultivo
from src.utilities.logger_base import log
import json
class TipoCultivoDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM tipo_cultivo ORDER BY id'
    _INSERT = 'INSERT INTO tipo_cultivo (tip_cul_nombre, tip_cul_variedad, tip_cul_referencia) VALUES (%s,%s,%s)'
    _UPDATE = 'UPDATE tipo_cultivo SET  tip_cul_nombre=%s, tip_cul_variedad=%s, tip_cul_referencia=%s WHERE id=%s'
    _DELETE = 'DELETE FROM tipo_cultivo WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            tipoCultivos = []
            if registros is None or registros == []:
                return None
            else:
                print(registros)
                for registro in registros:
                    tipoCultivo = TipoCultivo(registro[0], registro[1], registro[2], registro[3],registro[4], registro[5], registro[6], registro[7], registro[8])
                    tipoCultivos.append(tipoCultivo)
                return tipoCultivos
    
    @classmethod
    def eliminar(cls, tipoCultivo):
        with CursorPool() as cursor:
            valores = (tipoCultivo.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar tipo cultivo, {tipoCultivo}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,tipoCultivo):
        with CursorPool() as cursor:
            valores = (tipoCultivo.nombre, tipoCultivo.variedad, tipoCultivo.referencia )
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar tipo cultivo, {tipoCultivo}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, tipoCultivo):
        with CursorPool() as cursor:
            valores = (tipoCultivo.nombre, tipoCultivo.variedad, tipoCultivo.referencia, tipoCultivo.id )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar tipo cultivo, {tipoCultivo}')
            return cursor.rowcount