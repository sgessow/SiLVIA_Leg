import os
import glob
import csv
import SiLVIA_Leg.Util.make_trajectory as trajectory


for filename in glob.glob('16Volts Adjusting Spring/*.csv'):
    print(filename)
    data=[]
    with open(filename) as readFile:
        reader = csv.reader(readFile,delimiter=',')
        for row in reader:
            coord=trajectory.calculate_coordinates([[float(row[5]),float(row[6])]])
            new_row=row+coord[0]
            data.append(new_row)
    with open(filename,'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(data)