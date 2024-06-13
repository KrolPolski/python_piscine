#!/usr/bin/env python

from S1E9 import Character


class Baratheon(Character):
    """A class for defining members of the Baratheon Family"""
    def __init__(self, first_name, is_alive=True):
        """Creates an object from the Baratheon class"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hair = 'dark'

    def __str__(self):
        return f"<bound method Baratheon.__str__ of Vector: \
('{self.family_name}', '{self.eyes}', '{self.hair}')>"

    def __repr__(self):
        return f"Vector:('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def die(self):
        """Kills the character in question"""
        self.is_alive = False


class Lannister(Character):
    """A class for defining members of the Lannister Family"""
    def __init__(self, first_name, is_alive=True):
        """Creates an object from the Lannister class"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hair = 'light'

    def __str__(self):
        return f"<bound method Lannister.__str__ of Vector: \
('{self.family_name}', '{self.eyes}', '{self.hair}')>"

    def __repr__(self):
        return f"Vector:('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def die(self):
        """Kills the character in question"""
        self.is_alive = False

    def create_lannister(self, is_alive=True):
        """Spawns a lannister with a method instead of
        directly with a constructor"""
        return (Lannister(self))
