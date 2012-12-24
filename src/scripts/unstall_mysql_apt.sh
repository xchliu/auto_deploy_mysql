#!/bin/bash
#apt-get autoremove --purge mysql-server
apt-get remove mysql-server -y
apt-get autoremove mysql-server -y
apt-get remove mysql-common -y
