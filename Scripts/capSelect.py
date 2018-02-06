#quick little script designed to give optimal capacitor sizing based on
#lowest cost for value, voltasge, grade, etc.
#standard values for voltage rating and size taken from digikey

import sys
import os

voltages = (2.5, 4, 6.3, 10, 16, 20, 25, 35, 50, 63, 80, 100, 150, 200, 250) #standard values

val = input("Enter Capacitance Value:")
if "m" in val or "M" in val:
    mult = 1e-3
if "u" in val or "U" in val:
    mult = 1e-6
if "n" in val or "N" in val:
    mult = 1e-9
if "p" in val or "P" in val:
    mult = 1e-12


