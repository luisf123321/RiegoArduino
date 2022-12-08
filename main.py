#import serial
#import time
#from logica.logica_calculo_riego import logica
from src.logica.logica_lecturas_riego import LogicaLecturasRiego

#logica.calcular_lrn()
LogicaLecturasRiego.lecturaHumedad()
"""
arduino = serial.Serial(port = "COM7", baudrate=115200 , timeout=.1)
def read(x):
    arduino.flushOutput()
    arduino.write(bytes(x, "utf-8"))
    data = arduino.readline()
    return data

while True:
    text = '{"nodo":2,"pin":"D8", "command":"ON"}'
    value = read(text)
    print(value)
    time.sleep(10)

    text = '{"nodo":2,"pin":"D8", "command":"OFF"}'
    value = read(text)
    print(value)
    time.sleep(10) """




