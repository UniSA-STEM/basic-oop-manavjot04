"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Manavjot singh dutta
ID: 110430330
Username: dutmy005
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch
from Rig import Rig

class Hacker:    
    def __init__(self, name):
        self._name = name
        self._inventory = [CryptoToken()]
        self._rig = None
        self._trace_level = 0
        self._trace_threshold = 5

    def acquire_rig(self, rig=None):
        if self._rig is not None:
            print(f"{self._name} already has a rig.")
            return False
        token = self._find_asset("CryptoToken", inventory=True, rig_storage=False)
        if token is None:
            print(f"{self._name} has no CryptoToken to acquire a rig.")
            return False
        self._rig = rig if rig else Rig(f"{self._name}'s Rig")
        print(f"{self._name} activates {self._rig.name}!")
        return True

    def _find_asset(self, name, inventory=True, rig_storage=False): # To find and remove an asset by name from inventory or rig storage.
        
        if inventory:
            for i, asset in enumerate(self._inventory):
                if asset.name == name:
                    return self._inventory.pop(i)
        if rig_storage and self._rig:
            for i, asset in enumerate(self._rig.storage):
                if asset.name == name:
                    return self._rig.storage.pop(i)
        return None

    def launch_data_spike(self, target_rig): #Launching a data spike at a target rig, thus increasing the trace.
        if self._trace_level > self._trace_threshold:
            print(f"{self._name}'s trace level ({self._trace_level}) exceeds threshold, action blocked.")
            return False
        if self._rig is None:
            print(f"{self._name} has no rig to launch from.")
            return False
        spike = self._find_asset("DataSpike", inventory=False, rig_storage=True)
        if spike is None:
            print(f"No DataSpike available in {self._rig.name}'s storage.")
            return False
        target_rig.take_hit()
        self._trace_level += 1
        print(f"{self._name} launches data spike at {target_rig.name}!")
        if target_rig.broken:
            print(f"{target_rig.name} is broken!")
        return True

    def extract_assets(self, target_rig): #Extracting the unsecured assets from a broken rig, thus increasing the trace.
        if self._trace_level > self._trace_threshold:
            print(f"{self._name}'s trace level ({self._trace_level}) exceeds threshold, action blocked.")
            return False
        if not target_rig.broken:
            print(f"{target_rig.name} is not broken.")
            return False
        if self._rig is None:
            print(f"{self._name} has no rig to extract with.")
            return False
        drive = self._find_asset("RemovableDrive", inventory=False, rig_storage=True)
        if drive is None:
            print(f"No RemovableDrive in {self._rig.name}'s storage.")
            return False
        extracted = [a for a in target_rig.storage if not a.encrypted]
        target_rig.storage[:] = [a for a in target_rig.storage if a.encrypted]
        self._inventory.extend(extracted)
        self._trace_level += len(extracted)
        print(f"{self._name} extracted {len(extracted)} unsecured assets from {target_rig.name}.")
        return True

    def encrypt_asset(self, asset): #Encrypting an asset using a SecurityChip.
        chip = self._find_asset("SecurityChip", inventory=True, rig_storage=True)
        if chip is None:
            print(f"{self._name} has no SecurityChip to encrypt.")
            return False
        asset.encrypted = True
        print(f"{self._name} encrypted {asset.name}.")
        return True

    def decrypt_asset(self, asset): #Decrypting an asset using a SecurityChip.
        chip = self._find_asset("SecurityChip", inventory=True, rig_storage=True)
        if chip is None:
            print(f"{self._name} has no SecurityChip to decrypt.")
            return False
        asset.encrypted = False
        print(f"{self._name} decrypted {asset.name}.")
        return True

    def upgrade_rig(self): #this Upgrades the hacker's rig using a HardwarePatch.
        if self._rig is None:
            print(f"{self._name} has no rig to upgrade.")
            return False
        patch = self._find_asset("HardwarePatch", inventory=True, rig_storage=False)
        if patch is None:
            print(f"{self._name} has no HardwarePatch in inventory.")
            return False
        self._rig.upgrade()
        return True

    def __str__(self):
        rig_name = self._rig.name if self._rig else "None"
        inventory_str = ", ".join(str(asset) for asset in self._inventory)
        return f"Hacker: {self._name}, Rig: {rig_name}, Trace: {self._trace_level}, Inventory: {inventory_str}"