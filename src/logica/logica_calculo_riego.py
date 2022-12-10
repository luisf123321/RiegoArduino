from src.dao.admin_riego_dao import AdminRiegoDao
from src.models.admin_riego import AdminRiego
from src.models.cultivo import Cultivo
from src.dao.cultivo_dao import CultivoDao
from src.models.sectores import Sector
from src.dao.sectores_dao import SectoresDao
from src.models.tipo_suelo import TipoSuelo
from src.dao.tipo_suelo_dao import TipoSueloDao
from src.dao.tipo_cultivo_dao import TipoCultivoDao
from datetime import datetime

class LogicaCalculoRiego:
    @classmethod
    def calcular_lrn(cls, sector):
        sector = SectoresDao.seleccionarById(sector)
        tiposuelo= TipoSueloDao.seleccionarTipoSuelo(sector.suelo)
        print(tiposuelo.nombre, tiposuelo.cp)
        cp = tiposuelo.cp
        pmp = tiposuelo.pmp
        ihd = cp-pmp
        print("indice de humedad disponible", ihd)

        adminRiego = AdminRiegoDao.buscarSector(sector.id)
        nap = adminRiego.nad
        print(adminRiego.sector,adminRiego.nad)
        
        lrn = ihd * nap 
        print("lamina de riego neta: ", lrn)
        return lrn

    @classmethod
    def calcular_lrb(cls, lrn, sector):
        adminriego = AdminRiegoDao.buscarSector(sector)
        eficiencia = adminriego.efectividad
        lrb = (lrn/eficiencia)*100
        return lrb

    @classmethod
    def calcular_lrb_etapa(cls, lrb, sector):
        sector = SectoresDao.seleccionarById(sector)
        cultivodao = CultivoDao.buscarPorId(sector.cultivo)
        etapa_inicial = cultivodao.fechaInicio
        etapa_desarrollo = cultivodao.fechaDesarrollo
        etapa_maduracion = cultivodao.fechaMaduracion
        etapa_final= cultivodao.fechaFinal
        lrb_etapa = 0
        if datetime.now() < etapa_inicial:
            lrb_etapa = lrb
        elif datetime.now() < etapa_desarrollo:
            lrb_etapa = lrb + (lrb*0.23)
        elif datetime.now() < etapa_maduracion:
            lrb_etapa = lrb + (lrb*0.53) 
        elif datetime.now() < etapa_final:
            lrb_etapa = lrb + (lrb*0.23)
        return lrb_etapa

    @classmethod
    def tiempo_riego(cls, lrb_etapa, sector):
        adminriego = AdminRiegoDao.buscarSector(sector)
        distancia = adminriego.distancia
        distancia_laterales = adminriego.radio
        num_emisores = 1/(distancia*distancia_laterales)
        caudal_emisor = adminriego.caudal
        tiempo_riego = (lrb_etapa/caudal_emisor)*(1/num_emisores)*60
        return tiempo_riego





        