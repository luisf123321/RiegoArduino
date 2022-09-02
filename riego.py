import serial
import time
import threading

#consejodefacultad.ingenieria

ser = serial.Serial('COM9', 115200, timeout=1)  # open serial port
print(ser.name)         # check which port was really used

print("--- start ---")

aplicaciones = [{"id":1,"cantidad":1300},
                {"id":2,"cantidad":300},
                {"id":3,"cantidad":700}]

sectores = [{"id":1,"cantidad":1300},
            {"id":2,"cantidad":300},
            {"id":3,"cantidad":700}]

# https://realpython.com/intro-to-python-threading/

#def riego(quantity, onInterval, offInterval):
def riego(_id, cantidad):
    
    if _id == 1:
        print("start ", _id)
        ser.write(b'A')
        time.sleep(cantidad/100)
        ser.write(b'B')
        print("end ", _id)
        
        
    if _id == 2:
        print("start ", _id)
        ser.write(b'D')
        time.sleep(cantidad/100)
        ser.write(b'E')
        print("end ", _id)
        
    if _id == 3:
        print("start ", _id)
        ser.write(b'G')
        time.sleep(cantidad/100)
        ser.write(b'H')
        print("end ", _id)
        

def regar():
    for sector in sectores: 
        _id = sector["id"]
        cantidad = sector["cantidad"]
        x = threading.Thread(target=riego, args=(_id, cantidad))
        print("Main    : before running thread")
        x.start()
        print("Main    : wait for the thread to finish")
        # x.join()
        print("Main    : all done")
    
    

# for i in range(5):
#     ser.write(b'B')     # write a string  
#     ser.write(b'D')     # write a string  
#     ser.write(b'F')     # write a string  
#     time.sleep(2)
    
#     ser.write(b'A')     # write a string
#     ser.write(b'C')     # write a string
#     ser.write(b'E')     # write a string
#     time.sleep(2)
    
#     s = ser.read(10)
#     print("read:", s)
    
# print("--- end ---")

regar()

ser.close()