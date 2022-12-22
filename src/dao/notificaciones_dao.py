from src.utilities.cursor_pool import CursorPool
from src.models.notificaciones import Notificaciones
from src.utilities.logger_base import log
import json

class NotificacionesDao:
    _SELELCT = 'SELECT * FROM notificaciones ORDER BY id'
    _INSERT = 'INSERT INTO notificaciones (usuario, mensaje, estado, fecha_origen ) VALUES (%s,%s,%s,%s)'


    @classmethod
    def insertar(cls,notificaciones):
        with CursorPool() as cursor:
            valores = (notificaciones.usuario, notificaciones.mensaje, notificaciones.estado,notificaciones.fechaOrigen)
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar notificacion, {notificaciones}')
            return cursor.rowcount
    