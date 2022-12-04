#import psycopg2 as db
#poner punto antes de logger
from .logger_base import log
import sys
from psycopg2 import pool


class Conexion:
    _DATABASE = 'onryyemf'
    _USERNAME = 'onryyemf'
    _PASSWORD = 'vAiidLCoyYoIjo8ii9xqQNwLrIply_1H'
    _PORT = '5432'
    _HOST = 'batyr.db.elephantsql.com'
    _MIN_CON = 1
    _MAX_CON = 3
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON, 
                    cls._MAX_CON, 
                    host=cls._HOST, 
                    user=cls._USERNAME, 
                    password=cls._PASSWORD, 
                    port=cls._PORT, 
                    database=cls._DATABASE)
                #log.debug(f'conexion exitosa, {cls._pool}')
                return cls._pool
            except Exception as ex:
                log.error(f'error al obtener pool, {ex}')
                #sys.exit()
        else:
            return cls._pool


    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        #log.debug(f'obtener conexion, {conexion}')
        return conexion

    @classmethod
    def liberarConecion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        #log.debug(f'regresar conecion al pool')

    @classmethod
    def cerrarPool(cls):
        cls.obtenerPool().closeall()


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConecion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    Conexion.cerrarPool()



