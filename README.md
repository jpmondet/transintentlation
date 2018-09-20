#Transintentlation
======

[alt text](https://travis-ci.org/jpmondet/transintentlation "misc/transintentlation.svc")
[alt text](https://coveralls.io/r/jpmondet/transintentlation "https://coveralls.io/repos/jpmondet/transintentlation/badge.png)

**Work In Progress...**



##Usage as CLI:

By default, shows the commands to apply on a device to conform with the intended config :
``transintentlation intent.cfg n9k.cfg``

In addition, there are some options:
``transintentlation --help``
```
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




