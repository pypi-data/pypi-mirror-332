# -*- coding: utf-8 -*-
"""
Created on Sun Mar 09 2025

@author: Cord Hockemeyer
"""

def domain(structure):
    """ Determine the domain of a set/list of frozensets
    """
    dom = set({})
    for s in structure:
        dom = dom.union(s)
    return dom