from sense_hat import SenseHat
import time

sense = SenseHat()

start = time.time()

while True:

  orientation = sense.get_orientation_degrees()
  pitch = orientation['pitch']
  roll = orientation['roll']
  yaw = orientation['yaw']

  acceleration = sense.get_accelerometer_raw()

  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']

  x=round(x,0)
  y=round(y,0)
  z=round(z,0)

  print("----------------------")
  print("pitch={0}, roll={1}, yaw={2}".format(pitch,roll,yaw))
  print("x={0}, y={1}, z={2}".format(x,y,z))

  time.sleep(0.5)

  if time.time() - start > 20:
    break

