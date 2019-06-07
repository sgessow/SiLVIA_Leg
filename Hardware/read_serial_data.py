from multiprocessing import Lock
import serial
import time
import ctypes

def read_serial(shared_val,duration=5, port='/dev/ttyACM0', baudrate=115200):
    lock=Lock()
    start_time = time.time()
    cur_time = start_time
    with serial.Serial(port, baudrate, timeout=None) as ser:
        # read up to ten bytes (timeout)
        ser.setDTR(True)
        while cur_time-start_time<duration:
            line_out=[]
            cur_time=time.time()
            line = str(ser.readline())[2:-5]
            line_out.append(cur_time)
            try:
                line_read = [float(x) for x in line.split(' ')]
                line_out=line_out+line_read
                if len(line_out)==6:
                    with lock:
                        for i in range(6):
                            shared_val[i] = line_out[i]
            except ValueError:
                pass
    ser.close()
    return True
