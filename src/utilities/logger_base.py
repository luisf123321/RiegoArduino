import logging as log


log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('riego_crud.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje nivel debug')
    log.info('Mensaje nivel info')
    log.warning('Mensaje nivel warning')
    log.error('Mensaje nivel error')
    log.critical('Mensaje nivel critico')