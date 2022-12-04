from src.utilities.cursor_pool import CursorPool
from src.models.admin_riego import AdminRiego
from src.utilities.logger_base import log
import json


class AdminRiegoDao:


    _SELELCT = 'SELECT * FROM admin_riego ORDER BY id'  
    _SELELCT_BY_SECTOR = 'SELECT * FROM admin_riego WHERE sector=%s'    
    _INSERT = 'INSERT INTO admin_riego (admin_tipo_riego, admin_nad, admin_efectividad, admin_caudal, admin_distancia, admin_radio,sector) VALUES (%(int)s,%(float)s,%(float)s,%(float)s,%(float)s,%(float)s,%(int)s)'
    _UPDATE = 'UPDATE admin_riego SET  admin_tipo_riego=%s, admin_nad=%s, admin_efectividad=%s, admin_caudal=%s, admin_distancia=%s, admin_radio=%s, sector=%s WHERE id=%s'
    _DELETE = 'DELETE FROM admin_riego WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            adminRiegos = []
            for registro in registros:
                adminRiego = AdminRiego(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7])
                adminRiegos.append(adminRiego)
                print(registro)
            return adminRiegos
    
    @classmethod
    def buscarSector(cls,sector):
        with CursorPool() as cursor:
            valores = (sector,)
            cursor.execute(cls._SELELCT_BY_SECTOR,valores)
            registro = cursor.fetchone()
            if registro is None or registro == []:
                return None
            else:
                adminRiego = AdminRiego(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7])
                print(adminRiego)
                return adminRiego
    
    @classmethod
    def eliminar(cls, adminRiego):
        with CursorPool() as cursor:
            valores = (adminRiego.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar adminRiego, {adminRiego}')
            return cursor.rowcount
    
    @classmethod
    def insertar(cls,adminRiego):
        with CursorPool() as cursor:
            valores = (adminRiego.tipoRiego, adminRiego.nad,adminRiego.efectividad,adminRiego.caudal,adminRiego.distancia, adminRiego.radio,adminRiego.sector )
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar adminRiego, {adminRiego}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, adminRiego):
        with CursorPool() as cursor:
            valores = (adminRiego.tipoRiego, adminRiego.nad,adminRiego.efectividad,adminRiego.caudal,adminRiego.distancia, adminRiego.radio,adminRiego.sector, adminRiego.id )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar adminRiego, {adminRiego}')
            return cursor.rowcount