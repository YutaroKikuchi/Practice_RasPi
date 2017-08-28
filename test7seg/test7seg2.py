import wiringpi as pi ,time

def seg_decoder(number):

	if number==0:
		ret = [1,1,1,1,1,1,0]
	elif number==1:
		ret = [0,1,1,0,0,0,0]
	elif number==2:
		ret = [1,1,0,1,1,0,1]
	elif number==3:
		ret = [1,1,1,1,0,0,1]
	elif number==4:
		ret = [0,1,1,0,0,1,1]
	elif number==5:
		ret = [1,0,1,1,0,1,1]
	elif number==6:
		ret = [1,0,1,1,1,1,1]
	elif number==7:
		ret = [1,1,1,0,0,0,0]
	elif number==8:
		ret = [1,1,1,1,1,1,1]
	elif number==9:
		ret = [1,1,1,1,0,1,1]
	else:
		ret = [0,0,0,0,0,0,0]

	return ret

inv_time = 1

out_7seg1=[3,2,14,15,18,4,17]
out_7seg2=[27,22,23,24,25,26,19]

pi.wiringPiSetupGpio()

for i in range(7):
	pi.pinMode(out_7seg1[i],1)
	#pi.pinMode(out_7seg2[i],0)

count = 0

flag = False

while(True):

        if flag == False:
                for i in range(7):
                        pi.digitalWrite(out_7seg1[i],1)
                        #pi.pinMode(out_7seg2[i],1)

                flag = True

        else:
                for i in range(7):
                        pi.digitalWrite(out_7seg1[i],0)
                        #pi.pinMode(out_7seg2[i],1)
                flag = False

        time.sleep(1)
