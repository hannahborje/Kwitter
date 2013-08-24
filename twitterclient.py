#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TDP013: Laboration 1
twitterclient.py
Hannah Börjesson & Per Jonsson IP2
Klientklass för testning med Selenium(2) av lab1.html

Uppfyller kravet att testa alla krav med Selenium

OBS!
För att installera Selenium: $ pip install -U selenium
Exekveringen förutsätter att Firefox också finns installerat 
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import time


class TwitterClient:
    """ Innehåller metoder för att automatiserad testning av kraven på vår
    Twitterklon genom att själv agera som användare av webbläsaren """

    def __init__(self):
        # Skapa en instans av Seleniums Firefox driver
        self.browser = webdriver.Firefox()

    def get_url(self, port):
        # Öppna önskad URL
        url = "http://127.0.0.1:{0}/lab1.html".format(port)
        print "Försöker öppna: {0} ".format(url)
        self.browser.get(url)
    
    def assert_connection(self, title):
        error = "Sidan du begärde gick inte att ladda. Kolla portnumret. "
        # Kolla att sidan har laddats genom att se om titeln är vår egen
        assert title in self.browser.title, error


    def test_tweets(self, tweets, error_msg):
        """ KRAV 1: En användare ska kunna skriva in ett meddelande i ett fält
            KRAV 2: En användare ska kunna, genom att klicka på en knapp,
            publicera sitt meddelande"""
        
        # Hitta elementet där vi komponerar tweets + publicera-knapp
        textarea = self.browser.find_element_by_id("textarea")
        button = self.browser.find_element_by_id("button")
        
        print "Skapar och publicerar tweets:"
        # lägg till default-tweeten som finns i textarean först
        tweets.insert(0, textarea.text) 

        # Skriv tweets + klicka på publicera
        for t in tweets:
            self.send_tweet(t, textarea, button)            
            # Kan vi hitta tweet:en i trädet? Leta felmeddelande annars
            caught_tweet = self.find_tweet()
            print "Hittade tweeten i trädet"
            if not self.assert_tweet(t.strip(), caught_tweet.text.encode('utf-8')):
                self.assert_error_msg(t, error_msg)
            # Testa sedan kronologisk ordning

    def send_tweet(self, tweet, textarea, button):
        print "Skickar tweet: ", repr(tweet)
        t = tweet.decode('utf-8').strip() # för ÅÄÖ
        textarea.click() # fokus på textrutan          
        textarea.send_keys(t) 
        button.click() 

    def find_tweet(self):
        """ KRAV 4: Ett meddelande som är publicerat skall visas i kronologiskt
        fallande (senast först) ordning nedanför textfältet."""
        # find_element_by_id returnerar alltid det första/översta elementet
        # därmed kan vi testa att det översta elementet är det vi senast skickat
        return self.browser.find_element_by_id("tweetmsg")
    
    def find_tweets(self):
        return self.browser.find_elements_by_id("tweetmsg")

    def tweet_exceeds_limits(self, tweet):
        print "Kollar längd på tweeten som skickades"
        length = len(tweet)
        print "Tweeten som skickades var: ", repr(tweet), "\n med längd: ", length      
        return length < 1 or length > 140

    def assert_tweet(self, tweet1, tweet2):
        print "Testar matcha: ", repr(tweet1), "mot: ", repr(tweet2)
        if tweet1 == tweet2:
            print "Lyckades"
            return True
        print "Lyckades inte matcha"
        return False

    def find_error_msg(self):
        # Felmeddelande genereras enbart om tweet är < 0 || > 140 tecken
        print "Letar efter felmeddelande i trädet"
        return self.browser.find_element_by_id("error")

    def assert_error_msg(self, tweet, error_msg):
         """ KRAV 3: Om meddelandet är tomt eller mer än 140 tecken,
         ska det inte publiceras och ett felmeddelande ska visas"""
         error_msg = error_msg.decode('utf-8').strip()
         caught_error_msg = self.find_error_msg().text
         
         if self.tweet_exceeds_limits(tweet):
             print "Otillåten längd på tweet"
             assert caught_error_msg == error_msg, "Hittade ingen tweet och inget felmeddelande"
             print "Hittade ett felmeddelande: ", caught_error_msg
        
    def test_checkboxes(self):
        # Hur många bör vi hitta = antalet tweets
        checkboxes = self.find_checkboxes()
        num_boxes = len(checkboxes)
        print "Letar checkboxar, hittade: ", num_boxes
        
        # klicka, så att de försvinner
        if num_boxes > 0:
            self.disable_textboxes(checkboxes)
            self.test_checkboxes() # Kolla att de försvunnit
        else:
            # Antal bör vara 0
            assert (num_boxes == 0), "Borde inte finnas checkboxar kvar nu"

    def find_checkboxes(self):
        """ KRAV 5: Alla meddelanden som visas skall ha en knapp
        som när man klickar markerar meddelandet som läst. """
        return self.browser.find_elements_by_id("checkbox")
        
    def disable_textboxes(self, checkboxes):
        for c in checkboxes:
            c.click()


    def refresh(self):
        self.browser.refresh()
            
    def test_refresh(self):
        caught_tweets = self.find_tweets()
        num_tweets = len(caught_tweets)
        print "Laddar om sidan"
        print "Innan omladdning finns: ", num_tweets, " antal tweets"
        self.refresh()
        self.assert_refresh()        

    def assert_refresh(self):
        """  KRAV 7: Alla meddelanden (lästa som olästa) skall försvinna
        när man laddar om sidan. """
        # inga poster ska hittas
        caught_tweets = self.find_tweets()
        num_tweets = len(caught_tweets)       
        print "Efter omladdning hittades: ", len(caught_tweets), " antal tweets"
        #assert 0
    
    def quit(self):
        self.browser.quit()






