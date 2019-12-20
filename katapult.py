#!/usr/bin/env pybricks-micropython

from pybricks.parameters import (SoundFile, Color, Port)

from catapult import Catapult

positions =  [35, 43, 54]

#for pos in positions :
while True :
    pos = 54
    input("Start?")
    catapult = Catapult(Port.A, Port.B, 1)
    catapult.reset()
    catapult.safe_lock()
    a = ""
    while a is not "n" :
        catapult.retract(100)
        a = input("Rotate?")
    catapult.unlock()
    catapult = Catapult(Port.A, Port.B, pos)
    input("Lock?")
    catapult.reset()
    catapult.safe_lock()
    input("Retract?")
    catapult.retract(100)

    input("Continue?")
    catapult.unlock()