import sys
#sys.path.append("C:\\Users\\LUISFERNANDO\\Documents\\proyecto-code\\RiegoFlask")

from src.utilities.cursor_pool import CursorPool
from src.models.cultivo import Cultivo
from src.utilities.logger_base import log
import json
import datetime
class CultivoDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM cultivo ORDER BY id'
    _SELECT_BY_USER = 'SELECT * FROM cultivo WHERE cul_user=%s '
    _SELECT_BY_ID = 'SELECT * FROM cultivo WHERE id=%s '
    _INSERT = 'INSERT INTO cultivo (cul_nombre, cul_tipo_cul, cul_fecha_inicio, cul_fecha_final, cul_estado,cul_user, cul_fecha_desarrollo, cul_fecha_maduracion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    _UPDATE = 'UPDATE cultivo SET  cul_nombre=%s, cul_tipo_cul=%s, cul_fecha_inicio=%s, cul_fecha_final=%s, cul_estado=%s,cul_user=%s, cul_fecha_desarrollo=%s, cul_fecha_maduracion=%s WHERE id=%s'
    _DELETE = 'DELETE FROM cultivo WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            cultivos = []
            for registro in registros:
                cultivo = Cultivo(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
                cultivos.append(cultivo)
            return cultivos
    
    @classmethod
    def buscarPorUsuario(cls,cultivo):
        with CursorPool() as cursor:
            valores = (cultivo.user,)
            cursor.execute(cls._SELECT_BY_USER,valores)
            registros = cursor.fetchall()
            if registros is None or registros == []:
                return None
            else:
                cultivos = []
                for registro in registros:
                    fecha_inicio = registro[3]
                    fecha_inicio = fecha_inicio.strftime('%Y-%m-%d')   
                    fecha_fin = registro[4]
                    fecha_fin=fecha_fin.strftime('%Y-%m-%d')
                    fecha_desarrollo = registro[7]
                    fecha_desarrollo=fecha_desarrollo.strftime('%Y-%m-%d') 
                    fecha_maduracion = registro[8]  
                    fecha_maduracion=fecha_maduracion.strftime('%Y-%m-%d')         
                    cultivo = Cultivo(registro[0], registro[1], registro[2], fecha_inicio, fecha_fin, registro[5], registro[6],fecha_desarrollo,fecha_maduracion)
                    cultivos.append(cultivo)
                return cultivos
    
    @classmethod
    def buscarPorId(cls,cultivo):
        with CursorPool() as cursor:
            valores = (cultivo.id,)
            cursor.execute(cls._SELECT_BY_ID,valores)
            registro = cursor.fetchone()
            if registro is None:
                return None
            else:
                #fecha_inicio = registro[3]
                #fecha_inicio = fecha_inicio.strftime('%Y-%m-%d')   
                #fecha_fin = registro[4]
                #fecha_fin=fecha_fin.strftime('%Y-%m-%d') 
                #fecha_desarrollo = registro[7]
                #fecha_desarrollo=fecha_desarrollo.strftime('%Y-%m-%d') 
                #fecha_maduracion = registro[8]  
                #fecha_maduracion=fecha_maduracion.strftime('%Y-%m-%d')     
                cultivo = Cultivo(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6],registro[7],registro[8],registro[9])
                return cultivo
               
    
    @classmethod
    def eliminar(cls, cultivo):
        with CursorPool() as cursor:
            valores = (cultivo.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar cultivo, {cultivo}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,cultivo):
        with CursorPool() as cursor:
            valores = (cultivo.cultivoNombre, cultivo.tipoCultivo,cultivo.fechaInicio,
            cultivo.fechaFinal,cultivo.cultivoEstado,cultivo.user, 
            cultivo.fechaDesarrollo,cultivo.fechaMaduracion )
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar cultivo, {cultivo}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, cultivo):
        with CursorPool() as cursor:
            valores = (cultivo.cultivoNombre, cultivo.tipoCultivo,
            cultivo.fechaInicio,cultivo.fechaFinal,cultivo.cultivoEstado,
            cultivo.user,cultivo.fechaDesarrollo,cultivo.fechaMaduracion,cultivo.id )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar cultivo, {cultivo}')
            return cursor.rowcount