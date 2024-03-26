import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
def tentotwo(x):
    two = [0, 0 , 0, 0, 0, 0, 0, 0]
    i = 0
    while x:
        if x % 2 == 1:
            two[i] = 1
        else:
            two[i] = 0
        x //= 2
        i+=1
        
    
    return two[::-1]
x = 0

y = 1
T = input()
try:
    while True:
        try:
            T = int(T)
            GPIO.output(dac, tentotwo(x))
            time.sleep(T/512)
            
            if x == 0:
                y = +1
            if x == 255:
                y = -1
            x += y
        except:
            break
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
