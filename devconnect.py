import serial
import sys
import glob

import logging
import threading
import time
import os



# set global variable flag
exit_flag = False
com_semaphore = False
readings = [0] *6
def read_port(serialPort):
    i = 0
    global exit_flag
    while exit_flag==False:
        # Wait until there is data waiting in the serial buffer
        try:
            if(serialPort.in_waiting > 0):

                # Read data out of the buffer until a carraige return / new line is found
                serialString = serialPort.readline()


                if (serialString.decode('UTF-8') == ">eof\r\n"):
                    os.system("clear")
                    com_semaphore = False
                    i=0
                elif (serialString.decode('UTF-8') == ">txf\r\n"):
                    print("Data Recieved:")
                    com_semaphore = True
                else:
                    # Print the contents of the serial data
                    readings[i]=serialString.decode('UTF-8')[4:-2]
                    i += 1
                    print(serialString.decode('UTF-8')[0:-1])
        except:
            print("Connection Lost")
            return


# forces readings thread to return
def exit_app():
    global exit_flag
    exit_flag=True
    print('Exiting now', exit_flag)





def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result




def connect(port):
    try:
        serialPort = serial.Serial(port = port, baudrate=115200,
                                bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        print("Connection Succesful")
        return serialPort
    except:
        print("No port was found")
        return serialPort




if __name__ == '__main__':
    # ports = serial_ports()
    # print(ports)
    serialPort = connect('COM3')

    n=threading.Thread(target=read_port, args=(serialPort,))
    # i=threading.Thread(target=get_input)
    n.start()
    # i.start()