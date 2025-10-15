"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Manavjot Singh Dutta
ID: 110430330
Username: Dutmy005
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from abc import ABC, abstractmethod

class Asset(ABC):
    
    def __init__(self, name, description, encrypted=False): #For initializing an asset 
        self._name = name
        self._description = description
        self._encrypted = encrypted

    @property
    def name(self): #This is for name of the asset
        return self._name

    @property
    def encrypted(self): #this for keeping the asset encrypted
        return self._encrypted

    @abstractmethod
    def __str__(self):
        result = self._name + ": " + self._description
        if self._encrypted:
            result = result + " [Encrypted]"
        return result