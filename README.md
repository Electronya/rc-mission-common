# rc-mission-common
Collection common packages used by multiple RC mission softwares ((commander, operator))

![test](https://github.com/Electronya/rc-mission-common/actions/workflows/test.yml/badge.svg)
[![coverage](https://codecov.io/gh/Electronya/rc-mission-common/branch/main/graph/badge.svg?token=WEAWM1E3HZ)](https://codecov.io/gh/Electronya/rc-mission-common)

## List of packages
 - messages
 - mqttClient

## Setting symlink in base repo
```
ln -s ../../rc-mission-common/src/pkgs/messages src/pkgs/messages
ln -s ../../rc-mission-common/src/pkgs/mqttClient src/pkgs/mqttClient
```
