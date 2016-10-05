#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        self.tags = ['']
        self.atts = ['']  # lista de diccionarios de atributos 

    def startElement(self, name, attrs):

        atts_rootlayout = ['width', 'height', 'background-color']
        atts_region = ['id', 'top', 'bottom', 'left', 'right']
        atts_img = ['src', 'region', 'begin', 'dur']
        atts_audio = ['src', 'begin', 'dur']
        atts_textstream = ['src', 'region']
        dicc_tags = {'root-layout': atts_rootlayout,
                          'region': atts_region, 'img': atts_img,
                          'audio': atts_audio,
                          'textstream': atts_textstream}

        if name == 'root-layout' or name == 'region' or name == 'img' or name == 'audio' or name == 'textstream':
            self.tags.append(name)
            dicc = {}
            for attr in dicc_tags[name]:
                dicc[attr] = attrs.get(attr, "")

            self.atts.append(dicc)
            
    def get_tags(self):    
        for tag in self.tags: 
            print(tag)
if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    sHandler.get_tags()
