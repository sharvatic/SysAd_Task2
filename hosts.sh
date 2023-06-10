#!/bin/bash
echo "Please enter the v4 ip address of your system"
read input
echo "Please enter your password"
sudo echo "$input gamma-z.hm" >> /etc/hosts
