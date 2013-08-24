#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TDP013: Laboration 1
testserver.py
Hannah Börjesson & Per Jonsson IP2
Används för testning med Selenium(2) av lab1.html
 
"""
import sys

class Server:
    """ Anger portnumret till localhost-servern"""
    def __init__(self):
        # Försök hämta portnummer från kommandoraden 
        if sys.argv[1:]:
            self.port = int(sys.argv[1])
        else:
            self.port = 8000
            
        # För att starta servern på angiven port (för lata typer)
        #subprocess.Popen("python -m SimpleHTTPServer {0}".format(PORT), shell=True)
