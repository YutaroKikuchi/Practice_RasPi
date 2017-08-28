import wiringpi as wp
import datetime
import time

def outputMat(write, sleep, pin_X, pin_Y, pos, turn_off=wp.GPIO.LOW, turn_on = wp.GPIO.HIGH):
    xline = len(pin_X)
    yline = len(pin_Y)

    for i in range(yline):
        
        for j in range(xline):
            write(pin_X[j], pos[i][j])
        for j in range(yline):
            if j == i:
                write(pin_Y[j], turn_off)
            else:
                write(pin_Y[j], turn_on)
        sleep(0.0009)

        for j in range(xline):
            write(pin_X[j], turn_off)
        for j in range(yline):
            write(pin_Y[j], turn_on)
        sleep(0.0001)

def decoder_Num(num):

    if num == 0:
        ret = [[1,1,1,1,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,1,1,1,1]]
    elif num == 1:
        ret = [[0,0,0,0,1],
               [0,0,0,0,1],
               [0,0,0,0,1],
               [0,0,0,0,1],
               [0,0,0,0,1],
               [0,0,0,0,1],
               [0,0,0,0,1]]
    elif num == 2:
        ret = [[1,1,1,1,1],
               [0,0,0,0,1],
               [0,0,0,0,1],
               [1,1,1,1,1],
               [1,0,0,0,0],
               [1,0,0,0,0],
               [1,1,1,1,1]]
    elif num == 3:
        ret = [[1,1,1,1,1],
               [0,0,0,0,1],
               [0,0,0,0,1],
               [1,1,1,1,1],
               [0,0,0,0,1],
               [0,0,0,0,1],
               [1,1,1,1,1]]
    elif num == 4:
        ret = [[1,0,0,0,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,1,1,1,1],
               [0,0,0,0,1],
               [0,0,0,0,1],
               [0,0,0,0,1]]
    elif num == 5:
        ret = [[1,1,1,1,1],
               [1,0,0,0,0],
               [1,0,0,0,0],
               [1,1,1,1,1],
               [0,0,0,0,1],
               [0,0,0,0,1],
               [1,1,1,1,1]]
    elif num == 6:
        ret = [[1,1,1,1,1],
               [1,0,0,0,0],
               [1,0,0,0,0],
               [1,1,1,1,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,1,1,1,1]]
    elif num == 7:
        ret = [[1,1,1,1,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [0,0,0,0,1],
               [0,0,0,0,1],
               [0,0,0,0,1]]
    elif num == 8:
        ret = [[1,1,1,1,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,1,1,1,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,1,1,1,1]]
    elif num == 9:
        ret = [[1,1,1,1,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,1,1,1,1],
               [0,0,0,0,1],
               [0,0,0,0,1],
               [1,1,1,1,1]]
    else:
        ret = [[1,1,1,1,1],
               [1,1,1,1,1],
               [1,1,1,1,1],
               [1,1,1,1,1],
               [1,1,1,1,1],
               [1,1,1,1,1],
               [1,1,1,1,1]]

    return ret

pin_X = [21,16,13,11,5]
pin_Y = [26,19,20,6,12,7,8]

wp.wiringPiSetupSys()

for i in range(len(pin_X)):
    wp.pinMode(pin_X[i],wp.GPIO.OUTPUT)

for i in range(len(pin_Y)):
    wp.pinMode(pin_Y[i],wp.GPIO.OUTPUT)

for i in range(len(pin_X)):
    wp.digitalWrite(pin_X[i],wp.GPIO.OUTPUT)

for i in range(len(pin_Y)):
    wp.digitalWrite(pin_Y[i],wp.GPIO.OUTPUT)

count = 0

rate = 0.01

while(True):

    pos = decoder_Num(count)

    t = 0
    start = int(time.mktime(datetime.datetime.now().timetuple()))
    while(True):
        outputMat(wp.digitalWrite,time.sleep,pin_X,pin_Y,pos,0,1)
        if(int(time.mktime(datetime.datetime.now().timetuple()))-start >= 1):
            break

    count += 1

    if count >=10:
        count = 0
