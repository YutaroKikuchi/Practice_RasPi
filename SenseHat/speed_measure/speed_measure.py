from sense_hat import SenseHat
import time
import scipy as sc

V_MAX = 5.0

sense = SenseHat()

def led_x(velocity):

    if velocity > V_MAX:
        velocity = V_MAX

    velocity_abs = abs(velocity)
    velocity_abs = round(velocity_abs,0)

    level = velocity_abs / 5.0

    pix = 0
    while(pix <= level):
        if velocity < 0:
            pix = pix * -1

        sense.set_pixel(3,pix+4,255,0,0)
        sense.set_pixel(4,pix+4,255,0,0)

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

