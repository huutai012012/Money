import RPi.GPIO as GPIO
from time import sleep
import drivers
display = drivers.Lcd()


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MATRIX = [ [1,2,3,'A'],  #keycode
           [4,5,6,'B'],
           [7,8,9,'C'],
           ['*',0,'#','D'] ]
ROW = [4,17,27,22]
COL = [10,9,11,0]
GPIO.setmode(GPIO.BCM)
sensor = 14
DCmotor = 21
GPIO.setup(18,GPIO.OUT)
GPIO.setup(sensor,GPIO.IN)

#khai bao cho ham lay tien
sensor = 14
in1=  6 
in2 = 13
in3 = 19
in4 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(in1,GPIO.OUT,initial =0)
GPIO.setup(in2,GPIO.OUT,initial =0)
GPIO.setup(in3,GPIO.OUT,initial =0)
GPIO.setup(in4,GPIO.OUT,initial =0)



for j in range(4):
    GPIO.setup(COL[j],GPIO.OUT)
    GPIO.output(COL[j],1)
for i in range(4):
    GPIO.setup(ROW[i],GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT,initial=0) #gia tri ban dau la o muc thap


    
#################################################################################    
def presskey():
    GPIO.setmode(GPIO.BCM)
    for j in range(4):
        GPIO.setup(COL[j],GPIO.OUT)
        GPIO.output(COL[j],1)
    for i in range(4):
        GPIO.setup(ROW[i],GPIO.IN,pull_up_down=GPIO.PUD_UP)
        GPIO.setup(18,GPIO.OUT,initial=0) #gia tri ban dau la o muc thap
    while True:
        for j in range(4):
            GPIO.output(COL[j],0)
            for i in range(4):
                if GPIO.input(ROW[i]) ==0:
                    print("Your key pressed is:",MATRIX[i][j])
                    sleep(0.5)
                    return MATRIX[i][j]
        return 'noKey'
        
############################################################################
'''
Laytien la ham nhan tien, khi chay r=thi ham se kiem tra co tien hay ko
co thi nhan ko thi thoa ham
'''
def layTien():
    input_state = GPIO.input(sensor)
    print('sensor o muc',input_state)
    if input_state == 0:
        while input_state == 0: # khi gia tri nhan vao = 1
            print('sensor o muc',input_state)
            print('Dang nhan tien')
            display.lcd_clear()
            display.lcd_display_string('DANG NHAN TIEN !!',1)  
            input_state = GPIO.input(sensor)
            GPIO.output(in1,1)        #pinout Rasp noi voi IN1 cua L293, DC motor start
            GPIO.output(in2,0) 
            print(' in1 len muc 1')
            GPIO.output(in3,1)        #pinout Rasp noi voi IN1 cua L293, DC motor start
            GPIO.output(in4,0) 
            print(' in2 len muc 1')
        GPIO.output(in1,0)
        GPIO.output(in2,0)
        GPIO.output(in3,0)
        GPIO.output(in4,0)
        sleep(3)
        GPIO.output(in3,1)        #pinout Rasp noi voi IN1 cua L293, DC motor start
        GPIO.output(in4,0)
        GPIO.output(in1,1)
        GPIO.output(in2,0)
        sleep(5)
    GPIO.output(in1,0)
    GPIO.output(in2,0)
    GPIO.output(in3,0)
    GPIO.output(in4,0)
    display.lcd_clear()
    display.lcd_clear()
    display.lcd_display_string('  GIA TRI TIEN',2)
    sleep(3)
    display.lcd_clear()
    
############################################################################
