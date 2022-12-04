#import serial
#import time
from src.logica.logica1 import logica

logica.calcular_lrn()
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




