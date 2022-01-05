#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser(description= "Weight Conversion" , formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-w','--weight',type = int, metavar = 'weight' , required=True, help = 'Clarify number')
parser.add_argument('-t','--type',type = str, metavar = 'type' , required=True, help = 'Clarify kilograms or pounds')
arg = parser.parse_args()
type = str(arg.type)
print(type)
weight = float(arg.weight)
if type.upper()  == "L":
    conversion = weight / 0.45
    print("Weight in Lbs "+ str(conversion))
else:
    conversion = weight * 0.45
    print("Weight in Kgs "+ str(conversion))


