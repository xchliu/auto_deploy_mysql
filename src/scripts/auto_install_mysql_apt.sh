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
#dpkg --remove mysql-server mysql-server-5.5
#rm -f /var/lib/dpkg/info/mysql*
apt-get update -f -qq
#apt-get upgrade -y
export DEBIAN_FRONTEND=noninteractive
apt-get -q -y -qq install mysql-server
