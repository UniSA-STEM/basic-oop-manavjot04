"""
File: main.py
Description: <A brief description of this Python module.>
Author: Manavjot Singh Dutta
ID: 110430330
Username: Dutmy005
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
from Hacker import Hacker
from Rig import Rig
from Asset import CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch

random.seed(42)

def test_acquire_rig():
    print("\n--- Test Acquire Rig ---") #To test the rig
    hacker = Hacker("Shadow")
    print(hacker)
    hacker.acquire_rig()
    print(hacker)
    print(hacker._rig)

def test_acquire_rig_no_token(): # To Test the acquiring of rig without a CryptoToken.
    print("\n--- Test Acquire Rig No Token ---")
    hacker = Hacker("Ghost")
    hacker._inventory = []
    hacker.acquire_rig()

def test_upgrade_rig(): # To Test the upgrading a rig with a HardwarePatch.
    print("\n--- Test Upgrade Rig ---")
    hacker = Hacker("Neo")
    hacker.acquire_rig()
    hacker._inventory.append(HardwarePatch())
    hacker.upgrade_rig()
    print(hacker._rig)

def test_upgrade_no_rig(): # To Test the upgrading without a rig.
    print("\n--- Test Upgrade No Rig ---")
    hacker = Hacker("Trinity")
    hacker.upgrade_rig()

def test_upgrade_no_patch(): # To Test the upgrading without a HardwarePatch.
    print("\n--- Test Upgrade No Patch ---")
    hacker = Hacker("Morpheus")
    hacker.acquire_rig()
    hacker.upgrade_rig()

def test_launch_data_spike(): # To Test launching data spikes to damage and break a rig.
    print("\n--- Test Launch Data Spike ---")
    attacker = Hacker("Blade")
    attacker.acquire_rig()
    defender_rig = Rig("Target Rig")
    attacker.launch_data_spike(defender_rig)
    print(defender_rig)
    attacker.launch_data_spike(defender_rig)
    print(defender_rig)

def test_extract_assets(): # To Test extracting assets from a broken rig.
    print("\n--- Test Extract Assets ---")
    attacker = Hacker("Runner")
    attacker.acquire_rig()
    defender_rig = Rig("Victim Rig")
    defender_rig.take_hit()
    defender_rig.take_hit()
    secure_asset = SecurityChip(encrypted=True)
    defender_rig._storage.append(secure_asset)
    defender_rig._storage.append(CryptoToken())
    attacker.extract_assets(defender_rig)
    print(attacker)
    print(defender_rig)

def test_encrypt_decrypt():
    print("\n--- Test Encrypt/Decrypt ---")
    hacker = Hacker("Cipher")
    hacker.acquire_rig()
    hacker._inventory.append(SecurityChip())
    asset = DataSpike()
    hacker._inventory.append(asset)
    hacker.encrypt_asset(asset)
    print(asset)
    hacker._inventory.append(SecurityChip())
    hacker.decrypt_asset(asset)
    print(asset)

if __name__ == "__main__":
    test_acquire_rig()
    test_acquire_rig_no_token()
    test_upgrade_rig()
    test_upgrade_no_rig()
    test_upgrade_no_patch()
    test_launch_data_spike()
    test_extract_assets()
    test_encrypt_decrypt()