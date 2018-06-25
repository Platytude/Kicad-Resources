#quick little script designed to give a baseline inductor value for
#buck converters, based on TI AN1197

import sys
import os

vin = input("Enter Input voltage:")
vo= input("Enter Output voltage:")
io=input("Enter Output Current(A):")
f = input("Enter Switching Frequency:")
r = input("Enter desired value of r (recommended between 0.25-0.5):")
vsw = input("Enter Switch Voltage:")
vd = input("Enter Diode Voltage:")

L = ((vin-vsw-vo)*(vo+vd))/((vin-vsw+vd)*r*f*io)*(10**6)
print("Rough Inductor Value is",L,"uH")
