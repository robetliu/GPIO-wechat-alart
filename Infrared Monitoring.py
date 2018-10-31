from wxpy import *
from wechat_sender import *
import picamera
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
#GPIO.setup(11,GPIO.OUT)
bot=Bot(console_qr=True,cache_path=True)#终端显示二维码 ，一段时间不需要输入二维码
my_friend = bot.friends().search('刘睿')[0]
#tuling = Tuling(api_key='8edce3ce905a4c1dbb965e6b35c3834d')
@bot.register(my_friend)
def reply_my_friend(msg):
    ms=msg.text
    print(ms)
    if ms.find("拍照")>=0:
        print("拍照ok")
        camera=picamera.PiCamera()
        camera.led=True
        try:
            camera.vflip=True#垂直翻转
            camera.start_preview()
            camera.brightness = 60#亮度
            camera.capture('imagex.jpg')
            camera.stop_preview()
        except:
            my_friend.send('PiCamera Error')
        else:
            my_friend.send_image('imagex.jpg')
        finally:
            camera.close()
    if ms.find("摄像")>=0:
        print("摄像ok")
        camera=picamera.PiCamera()
        camera.resolution = (640, 480)
        camera.led=True
        try:
            camera.start_preview()
            camera.start_recording('videonow.h264', format='h264', quantization=23, resize=(1024, 768))
            camera.wait_recording(8)
            camera.stop_recording()
            camera.stop_preview()
        except:
            my_friend.send('PiCamera Error')
        else:
            my_friend.send_video('videonow.h264')
        finally:
            camera.close()
    else:
        return
        
def detct():
    while True:
        curtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        if GPIO.input(17) == True:
            alart(curtime)
            camera=picamera.PiCamera()
            camera.led=True
            try:
                camera.vflip=True
                camera.start_preview()
                camera.brightness = 60#亮度
                camera.capture('image.jpg')
                camera.stop_preview()
            except:
                my_friend.send('PiCamera Error')
            else:
                my_friend.send_image('image.jpg')
            finally:
                camera.close()
        else:
            print(" Noanybody!")
            #tuling.do_reply("Noanybody")
            #my_friend.send("Noanybody")
        time.sleep(15) #每15秒检查一次
            
def alart(curtime):
    print(curtime+" Somebody is come!")

time.sleep(5)
detct()
embed()# 进入 Python 命令行、让程序保持运行
#bot.join()# 或者仅仅堵塞线程
GPIO.cleanup()