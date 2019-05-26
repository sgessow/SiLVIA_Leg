from multiprocessing import Queue
import serial
import time


def read_serial(Q,duration=5, port='/dev/ttyACM0', baudrate=9600):
    Data=[]
    with serial.Serial(port, baudrate, timeout=1) as ser:
        # read up to ten bytes (timeout)
        start_time=time.time()
        cur_time=start_time
        while cur_time-start_time<duration:
            cur_time=time.time()
            line = ser.readline()
            #print(line)
            try:
                num_line=float(line)
                Data.append(num_line)
            except ValueError:
                Data.append(line)
    Q.put(Data)
    return True
