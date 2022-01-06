#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser(description= "Picnic" , formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('item',metavar='str', nargs = "+", help='items to bring')
parser.add_argument('-s','--sorted',action='store_true', help = "sorts the items")
arg = parser.parse_args()
items = arg.item
num = len(items)
if arg.sorted:
    items.sort()

bring = ""
if num == 1:
    bring = items[0]
elif num == 2:
    bring = " and ".join(items)
else: 
    items[-1] = "and " + items[-1]
    bring = ", ".join(items)
    
print('You are bringing {}.'.format(bring))
