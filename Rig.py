"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Manavjot Singh Dutta
ID: 110430330
Username: dutmy005
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
from Asset import DataSpike, RemovableDrive, CryptoToken, SecurityChip, HardwarePatch

class Rig:
    
    def __init__(self, name):
        self._name = name
        self._damage = 0
        self._broken = False
        self._storage = [DataSpike(), DataSpike(), RemovableDrive()]
        self._upgrade_level = 0
        self._max_storage = 5 + self._upgrade_level * 2

    @property
    def name(self):
        return self._name

    @property
    def storage(self): #For the storage of the rig
        return self._storage

    @property
    def broken(self):#To chech if the rig is broken or not
        return self._broken

    def take_hit(self): #For the damage by the hit
        self._damage += 1
        if self._damage >= (2 + self._upgrade_level):
            self._broken = True

    def repair(self): #For the repair
        if self._damage > 0 or self._broken:
            self._damage = 0
            self._broken = False
            return True
        print(f"{self._name} does not need repair.")
        return False

    def upgrade(self): #To upgrade
        self._upgrade_level += 1
        self._max_storage = 5 + self._upgrade_level * 2
        print(f"{self._name} upgraded to level {self._upgrade_level}.")

    def generate_asset(self):
        if len(self._storage) >= self._max_storage:
            print(f"{self._name} storage full, cannot generate asset.")
            return None
        asset_types = [CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch]
        asset_class = random.choice(asset_types)
        new_asset = asset_class()
        self._storage.append(new_asset)
        print(f"Generated {new_asset.name} in {self._name}.")
        return new_asset

    def get_condition(self):
        if self._broken:
            return f"Broken (Level {self._upgrade_level})"
        elif self._damage == 0:
            return f"Pristine (Level {self._upgrade_level})"
        return f"Damaged ({self._damage}/{2 + self._upgrade_level}) (Level {self._upgrade_level})"

    def __str__(self):
        assets_str = ", ".join(str(asset) for asset in self._storage)
        return f"{self._name} - {self.get_condition()} - Stored: {assets_str}"
    

