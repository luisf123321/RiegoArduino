from src.dao.admin_riego_dao import AdminRiegoDao
from src.models.admin_riego import AdminRiego
from src.models.cultivo import Cultivo
from src.models.sectores import Sector
from src.models.tipo_suelo import TipoSuelo
from src.dao.tipo_suelo_dao import TipoSueloDao

class logica:
    @classmethod
    def calcular_lrn(cls):
        #IHD*Pr*NAP
        #IHD medios segun tipo de suelo
        #Pr segun la edad del cultivo
        #NAP % de humedad permitido
        sector = AdminRiego.sector
        tipo_suelo = TipoSueloDao.seleccionarTodos()
        for n in tipo_suelo:
            print(n.id,n.nombre)

        tiposuelo= TipoSueloDao.seleccionarTipoSuelo(1)
        print(tiposuelo.nombre, tiposuelo.cp)
        """pmp = TipoSuelo.pmp
        cp = TipoSuelo.cp
        ihd = pmp - cp
        
        nap = AdminRiego.nad
        lrn = ihd * nap """


        