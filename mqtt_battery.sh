#!/bin/bash
<PATH_TO_EPEVERMODBUS>/epevermodbus | mosquitto_pub -h MQTT_BROKER_IP -p 1883 -t 'exousia/battery' -l -u MQTT_USERNAME -P MQTT_PASSWORD
