from sense_hat import SenseHat
import time
import scipy as sc

V_MAX = 4.0

sense = SenseHat()

def led_x(velocity):

    if velocity > V_MAX:
        velocity = V_MAX

    velocity_abs = abs(velocity)
    velocity_abs = round(velocity_abs,0)

    if velocity < 0:
        level = -level

    if level == -4.0:
        pix = [True,True,True,True,False,False,False,False]
    elif level = -3.0:
        pix = [False,True,True,True,False,False,False,False]
    elif level = -2.0:
        pix = [False,False,True,True,False,False,False,False]
    elif level = -1.0:
        pix = [False,False,False,True,False,False,False,False]
    elif level = 0.0:
        pix = [False,False,False,False,False,False,False,False]
    elif level = 1.0:
        pix = [False,False,False,False,True,False,False,False]
    elif level = 2.0:
        pix = [False,False,False,False,True,True,False,False]
    elif level = 3.0:
        pix = [False,False,False,False,True,True,True,False]
    elif level = 4.0:
        pix = [False,False,False,False,True,True,True,True]
    else:
        pix = [True for i in range(8)]
    
    for i in range(8):

        if pix[i] == True:
            sense.set_pixel(i,3,255,0,0)
            sense.set_pixel(i,4,255,0,0)
        else:
            sense.set_pixel(i,3,0,0,0)
            sense.set_pixel(i,4,0,0,0)

def getVelocity(pre, cur, diff):

    return (cur-pre) / diff

sense.clear()

cur = sense.get_orientation_dgrees()
pre = sense.get_orientation_dgrees()
pre_time = time.time()

while True:
    ori = sense.get_orientation_dgrees()

    cur = ori['pitch']

    cur_time = time.time()
    velocity_x = getVelocity(pre,cur,cur_time-pre_time)

    pre = cur
    pre_time = cur_time

    led_x(velocity_x)

