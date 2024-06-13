#!/usr/bin/env python

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Passes the divine right of kings to a new person"""
    def set_eyes(self, eyes):
        """Changes eye color"""
        self.eyes = eyes

    def set_hair(self, hair):
        """Changes hair color"""
        self.hair = hair

    def get_hair(self):
        """returns hair color"""
        return self.hair

    def get_eyes(self):
        """returns eye color"""
        return self.eyes


def main():
    Jof = King('Jof')
    print(Jof.__dict__)


if __name__ == '__main__':
    main()
