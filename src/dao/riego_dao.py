from utilities.cursor_pool import CursorPool
from models.riego import Riego
from utilities.logger_base import log


class RiegoDao:
    '''
    DAO --> Data Access Object
    '''

    _SELELCT = 'SELECT * FROM riego ORDER BY id'
    _INSERT = 'INSERT INTO riego (rie_cantidad_liquido_calandario, rie_cantidad_liquido_aplicada, rie_fecha_inicio, rie_fecha_fin, rie_estado, rei_cantidad_liquido_calculado,rie_sectores, rie_cultivos) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    _UPDATE = 'UPDATE riego SET  rie_cantidad_liquido_calandario=%s, rie_cantidad_liquido_aplicada=%s, rie_fecha_inicio=%s, rie_fecha_fin=%s, rie_estado=%s, rei_cantidad_liquido_calculado=%s, rie_sectores=%s, rie_cultivos=%s  WHERE id=%s'
    _DELETE = 'DELETE FROM riego WHERE id=%s'

    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELELCT)
            registros = cursor.fetchall()
            riegos = []
            for registro in registros:
                riego = Riego(registro[0], registro[1], registro[2], registro[3],
                              registro[4], registro[5], registro[6], registro[7], registro[8])
                riegos.append(riego)
                print(riego)
            return riegos

    @classmethod
    def eliminar(cls, riego):
        with CursorPool() as cursor:
            valores = (riego.id,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'eliminar riego, {riego}')
            return cursor.rowcount

    @classmethod
    def insertar(cls, riego):
        with CursorPool() as cursor:
            valores = (riego.canLiqCalendario, riego.canLiqAplicada, riego.fechaInicio,
                       riego.fechaFinal, riego.estado, riego.canLiqCalculado, riego.sector, riego.cultivo)
            cursor.execute(cls._INSERT, valores)
            log.debug(f'insertar riego, {riego}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, riego):
        with CursorPool() as cursor:
            valores = (riego.canLiqCalendario, riego.canLiqAplicada, riego.fechaInicio, riego.fechaFinal,
                       riego.estado, riego.canLiqCalculado, riego.sector, riego.cultivo, riego.id)
            cursor.execute(cls._UPDATE, valores)
            log.debug(f'actualizar riego, {riego}')
            return cursor.rowcount
