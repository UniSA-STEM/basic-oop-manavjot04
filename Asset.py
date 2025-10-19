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
    
    def __init__(self, name, description, encrypted=False):
        self._name = name
        self._description = description
        self._encrypted = encrypted

    @property
    def name(self): #This is for name of the asset
        return self._name

    @property
    def encrypted(self): #This for keeping the asset encrypted
        return self._encrypted

    @encrypted.setter
    def encrypted(self, value): 
        self._encrypted = value

    @abstractmethod
    def __str__(self):
        result = self._name + ": " + self._description
        if self._encrypted:
            result = result + " [Encrypted]"
        return result

class CryptoToken(Asset):
    def __init__(self, encrypted=False):
        super().__init__("CryptoToken", "Used to acquire or repair rigs.", encrypted)

    def __str__(self):
        return super().__str__()

class DataSpike(Asset):
    def __init__(self, encrypted=False): # The Asset that is to be used in battle to damage rig.
        super().__init__("DataSpike", "Used in battles.", encrypted)

    def __str__(self):
        return super().__str__()

class RemovableDrive(Asset): ##This used for gtting the things out of rig
    def __init__(self, encrypted=False):
        super().__init__("RemovableDrive", "Used for extraction.", encrypted)

    def __str__(self):
        return super().__str__()

class SecurityChip(Asset): #This is used to encrypt or decrypt asset
    def __init__(self, encrypted=False):
        super().__init__("SecurityChip", "Used to encrypt or decrypt assets.", encrypted)

    def __str__(self):
        return super().__str__()

class HardwarePatch(Asset): #This is for the upgration of the rigs
    def __init__(self, encrypted=False):
        super().__init__("HardwarePatch", "Used to upgrade rigs.", encrypted)

    def __str__(self):
        return super().__str__()
    

