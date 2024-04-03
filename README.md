## Important Note

For some reason, windows defender might falsy detect this as a Wacatac Trojan.
Add the directory containing the files you downloaded, to remedy this issue, as defender might delete the files.

If you don't feel comfortable with the provided binaries, you can take a look at the code and compile it yourself. (instructions on how to compile below)

## Description

This is a simple macro execution script used to quickly execute strategem actions in Helldivers 2.
This was mainly created with the loupedeck in mind, but it can also be used by other macro software and hardware, in the same fashion.

## Setup

Download the necessary files from the releases section and extract them ina directory of your choice.<br>
A recommended option is C:\helldivers because it will make it easier for setting up loupedeck actions.

## Configuration

You can modify the sequence keys to any key that you desire.
> Meaning you can for example bind the [Up, Down, Left, Right, stratagem_open] keys to any other key, like WASD and Alt, depending on what you use in-game.

To modify the key bindings, simply run the  configuration.exe file and follow the prompts.

## LoupeDeck setup

In loupedeck, create a new "Run command" action.

- Directly on the tile

  ![loupedeck_create_action_from_tile](./readme_media/loupedeck_create_action_from_tile.png)

Or

- From the sidebar

  ![loupedeck_create_action_from_sidebar](./readme_media/loupedeck_create_action_from_sidebar.png)


Select the stratagems.exe file and add key corresponding to the stratagem you want to trigger, as a parameter.<br>
**keys for the stratagems can be referenced in the codes.json file**

![run_action_dialog](./readme_media/run_action_dialog.png)

**! For non-loupedeck users !**<br>
When using this script with something other than the loupedeck, make sure to omit the double pipe **||** when adding the parameter.

---
## Strategems
| Engineering Bay          | Patriotic Administration Center| General Stratagems    | Robotics Workshop             | Orbital Cannons           | Hanger                   | Suits    |
|--------------------------|----------------------|-----------------------|-------------------------|---------------------------|--------------------------|--------------------------|
| jump_pack                | machine_gun          | reinforce             | hmg_emplacement         | orbital_gatling_barrage   | eagle_strafing_run       | patriot_exosuit          |
| supply_pack              | antimaterial_rifle   | sos_beacon            | shield_generator        | orbital_airburst_strike   | eagle_airstrike          |                          |
| guard_dog_rover          | stalwart             | resupply              | tesla_tower             | orbital_120mm_barrage     | eagle_cluster_bomb       |                          |
| ballistic_shield         | expendable_anti_tank | hellbomb              | antipersonnel_minefield | orbital_380mm_barrage     | eagle_napalm_airstrike   |                          |
| shield_generator_pack    | recoilless_rifle     | sssd_delivery         | incendiary_mines        | orbital_walking_barrage   | eagle_smoke_strike       |                          |
| guard_dog                | flame_thrower        | seismic_probe         | machine_gun_sentry      | orbital_laser             | eagle_110mm_rocket_pods  |                          |
|                          | autocannon           | upload_data           | gatling_sentry          | orbital_railcannon_strike | eagle_500kg_bomb         |                          |
|                          | railgun              | illumination_flare    | mortar_sentry           | orbital_precision_strike  | eagle_rearm              |                          |
|                          | spear_launcher       |                       | autocannon_sentry       | orbital_gas_strike        |                          |                          |
|                          | grenade_launcher     |                       | rocket_sentry           | orbital_ems_strike        |                          |                          |
|                          | laser_cannon         |                       | ems_mortar_sentry       | orbital_smoke_strike      |                          |                          |
|                          | heavy_machine_gun    |                       |                         |                           |                          |                          |
|                          | quasar_cannon        |                       |                         |                           |                          |                          |


## Single key - No menu toggle

You can use single key actions, as "up" or "down", if you want to assign arrow functions to your loupedeck.
or you can define a key sequence that does not engage the menu open key.

To define a single action, just add an entry to the codes.json with a single key (menu will be omitted automatically).
For the sequence, you have to add the **NM** flag in the sequence.
For example: 
```json
"up": "U",
"down": "D"
"custom_sequence": "NM U D R R L"
```

>You can disable the menu toggle action globally by using the **none** value for **open_mode** in config.ini


## Icons

To get all icons for the stratagem actions, you can either:
- Download the [Streamdeck Helldivers 2 Stratagem plugin](https://marketplace.elgato.com/product/helldivers-2-stratagem-0c648333-25a0-403f-9894-22c5f6b1ff89), which provides all icons in the zip,
- Get the SVGs from **@nvigneux 's** [Helldivers-2-Stratagems-icons-svg](https://github.com/nvigneux/Helldivers-2-Stratagems-icons-svg?tab=readme-ov-file) repository

## Compiling (optional)

### Requirements
- Windows
- Python 3.12
- pipenv
- Ability to run Makefiles on Windows (Recommend chocolatey to install make)

### Compiling
Clone the repo locally and run ```make build```

**Now go spread some democracy, soldier!**
