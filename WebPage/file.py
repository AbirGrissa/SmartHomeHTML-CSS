from flask import Flask,render_template
import RPi,GPIO as GPIO

app= Flask(__name__)#initialiser flask web application

pins=(11,12) #pins is a dict

GPIO.setmode(GPIO.BOARD) #numbers GPIOs by physical location
GPIO.setup(pins,GPIO.OUT) #set pins mode is output
GPIO.output(pins,GPIO.LOW)#set pins to LOW to off led

P_R = GPIO.PWM(pins[0],2000)#set frequeence to 2khz
P_G =GPIO.PWM(pins[1],2000)

def map(x,in_min,in_max,out_min,out_max):
    return(x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col): 
    R_val = col >>8
    G_val = col & 0x00FF

    R_val = map(R_val ,0,255,0,100)
    G_val = map(G_val ,0,255,0,100)

    P_R.ChangeDutyCycle(R_val)
    P_G.ChangeDutyCycle(G_val)

@app.route('/on') #on road
def on():
    P_R.start(0)
    P_G.start(0)
    setColor(0xFF00)
    return runder_template('indexOn.html')


@app.route('/off')
def off():
    P_R.stop(0)
    P_G.stop(0)
    GPIO.output(pins,GPIO.LOW)

    return runder_template('indexOff.html')   