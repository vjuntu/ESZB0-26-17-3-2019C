import RPi.GPIO as GPIO
from time import sleep

x = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

p = GPIO.PWM(16,100)
p.start (0)

while x<=90 and x>0:
    if GPIO.input(25) == GPIO.LOW:
        x = x+10
        print(x)
        p.ChangeDutyCycle(x)
        sleep(0.5)
    elif GPIO.input(24) == GPIO.HIGH:
        x = x-10
        print(x)
        p.ChangeDutyCycle(x)
        sleep(0.5)

GPIO.cleanup() 
