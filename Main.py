"""
File: main.py
Description: Tests the Hacker, Rig, and Asset classes through various scenarios.
Author: Manavjot Singh Dutta
ID: 110430330
Username: Dutmy005
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
from Hacker import Hacker
from Rig import Rig
from Asset import CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch

def test_acquire_rig():
    print("\n--- Test Acquire Rig ---")
    hacker = Hacker("Shadow")
    print(hacker)
    hacker.acquire_rig()
    print(hacker)
    print(hacker._rig)

def test_acquire_rig_no_token():
    print("\n--- Test Acquire Rig No Token ---")
    hacker = Hacker("Ghost")
    hacker._inventory = []
    hacker.acquire_rig()

def test_upgrade_rig():
    print("\n--- Test Upgrade Rig ---")
    hacker = Hacker("Neo")
    hacker.acquire_rig()
    hacker._inventory.append(HardwarePatch())
    hacker.upgrade_rig()
    print(hacker._rig)

def test_upgrade_no_rig():
    print("\n--- Test Upgrade No Rig ---")
    hacker = Hacker("Trinity")
    hacker.upgrade_rig()

def test_upgrade_no_patch():
    print("\n--- Test Upgrade No Patch ---")
    hacker = Hacker("Morpheus")
    hacker.acquire_rig()
    hacker.upgrade_rig()

def test_launch_data_spike(): 
    print("\n--- Test Launch Data Spike ---")
    attacker = Hacker("Blade")
    attacker.acquire_rig()
    defender_rig = Rig("Target Rig")
    attacker.launch_data_spike(defender_rig)
    print(defender_rig)
    attacker.launch_data_spike(defender_rig)
    print(defender_rig)

def test_extract_assets():  # To Test extracting assets from a broken rig.
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

def test_extract_not_broken(): #To extract the assets from broken rig
    print("\n--- Test Extract Not Broken ---")
    attacker = Hacker("Deck")
    attacker.acquire_rig()
    defender_rig = Rig("Safe Rig")
    attacker.extract_assets(defender_rig)

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

def test_encrypt_no_chip(): #Here testing encryption without a chip
    print("\n--- Test Encrypt No Chip ---")
    hacker = Hacker("Lock")
    hacker.acquire_rig()
    asset = HardwarePatch()
    hacker._inventory.append(asset)
    hacker.encrypt_asset(asset)

def test_high_trace_block(): #Here testing the actions that are blocked by high trace levels
    print("\n--- Test High Trace Block ---")
    hacker = Hacker("Trace")
    hacker.acquire_rig()
    hacker._trace_level = 6
    defender_rig = Rig("Trace Target")
    hacker.launch_data_spike(defender_rig)

def test_generate_asset():
    print("\n--- Test Generate Asset ---")
    hacker = Hacker("Gen")
    hacker.acquire_rig()
    generated = hacker._rig.generate_asset()
    print(f"Generated: {generated}")
    print(hacker._rig)

def test_repair_rig(): # Test to repair a rig
    print("\n--- Test Repair Rig ---")
    hacker = Hacker("Fix")
    hacker.acquire_rig()
    hacker._rig.take_hit()
    hacker._rig.take_hit()
    print(hacker._rig)
    hacker._inventory.append(CryptoToken())
    hacker.repair_rig()
    print(hacker._rig)

def test_store_retrieve():
    print("\n--- Test Store/Retrieve ---")
    hacker = Hacker("Storage")
    hacker.acquire_rig()
    asset = CryptoToken()
    hacker._inventory.append(asset)
    hacker.store_asset(asset)
    print(hacker)
    print(hacker._rig)
    hacker.retrieve_asset(asset)
    print(hacker)
    print(hacker._rig)

def test_store_encrypted():
    print("\n--- Test Store Encrypted ---")
    hacker = Hacker("SecureStore")
    hacker.acquire_rig()
    asset = CryptoToken(encrypted=True)
    hacker._inventory.append(asset)
    hacker.store_asset(asset)

def test_trace_from_transfers():
    print("\n--- Test Trace from Transfers ---")
    hacker = Hacker("TransferTrace")
    hacker.acquire_rig()
    chip = SecurityChip()
    hacker._inventory.append(chip)
    hacker.store_asset(chip)
    print(f"Trace after store: {hacker._trace_level}")

def test_reduce_trace():
    print("\n--- Test Reduce Trace ---")
    hacker = Hacker("Stealth")
    hacker.acquire_rig()
    hacker._trace_level = 4
    hacker._inventory.append(SecurityChip())
    hacker.reduce_trace()
    print(f"Trace after reduction: {hacker._trace_level}")
    hacker.reduce_trace()

if __name__ == "__main__":
    test_acquire_rig()
    test_acquire_rig_no_token()
    test_upgrade_rig()
    test_upgrade_no_rig()
    test_upgrade_no_patch()
    test_launch_data_spike()
    test_extract_assets()
    test_extract_not_broken()
    test_encrypt_decrypt()
    test_encrypt_no_chip()
    test_high_trace_block()
    test_generate_asset()
    test_repair_rig()
    test_store_retrieve()
    test_store_encrypted()
    test_trace_from_transfers()
    test_reduce_trace()