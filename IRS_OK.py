import RPi.GPIO as GPIO
import time
 
def init():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.IN)
	#GPIO.setup(11,GPIO.OUT)
	pass 
def detct():
    while True:
        curtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        if GPIO.input(11) == True:
            alart(curtime)
        else:
            print(" Noanybody!")
            continue
        time.sleep(6) #每6秒检查一次
def alart(curtime):
    print(curtime+" Somebody is come!")
time.sleep(5)
init()
detct()
GPIO.cleanup()