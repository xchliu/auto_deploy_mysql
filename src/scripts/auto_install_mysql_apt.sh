#!/bin/bash
#===============================================================================
#
#          FILE:  auto_install_mysql_apt.sh
#         USAGE:  sudo ./auto_install_mysql_apt.sh
#   DESCRIPTION:  auto install mysql-server with apt-get 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  sudo privileges is asked when running this script
#        AUTHOR:  xchliu
#       COMPANY:
#       VERSION:  1.0
#       CREATED:  12/18/2012
#      REVISION:  ---
#===============================================================================
apt-get update
export DEBIAN_FRONTEND=noninteractive
apt-get -q -y install mysql-server
service mysql stop