from multiprocessing import Queue
import serial
import time


def read_serial(Q,duration=5, port='/dev/ttyACM0', baudrate=9600):
    with serial.Serial(port, baudrate, timeout=1) as ser:
        # read up to ten bytes (timeout)
        start_time=time.time()
        cur_time=start_time
        while cur_time-start_time<duration:
            line_out=[]
            cur_time=time.time()
            line = ser.readline()
            #print(line)
            try:
                #Add time to line
                line_out.append("A")
                line_out.append(cur_time)
                num_line=float(line)
                #Add Force Data to line
                line_out.append(num_line)
                # Todo Add electrical current values to line
                Q.put(line_out)
            except ValueError:
                pass
    ser.close()
    return True
