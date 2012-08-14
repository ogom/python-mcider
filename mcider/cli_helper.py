""" mcider - cli helper
Copyright(c) 2012 ogom

Parser for command line options.
"""
import argparse

parser = argparse.ArgumentParser(description='Mcider is to convert markdown into slideshow.')

parser.add_argument(
    'file', metavar='FILE', type=argparse.FileType('r'),
    help='Contents of the markdown.'
)

parser.add_argument(
    '--theme', '-t', default='io2012',
    help='Theme of the slide. (io2012, io2011)'
)

parser.add_argument(
    '--output', '-o', metavar='FILE', type=argparse.FileType('w+'),
    help='File to output slide.'
)
