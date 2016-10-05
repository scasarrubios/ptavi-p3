#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        posibatts = ['width', 'height', 'background-color', 'id', 'top',
                     'bottom', 'left', 'right', 'src', 'region', 'begin',
                     'dur']
        self.tags = []
        self.tagatts = []

    def startElement(self, name, attrs):

        posibatts = ['width', 'height', 'background-color', 'id', 'top',
                     'bottom', 'left', 'right', 'src', 'region', 'begin',
                     'dur']
        posibtags = ['root-layout', 'region', 'img', 'audio', 'textstream']
        for tag in posibtags:
            if name == tag:
                tagdicc = {}
                attdicc = {}
                for att in posibatts:

                    attdicc[str(att)] = attrs.get(str(att), "")

                tagdicc[str(name)] = attdicc
                self.tags.append(tagdicc)

    def get_tags(self):
        for tag in self.tags:
            print(tag)

if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    sHandler.get_tags()
