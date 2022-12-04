

from src.utilities.cursor_pool import CursorPool
from src.models.tipo_suelo import TipoSuelo
from src.utilities.logger_base import log

class TipoSueloDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM tipo_suelo ORDER BY id'
    _INSERT = 'INSERT INTO tipo_suelo (tip_sue_nombre, tip_sue_velocidad_infiltracion, tip_sue_punto_marchitez, tip_sue_capacidad_campo) VALUES (%s,%s,%s,%s)'
    _UPDATE = 'UPDATE tipo_suelo SET  tip_sue_nombre=%s, tip_sue_velocidad_infiltracion=%s, tip_sue_punto_marchitez=%s, tip_sue_capacidad_campo=%s WHERE id=%s'
    _DELETE = 'DELETE FROM tipo_suelo WHERE id=%s'
    _SELECT_BY_ID = 'SELECT * FROM tipo_suelo WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            tiposSuelos = []
            for registro in registros:
                tipoSuelo = TipoSuelo(registro[0], registro[1], registro[2], registro[3], registro[4])
                tiposSuelos.append(tipoSuelo)
                print(tipoSuelo)
            return tiposSuelos
    
    @classmethod
    def seleccionarTipoSuelo(cls, id):
        with CursorPool() as cursor:
            valores = (id,)
            cursor.execute(cls._SELECT_BY_ID, valores)
            registro = cursor.fetchone()
            if registro is None:
                return None
            else:    
                tipo_suelo = TipoSuelo(registro[0], registro[1], registro[2], registro[3], registro[4])
                return tipo_suelo
        
    @classmethod
    def insertar(cls,tipoSuelo):
        with CursorPool() as cursor:
            valores = (tipoSuelo.nombre, tipoSuelo.velovidad, tipoSuelo.pmp,tipoSuelo.cp )
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar tipo suelo, {tipoSuelo}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, tipoSuelo):
        with CursorPool() as cursor:
            valores = (tipoSuelo.nombre, tipoSuelo.velovidad, tipoSuelo.pmp,tipoSuelo.cp , tipoSuelo.id)
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar tipo suelo, {tipoSuelo}')
            return cursor.rowcount