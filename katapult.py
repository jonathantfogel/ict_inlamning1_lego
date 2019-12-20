#!/usr/bin/env pybricks-micropython

from pybricks.parameters import (SoundFile, Color, Port)

from catapult import Catapult

positions =  [35, 43, 54]

for pos in positions :
    input("Start?")
    catapult = Catapult(Port.A, Port.B, 1) #Ställer in katapulten, nu roterar den bara i en sekund!
    catapult.reset()
    catapult.safe_lock() #Förbered för rotation genom att låsa axeln 
    a = ""
    while a is not "n" :
        catapult.retract(100) #Rotera axeln.
        a = input("Rotate?") #Fråga ifall det ska göras igen.
    catapult.unlock()
    catapult = Catapult(Port.A, Port.B, pos) #Lås upp axeln och ställ om katapulten för att kasta.
    input("Lock?") #Under denna tiden rättar vi till axeln och ser till att snöret sitter rätt.
    catapult.reset()
    catapult.safe_lock() #Nu kan vi låsa axeln igen och fortsätta med programmet.
    input("Retract?")
    catapult.retract(100)

    input("Continue?")
    catapult.unlock()