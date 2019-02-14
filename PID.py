#!/usr/bin/env python3

import os
import sys
import time
import datetime
import struct

import ev3dev2.motor as ev3_master_motor # LargeMotor,OUTPUT_A, OUTPUT_B, OUTPUT_C,OUTPUT_D
import ev3dev2.sensor as ev3_master_sensor_port # INPUT_1,INPUT_2,INPUT_3,INPUT_4
import ev3dev2.sensor.lego as ev3_master_sensor # ColorSensor

DaisyChainEnabled = True
if DaisyChainEnabled:
    import rpyc
    conn  = rpyc.classic.connect('ev3devS1')
    ev3_slave_motor   = conn.modules['ev3dev2.motor']
    ev3_slave_sensor_port = conn.modules['ev3dev2.sensor'] 
    ev3_slave_sensor = conn.modules['ev3dev2.sensor.lego']

# state constants
ON = True
OFF = False

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.
    This shows up in the output panel in VS Code.
    '''
    now = datetime.datetime.now().strftime('%H:%M:%S.%f')
    print(now, end=' ')
    print(*args, **kwargs, file=sys.stderr)

def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')

def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')

def set_font(name):
    '''Sets the console font

    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)

def main():
    '''The main function of our program'''

    # set the console just how we want it
    reset_console() #重置屏幕
    set_cursor(OFF) #
    set_font('Lat15-Terminus24x12')

    GyroSensor1 = ev3_master_sensor.GyroSensor(ev3_master_sensor_port.INPUT_1)
    
    for i in range (1000):
        angle = GyroSensor1.angle
        print('{} Gyro angle: {}'.format(i, angle))

    MB = ev3_slave_motor.LargeMotor(ev3_slave_motor.OUTPUT_B)
    MB.on(speed=50)
    time.sleep(10)
    MB.off() 

'''

    MA=ev3_Master.LargeMotor(OUTPUT_A)
    MB=LargeMotor(OUTPUT_B)
    MC=LargeMotor(OUTPUT_C)
    MD=LargeMotor(OUTPUT_D)
    col1 = ColorSensor(INPUT_1)
    col2 =  ColorSensor(INPUT_2)
    col3 =  ColorSensor(INPUT_3)
    col4 = ColorSensor(INPUT_4)

    error=0
    kp=0.6

    while True:
        n1=col1.reflected_light_intensity
        n2=col2.reflected_light_intensity
        n3=col3.reflected_light_intensity
        n4=col4.reflected_light_intensity
        debug_print(n1,n2,n3,n4)
        if n1>50 :
            n1=50
        if n2>50 :
            n2=50
        Turn=n1-n2-error
        if col3.reflected_light_intensity<40 or col4.reflected_light_intensity<40:
            if col3.reflected_light_intensity<40 :
                while col1.reflected_light_intensity>30 and  col2.reflected_light_intensity>30:
                    n1=col1.reflected_light_intensity
                    n2=col2.reflected_light_intensity
                    n3=col3.reflected_light_intensity
                    n4=col4.reflected_light_intensity
                    l=-20
                    r=40
                    MA.on(speed=l)  
                    MB.on(speed=l) 
                    MC.on(speed=r) 
                    MD.on(speed=r) 
                    debug_print('col3<40 and col1>30 and col2>30',n1,n2,n3,n4,l,r)
            else :
                while col2.reflected_light_intensity>30 and col1.reflected_light_intensity>30:
                    n1=col1.reflected_light_intensity
                    n2=col2.reflected_light_intensity
                    n3=col3.reflected_light_intensity
                    n4=col4.reflected_light_intensity
                    l=40
                    r=-20
                    MA.on(speed=l)  
                    MB.on(speed=l) 
                    MC.on(speed=r) 
                    MD.on(speed=r)    
                    debug_print('col4<40 and col1>30 and col2>30',n1,n2,n3,n4,l,r)
        else :
            l=Turn*kp+30        
            r=30-Turn*kp
            MA.on(speed=l)  
            MB.on(speed=l) 
            MC.on(speed=r) 
            MD.on(speed=r)
            debug_print('col3>40 and col4>40',n1,n2,n3,n4,l,r)
'''

if __name__ == '__main__':
    main()

