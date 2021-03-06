#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.tags = []

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
                    if str(attrs.get(str(att))) != 'None':
                        attdicc[str(att)] = attrs.get(str(att), "")
                tagdicc[str(name)] = attdicc
                self.tags.append(tagdicc)

    def get_tags(self):
        return self.tags

if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
