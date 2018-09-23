# Transintentlation // Work In Progress...
======

## Usage as CLI:

By default, shows the commands to apply on a device to conform with the intended config :

``transintentlation intent.cfg running.cfg``

Example output : 
```
!====================================================================================================
!COMMANDS TO APPLY TO BE IN SYNC WITH THE INTENT CONFIG:
!====================================================================================================
!!CLEANINGS AND MODIFICATIONS
!---------------------------
no banner motd 
no hostname RUNNING_HOSTNAME
interface loopback0
 no ip address 172.18.0.6/23
 ip address 172.18.0.6/24
vlan 99
 no name VLAN_99
 name Production
vrf context management
 no ip route 0.0.0.0/0 10.10.20.254
 ip route 0.0.0.0/0 10.10.20.1
!---------------------------
!!NEW CONFIGS 
!---------------------------
banner motd ^
Hello Foreign passenger
^
hostname test_vars
interface Ethernet1/9
 ip address 11.22.33.44/24
!====================================================================================================
```


In addition, there are some options:

```bash
transintentlation --help

Usage: transintentlation [OPTIONS] INTENT_CONFIG RUNNING_CONFIG

  Show the commands to apply to be in sync with the intent config by
  default. Options can be used by passing --OPTION_NAME=True

Options:
  --missing BOOLEAN            Show only the missing config
  --additional BOOLEAN         Show only the additional config
  --apply_missing BOOLEAN      Show the commands to apply the missing config
  --delete_additional BOOLEAN  Show the commands to delete the additional
                               config
  --diff BOOLEAN               Show only the diff between the 2 configs
  --variables PATH             In case you provide a .j2 file as the
                               "intent_config", you can pass a variables YAML
                               file with this option
  --help                       Show this message and exit.

```

## Usage in Python: 







