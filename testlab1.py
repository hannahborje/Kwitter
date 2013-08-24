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
(XXXX = portnummer)
 
"""


from twitterclient import TwitterClient # se twitterclient.py
from testserver import Server # se server.py

      
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
           print "Startar testning:"        
           client.test_tweets(tweets, error_msg[0])
           client.test_checkboxes()
           client.test_order(tweets) 
           client.test_refresh()
           
       except (KeyboardInterrupt, SystemExit):
           print "Program avslutades av användaren"
       except AssertionError as e:
           print "Fel vid assert: ", e
       except UnicodeDecodeError as e:
           print "Unicode-fel", e
       except Exception as e:
           print "Fel uppstod vid testning: ", e
                      
       # Om inga fel uppstått under testning    
       else:
           print "Testning genomförd (OK)"

    # Uppstartsfel
    except Exception as e:
        print "Fel uppstod vid laddning av html-sida: ", e       

    # Oavsett om fel uppstått under uppstart - gör följande
    finally:
        print "Slut på testning, stänger webbläsare"
        client.quit() 
       
