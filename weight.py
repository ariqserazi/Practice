#!/usr/bin/python3
weight = int(input("Weight:"))
type = input("(K)g or (L)bs:")
if type.upper()== "K":
    conversion = weight / 0.45
    print("Weight in Lbs "+ str(conversion))
else: 
    conversion = weight * 0.45
    print("Weight in Kgs "+ str(conversion))

