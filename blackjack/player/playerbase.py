# -*- coding: utf-8 -*-
"""
Module docstring

TODO:
    * Write module docstring
"""
from .hand import Hand


class PlayerBase:
    """Class to represent a base for player objects"""
    def __init__(self):
        self.hand = Hand()
