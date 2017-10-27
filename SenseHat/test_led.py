from sense_hat import SenseHat
import time

r = [255,0,0]
b = [0,0,0]

sense = SenseHat()

sense.clear()

sense.show_message("Hello ( ¥^ o ¥^ )")

time.sleep(1)

sense.show_letter("3",text_colour=[255,0,0])
time.sleep(1)
sense.show_letter("2",text_colour=[0,255,0])
time.sleep(1)
sense.show_letter("1",text_colour=[0,0,255])
time.sleep(1)

sense.clear()
for i in range(5):
    image = [
    
        b,b,b,b,b,b,b,b,
        b,r,r,b,b,r,r,b,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        b,r,r,r,r,r,r,b,
        b,r,r,r,r,r,r,b,
        b,b,r,r,r,r,b,b,
        b,b,b,r,r,b,b,b
    ]
    
    sense.set_pixels(image)
    temp = r
    r = b
    b = temp

    time.sleep(1)

sense.clear()
