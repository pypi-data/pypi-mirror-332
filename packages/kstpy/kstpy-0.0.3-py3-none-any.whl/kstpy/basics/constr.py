# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 2025

@author: Cord Hockemeyer
"""
from kstpy.helpers.kstFrozenset import kstFrozenset

def constr(structure):
    """ Compute the smallest knowledge space containing a famly of kstFrozensets

    Parameters
    ----------
    structure: set
        Family of kstFrozensets

    Returns
    -------
    Knowledge space

    Examples
    --------
    >>> from kstpy.data.xpl import xpl_basis
    >>> constr(xpl_basis)
    """
    total = set({})
    for state in structure:
        total = total.union(state)
        
    space = set({kstFrozenset({}), kstFrozenset(total)})
    space.union(structure)
    for state in structure:
        new_states = set({})
        for s in space:
            if not ((set({state | s})) <= space):
                new_states.add((state | s))
        space = space | new_states
    return space

