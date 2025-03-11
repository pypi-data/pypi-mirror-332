# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 2025

@author: Cord Hockemeyer
"""

def itemname(num):
    """Return an Itemname based on the item number
    """
    if (num < 1):
          raise Exception("Sorry, no numbers below zero")
    elif (num < 27):
         return(chr(num+96))
    elif (num < 677):
         return(chr((num//26)+96)+chr((num%26)+96)) 
    elif (num < 17577):
         return(chr((num//676)+96)+chr((num//26)+96)+chr((num%26)+96)) 
    else:
         raise Exception("So far limited to 17576 items")