"""
Program: set_age.py
Author: Ihsan Anwary
Last date modified: 11/06/2020
This program is an example of Overriding Class Methods with one base class and two drived classes
"""


class Employee:
    """" employee class"""

    def __init__(self, _last_name ,_first_name):  # constructor
        self._last_name = _last_name
        self._first_name = _first_name

    def display1(self):
        return f'{self._last_name},{self._first_name}'
