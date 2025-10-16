"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Manavjot Singh Dutta
ID: 110430330
Username: dutmy005
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import DataSpike, RemovableDrive

class Rig:
    
    def __init__(self, name):
        self._name = name
        self._damage = 0
        self._broken = False
        self._storage = [DataSpike(), DataSpike(), RemovableDrive()]
        self._upgrade_level = 0
        self._max_storage = 5 + self._upgrade_level * 2
