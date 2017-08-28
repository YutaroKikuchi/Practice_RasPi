import wiringpi as wp
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

pin_X = [21,16,13,11,5]
pin_Y = [26,19,20,6,12,7,8]

pos = [[1,1,1,1,1],
       [1,0,0,0,1],
       [1,0,0,0,1],
       [1,0,0,0,1],
       [1,0,0,0,1],
       [1,0,0,0,1],
       [1,1,1,1,1]]
wp.wiringPiSetupSys()

for i in range(len(pin_X)):
    wp.pinMode(pin_X[i],wp.GPIO.OUTPUT)

for i in range(len(pin_Y)):
    wp.pinMode(pin_Y[i],wp.GPIO.OUTPUT)

while(True):
    outputMat(wp.digitalWrite,time.sleep,pin_X,pin_Y,pos,0,1)
