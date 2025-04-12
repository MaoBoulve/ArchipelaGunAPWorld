# ArchipelaGunAPWorld
Revision AP World for Enter the Gungeon. Based on the prior work by KinTheInfinite (https://github.com/KinTheInfinite/Archipelago/releases).

## Required Software

- Enter The Gungeon
  - [Steam Store Page](https://store.steampowered.com/app/311690/Enter_the_Gungeon/)
  - [Epic Games Store](https://store.epicgames.com/en-US/p/enter-the-gungeon)
- [ArchipelaGun Mod](link TBD)

## Installation and Game Start Procedures

1. Install Enter The Gungeon through either Steam or Epic Games Store.
2. Use Thunderstore to install the Archipelago mod & dependency mods
   1. ArchipelaGun Mod (LINK TBD)
   2. Mod the Gungeon v1.8.4 (https://thunderstore.io/c/enter-the-gungeon/p/MtG_API/Mod_the_Gungeon_API/)
   3. Alexandria v0.4.9 (https://thunderstore.io/c/enter-the-gungeon/p/Alexandria/Alexandria/)
3. Start The Game Modded

# Joining a MultiWorld Game

* On run start, the Archipelagun will spawn. Fire to open the mod menu
 
 * Following commands are available:
 * connect (ip) (port) (slot name) --- [Connect to room. Space separated, without the parenthesis]
 * retrieve --- [Retrieve items from server, once per run ]
 * progress --- [Print out goals and current state of game completion]
 * apspawn --- [Debug spawn command  to spawn the next APItem]
 
 * fullconnect (ip) (port) --- [Workaround connection option for handling player names with spaces & rooms with passwords. Use with 'set'.]
 * set (option) --- [Replace 'option' with Name or Password. Set parameters for 'fullconnect']
