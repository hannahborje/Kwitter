#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TDP013: Laboration 1
testlab1.py
Hannah Börjesson & Per Jonsson IP2
Testning med Selenium(2) av lab1.html

För att installera Selenium: $ pip install -U selenium
För att köra på localhost: använd modulen SimpleHTTPServer
Starta testservern med: $ python -m SimpleHTTPServer XXXX
Exekvera med: $ python testlab1.py XXXX
(XXXX = portnummer, t.ex. 8000)

Testat i Python v.2.7.3
"""

from twitterclient import TwitterClient # se twitterclient.py
from testserver import Server # se server.py

import logging
LOG_FILE = 'kwitter.log'
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)

if __name__ == '__main__':
    # Ladda in  tweets att testa, från fil
    with open("test_tweets.txt", "r") as source_tweets:
        tweets = source_tweets.readlines()
    # Samt felmeddelande
    with open("test_errormsg.txt", "r") as error_source:
        error_msg = error_source.readlines()
  
    title = "Kwitter"  # Fönstertitel
    client = TwitterClient() # Testverktyget  
    
    try:
       # Försök starta Firefox + ladda sidan
       server = Server() 
       client.get_url(server.port)
       client.assert_connection(title)
       
       try:
           msg = "Startar testning"
           logging.info(msg)
           print(msg)        
           client.test_tweets(tweets, error_msg[0])
           client.test_checkboxes()
           client.test_refresh()
           
       except (KeyboardInterrupt, SystemExit):
           logging.error("Program avslutades av användaren")
       except AssertionError as e:
           logging.error("Fel vid assert: {0}".format(e))
       except UnicodeDecodeError as e:
           logging.error("Unicode-fel: {0}".format(e))
       except Exception as e:
           logging.error("Fel uppstod vid testning: ".format(e))
                      
       # Om inga fel uppstått under testning    
       else:
           msg = "Testning genomförd (OK)"
           logging.info(msg)
           print(msg)

    # Uppstartsfel
    except Exception as e:
        logging.error("Fel uppstod vid laddning av html-sida: {0}".format(e))       

    # Oavsett om fel uppstått under uppstart - gör följande
    finally:
        msg = "Slut på testning, stänger webbläsare"
        logging.info(msg)
        print(msg)
        client.quit() 
       
