#!/usr/bin/env bash

if [ -z $2 ]; then
    nmcli d wifi connect $1
else
    nmcli d wifi connect $1 password $2
fi
