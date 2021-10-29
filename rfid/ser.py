import serial
import time
import schedule

import csv
l=[]
def main_func():
    arduino=serial.Serial('COM3',9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    #list_values = decoded_values.split('x')

    #for item in list_values:
        #list_in_floats.append(float(item))

    #print(f'Collected readings from Arduino: {list_in_floats}')
    print(f'Collected readings from Arduino: {decoded_values}')
    l.append(decoded_values)
    for i in l:
        print(i)
    
    
    with open("C:\\Users\\mouni\\Desktop\\rfid.csv",'w', newline='') as file:
        for i in l:
            file.write(i)
        '''rfid_writer = csv.writer(rfid)
        rfid_writer.writerows(decoded_values)
    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
    print('Connection closed')
    print('<----------------------------->')


# ----------------------------------------Main Code------------------------------------
# Declare variables to be used
list_values = []
list_in_floats = []'''

print('Program started')

# Setting up the Arduino
schedule.every(3).seconds.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(1)
