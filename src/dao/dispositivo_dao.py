
from utilities.cursor_pool import CursorPool
from models.dispositivo import Dispositivo
from utilities.logger_base import log

class DispositivoDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM dispositivo ORDER BY id'
    _INSERT = 'INSERT INTO dispositivo (dis_nombre, dis_tipo, dis_modelo, dis_sectores, dis_estado) VALUES (%s,%s,%s,%s,%s)'
    _UPDATE = 'UPDATE dispositivo SET  dis_nombre=%s, dis_tipo=%s, dis_modelo=%s, dis_sectores=%s, dis_estado=%s WHERE id=%s'
    _DELETE = 'DELETE FROM dispositivo WHERE id=%s'
    _SELELCT_SECTOR_ESTADO = 'SELECT * FROM dispositivo WHERE dis_sector=%s AND dis_estado=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            dispositivos = []
            for registro in registros:
                dispositivo = Dispositivo(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                dispositivos.append(dispositivo)
                print(registro)
            return dispositivos
    
    @classmethod
    def eliminar(cls, dispositivo):
        with CursorPool() as cursor:
            valores = (dispositivo.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar dispositivo, {dispositivo}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,dispositivo):
        with CursorPool() as cursor:
            valores = (dispositivo.disNombre, dispositivo.disTipo, dispositivo.disModelo,dispositivo.disSectores,dispositivo.disEstado )
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar dispositivo, {dispositivo}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, dispositivo):
        with CursorPool() as cursor:
            valores = (dispositivo.disNombre, dispositivo.disTipo, dispositivo.disModelo,dispositivo.disSectores,dispositivo.disEstado,dispositivo.id )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar dispositivo, {dispositivo}')
            return cursor.rowcount

    @classmethod
    def seleccionarDispositivoSector(cls, sector):
        with CursorPool() as cursor:
            valores = (sector,1)
            cursor.execute(cls._SELELCT_SECTOR_ESTADO,valores)
            registro = cursor.fetchone()
            
            if registro is not None:
                dispositivo = Dispositivo(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                print(registro)
                return dispositivo
            else:
                return None

