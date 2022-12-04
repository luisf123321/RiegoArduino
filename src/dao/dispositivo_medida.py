from utilities.cursor_pool import CursorPool
from models.dispositivo_medida import DispositivoMedida
from utilities.logger_base import log

class DispositivoMedidaDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM dispositivo_medida ORDER BY id'
    _INSERT = 'INSERT INTO dispositivo_medida (dis_med_fecha, dis_med_medicion, dis_med_dispositivos) VALUES (%s,%s,%s)'
    _UPDATE = 'UPDATE dispositivo_medida SET  dis_med_fecha=%s, dis_med_medicion=%s, dis_med_dispositivos=%s WHERE id=%s'
    _DELETE = 'DELETE FROM dispositivo_medida WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            dispositivosMedidas = []
            for registro in registros:
                dispositivoMedida = DispositivoMedida(registro[0], registro[1], registro[2], registro[3])
                dispositivosMedidas.append(dispositivoMedida)
                print(dispositivoMedida)
            return dispositivosMedidas
    
    @classmethod
    def eliminar(cls, dispositivoMedida):
        with CursorPool() as cursor:
            valores = (dispositivoMedida.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar dispositivo medida, {dispositivoMedida}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,dispositivoMedida):
        with CursorPool() as cursor:
            valores = (dispositivoMedida.medida, dispositivoMedida.fecha, dispositivoMedida.dispositivo)
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar dispositivo medida, {dispositivoMedida}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, dispositivoMedida):
        with CursorPool() as cursor:
            valores = (dispositivoMedida.medida, dispositivoMedida.fecha, dispositivoMedida.dispositivo, dispositivoMedida.id)
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar dispositivo medida, {dispositivoMedida}')
            return cursor.rowcount