# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 13:03:53 2025

@author: hockemey
"""

class kstFrozenset(frozenset):
    """
    kstFrozenset is a derivative of the frozenset class.
    
    The main reason for its existance is the print function which
    does not show the class anymore. Set operands (|, &, ^, and -)
    have also been re-defined to produce kstFrozensets.
    """
    def __repr__(self):
        return set(self).__repr__()

    def __str__(self):
        return set(self).__str__()
    
    def __or__(self, value):
        return kstFrozenset(frozenset(self) | frozenset(value))
    
    def __and__(self, value):
        return kstFrozenset(frozenset(self) & frozenset(value))
    
    def __sub__(self, value):
        return kstFrozenset(frozenset(self) - frozenset(value))
    
    def __xor__(self, value):
        return kstFrozenset(frozenset(self) ^ frozenset(value))
    
