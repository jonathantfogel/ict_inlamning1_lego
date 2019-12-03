
#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from time import sleep
    
# Write your program here
brick.sound.beep()

claw = Motor(Port.D)
lift = Motor(Port.C, Direction.COUNTERCLOCKWISE, [8, 40])
turn = Motor(Port.B, Direction.CLOCKWISE, [11, 40])
rot_stop = TouchSensor(Port.S3)
col = ColorSensor(Port.S4)

color_pallet = {1:"Black", 2:"Blue", 3:"Green", 4:"Yellow", 5:"Red", 6:"White", None:"None"}

while True:
    claw.run(20) #Homeing lift
    sleep(3)
    claw.reset_angle(0)
    claw.run_target(100, -90)

    while col.color() != None: #Move lift to prepare for homing
        lift.run(25)
    lift.stop(Stop.HOLD)

    while col.color() == None: #Homeing lift
        lift.run(-25)
    lift.reset_angle(0)
    lift.stop(Stop.HOLD)

    while not rot_stop.pressed():#Homeing rot
            turn.run(128)

    if rot_stop.pressed(): #Saftey for the button is realt pressed
        turn.reset_angle(0) #Home aka at zero position
        turn.run_target(128, -23) #Moves to where block is
        turn.reset_angle(0) #New home, because it is the intresting position

    lift.run_target(25, -25) #Lowers arm to the block
    sleep(1) 

    claw.run(255) #Closes the claw with maximum force
    sleep(1)
    claw.stop(Stop.HOLD) #Holds the block

    lift.run_target(25, 15) #Lifts block to sensor
    lift.stop(Stop.HOLD) #Holds arm so block is at sensor height

    sleep(2)
    print(color_pallet[col.color()]) #Scans and prints color of block

    sleep(1)

    lift.run_target(255, 30) 
    turn.run_target(255, -90) #Rotates arm for new blockposition
    lift.run_target(25, -25) #Lowers block

    sleep(1)
    claw.stop(Stop.COAST) #Release block
