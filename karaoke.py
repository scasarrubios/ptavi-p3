#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys


if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open(sys.argv[1]))
    tags = sHandler.tags
    string = ''
    for line in tags:
        for tag in line:
            string = string + '\n' + tag + '\t'
            for att in line[tag]:
                string = string + att + '="' + line[tag][att] + '"\t'
    print(string)
