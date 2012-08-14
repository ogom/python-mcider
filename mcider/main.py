#!/usr/bin/env python
""" mcider - main
Copyright(c) 2012 ogom

Mcider is to convert markdown into slideshow.
"""
import os
from cli_helper import parser
import converter
import util

def main():
    """ entry points """
    args = parser.parse_args()
    
    path = os.path.abspath(os.path.dirname(args.file.name))
    output = os.path.join(path, os.path.splitext(os.path.basename(args.file.name))[0] + '.html')
    if args.output:
        path = os.path.abspath(os.path.dirname(args.output.name))
        output = os.path.abspath(args.output.name)

    slide = converter.Slide(args.file.read().decode('utf-8'), args.theme)
    html = slide.maker(path)
    util.fs_writer(output, html)

    print("Output: %s" % output)

if __name__ == '__main__':
    main()
