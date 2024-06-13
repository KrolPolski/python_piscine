#!/usr/bin/env python

from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for characters"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        pass

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """A class for defining members of the Stark Family"""
    def __init__(self, first_name, is_alive=True):
        """Creates an object from the Stark class"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Kills the character in question"""
        self.is_alive = False


def main():
    Ned = Stark("Ned")
    print(Ned.first_name)
    # print(Ned.is_alive)
    # hodor = Character("Hodor")


if __name__ == '__main__':
    main()
