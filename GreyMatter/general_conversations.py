#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:36:39 2018

@author: david
"""

from SenseCells.tts import tts

def who_are_you():
    message = "I am Dave's Virtual Assistant..  he didn't give me a name as such yet....."
    tts(message)
    
def undefined():
    tts("Sorry I didn't understand what you said there bro")

    