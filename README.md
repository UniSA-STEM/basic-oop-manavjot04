My assignment Overview

This project is a Python-based cyberpunk hacking simulation and it simulates a hacking environment where hackers manage rigs and assets to perform actions like attacking, extracting, and encrypting data. 

Author: Manavjot singh dutta , ID: 110430330

Project Structure

Asset.py: Defines an abstract Asset class with subclasses (CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch). Manages asset properties like _encrypted and a simplified __str__ method for readable output.

Rig.py: Represents a hacker’s computer with attributes (_damage, _storage, _upgrade_level) and methods for upgrading, repairing, and generating assets.

Hacker.py: Implements the main actor, managing inventory, rig, and trace level. Handles actions like launching data spikes, extracting assets, and encryption.

Main.py: Contains 16 test functions to verify core functionalities.

Features

Encrypted Assets: Assets have an _encrypted boolean, toggled via Hacker.encrypt_asset and decrypt_asset using a SecurityChip. Encrypted assets cannot be stored or retrieved, ensuring security.

Trace Level: Tracks hacking exposure in Hacker (_trace_level, threshold 5). Increases for actions like launch_data_spike (+1) or extract_assets (+number of assets). Blocked if above threshold; reduced by 2 with reduce_trace.

Rig Level: Managed via Rig._upgrade_level, increasing storage capacity (5 + level*2) and damage threshold (2 + level) via upgrade.

Tests: Comprehensive scenarios in Main.py, including core actions (e.g., test_acquire_rig, test_launch_data_spike) and many more