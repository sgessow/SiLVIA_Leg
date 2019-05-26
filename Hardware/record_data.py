from multiprocessing import Process, Queue
import read_serial_data
import measure_pos


q=Queue()
arduino = Process(target=read_serial_data.read_serial, args=([q]))
dyna = Process(target=measure_pos.read_pos, args=([q]))
arduino.start()
dyna.start()
arduino.join()
dyna.join()
print(q.get())
