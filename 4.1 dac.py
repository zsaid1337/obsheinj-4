import RPi.GPIO as GPIO
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def tentotwo(x):
    voltage = 3.3*x/256
    two = []
    while x:
        if x % 2 == 1:
            two.append(1)
        else:
            two.append(0)
        x //= 2
        
    
    return two[::-1], voltage

try:
    while True:
        arr = [0, 0, 0, 0, 0, 0, 0, 0]

        
        print("Введите число от 0 до 255")
        k = input()
        if k == "q":
            break
        elif int(k) != float(k) or int(k) > 255 or int(k) < 0:
            print("Братишка, здесь-то ты и попутал")
        binary = tentotwo(int(k))[0]
        for i in range(len(binary)):
            arr[i] = binary[i]
        for i in range(8):
            GPIO.output(dac[i], arr[i])
        voltage = tentotwo(int(k))[1]
        print(f"Напряжение на ЦАП: {voltage}")
        




finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()























































































