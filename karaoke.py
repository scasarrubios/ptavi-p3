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
    replace = {"': '": '="', "'}}, ": '"\n', "', '": '"\t', "': {'": '\t',
               "'}}]": '"', "{'": '', "': ": '\t', '[': ''}
    #elementos a remplazar con sus reemplazamientos deseados
    keys = ["': '", "'}}, ", "', '", "': {'", "'}}]", "{'", "': ", '[']
    #claves de los elementos a reemplazar para hacerlo de manera ordenada
    for elem in keys:
        tags = str(tags).replace(elem, replace[elem])
    print(tags)
