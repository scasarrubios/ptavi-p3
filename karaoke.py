#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve
import sys
import json


class KaraokeLocal():

    def inicializador(self, fich):
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(fich))
        self.tags_list = sHandler.get_tags()

    def __str__(self):
        string = ''
        for line in self.tags_list:
            for tag in line:
                string = string + '\n' + tag + '\t'
                for att in line[tag]:
                    string = string + att + '="' + str(line[tag][att]) + '"\t'
        print(string)

    def to_json(self, fich_name):
        data = {}
        if fich_name != 'local.json':
            nombre = str(sys.argv[1]).strip(".smil") + '.json'
        else:
            nombre = fich_name
        fichero = open(nombre, 'w')
        json.dump(self.tags_list, fichero)

    def do_local(self):
        for line in self.tags_list:
            for tag in line:
                for att in line[tag]:
                    if line[tag][att][:7] == "http://":
                        urlretrieve(line[tag][att])
                        url = line[tag][att].split('/')
                        line[tag][att] = url[-1]

if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except:
        sys.exit('Se debe ejecutar como karaoke.py fich.smil')
    karaoke = KaraokeLocal()
    karaoke.inicializador(fichero)
    karaoke.__str__()
    karaoke.to_json(sys.argv[1])
    karaoke.do_local()
    karaoke.to_json('local.json')
    karaoke.__str__()
