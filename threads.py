import serial
import logging
import threading
import time
import os


serialPort = serial.Serial(port = "COM3", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

serialString = ""

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


# set global variable flag
flag = 1
eofStr = "eof\r\n"
def list_ports():
    global flag
    while flag==1:
        # Wait until there is data waiting in the serial buffer
        if(serialPort.in_waiting > 0):

            # Read data out of the buffer until a carraige return / new line is found
            serialString = serialPort.readline()


            if (serialString.decode('UTF-8') == "eof\r\n"):
                os.system("clear")
            else:
                # Print the contents of the serial data
                print(serialString.decode('UTF-8')[0:-1])
             
            
                
        
def get_input():
    global flag
    keystrk=input('Press a key \n')
    # thread doesn't continue until key is pressed
    print('You pressed: ', keystrk)
    flag=False
    print('flag is now:', flag)

n=threading.Thread(target=list_ports)
i=threading.Thread(target=get_input)
n.start()
i.start()   