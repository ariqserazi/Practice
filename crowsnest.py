#!/usr/bin/python3
import argparse


parser = argparse.ArgumentParser(description= "correct article" , formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('word',metavar='word', help='A word')
arg = parser.parse_args()
word = arg.word
article = 'an' if word[0].lower() in 'aeiou' else 'a'
print(f'Ahoy, Captain, {article} {word} off the larboard bow!')
