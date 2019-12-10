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

redPile = -20
otherPile = -20
deltaLift = 10

color_pallet = {1:"Black", 2:"Blue", 3:"Green", 4:"Yellow", 5:"Red", 6:"White", None:"None"}

def setRedBlock() :
    turn.run_target(100, -70)
    global redPile
    lift.run_target(50, redPile) #Lowers block
    redPile += deltaLift

def setOtherBlock() :
    turn.run_target(100, 70)
    global otherPile
    print(otherPile)
    lift.run_target(50, otherPile) #Lowers block
    otherPile += deltaLift

claw.run(60) #Homeing lift
sleep(3)
claw.reset_angle(0)
claw.run_target(100, -90)
claw.reset_angle(0)

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
    #turn.run_target(128, -23) #Moves to where block is
    turn.run_target(150, -103) #Moves to where block is
    turn.reset_angle(0) #New home, because it is the intresting position
    turn.run_target(100, 90) #Moves to where block is

while True:
    input("Smack my bitch up (confirm?): ")
    claw.run_target(100, 0)
    lift.run_target(100, 0)
    turn.run_target(150, 0)
    sleep(1)

    lift.run_target(25, -25) #Lowers arm to the block
    sleep(0.7) 

    claw.run(255) #Closes the claw with maximum force
    sleep(1)
    claw.stop(Stop.HOLD) #Holds the block

    lift.run_target(40, 5) #Lifts block to sensor
    lift.stop(Stop.HOLD) #Holds arm so block is at sensor height

    sleep(0.8)
    print(color_pallet[col.color()]) #Scans and prints color of block
    saveColour = col.color()
    lift.run_target(40, 30) #Lifts block to sensor
    sleep(1)
    if (saveColour == 5) :
        setRedBlock()
    else :
        setOtherBlock()
    sleep(1)
    
    claw.stop(Stop.COAST) #Release block
    sleep(1)
    lift.run_target(40, 30) #Lifts block to sensor
    sleep(1)

    #lift.run_target(255, 30) 
    #turn.run_target(255, -90) #Rotates arm for new blockposition
    #lift.run_target(20, -25) #Lowers block


