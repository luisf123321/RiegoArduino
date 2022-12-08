import serial
import time
arduino = serial.Serial(port = "COM7", baudrate=115200 , timeout=.1)
class ArduinoBase:
    @classmethod
    def lecturaSensorHumedad(cls, request):
        value = cls.read(request)
        print(value)
        return value
    @classmethod
    def read(cls, x):
        arduino.flushOutput()
        arduino.write(bytes(x, "utf-8"))
        data = arduino.readline()
        return data
    
    @classmethod
    def activarValvula(cls,request):
        value = cls.read(request)
        print(value)
        return value

        
