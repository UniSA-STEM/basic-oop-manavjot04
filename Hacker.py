"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Manavjot singh dutta
ID: 110430330
Username: dutmy005
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import CryptoToken
from Rig import Rig

class Hacker:
    def __init__(self, name):
        self._name = name
        self._inventory = [CryptoToken()]
        self._rig = None
        self._trace_level = 0
        self._trace_threshold = 5