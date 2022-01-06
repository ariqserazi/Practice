import argparse
parser = argparse.ArgumentParser(description= "Picnic" , formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('item',metavar='str', nargs = "+", help='items to bring')
parser.add_argument('-s','--sorted',action='store_true', help = "sorts the items")
arg = parser.parse_args()
items = arg.items
num = len(items)
