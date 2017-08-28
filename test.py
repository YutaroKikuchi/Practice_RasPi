import wiringpi as pi
import time


def displayNumber(n):
    "自然数nを二進数としてLEDに表示する．"
    for j in range(len(pinLed)):
        pi.digitalWrite(pinLed[j], n & (1<<j))


pinLed = [2, 3, 4, 5]
pinSw = 26

pi.wiringPiSetupSys()

for pin in pinLed:
    pi.pinMode(pin, 1)

pi.pinMode(pinSw,  0)

counter = 1
lastState = False

startTime = time.time()

try:
    displayNumber(counter)

    while True:
        newState = pi.digitalRead(pinSw)

        if (( newState == True) and (lastState == False)):
            counter += 1
            displayNumber(counter)
            time.sleep(0.2)   # 状態が変わったら少し待つ．

            startTime = time.time()

        if (( newState == True) and (lastState == True)):
            if (time.time() - startTime > 2.0):
                counter = 0
                displayNumber(counter)

        lastState = newState

finally:
    for pin in pinLed:
        pi.digitalWrite(pin, 0)
