#!/bin/bash
#===============================================================================
#
#          FILE:  general-config.sh
#         USAGE:  sudo ./general-config.sh
#   DESCRIPTION:  general configuration after install mysql
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  sudo privileges is asked when running this script
#        AUTHOR:  xchliu
#       COMPANY:
#       VERSION:  1.0
#       CREATED:  12/20/2012
#      REVISION:  ---
#===============================================================================
if [[ a$1 = a ]];then
	 pass
else
	datadir=$1
fi
service mysql stop
mv /etc/mysql/my.cnf ./my.cnf.old
mv /tmp/my.cnf /etc/mysql/my.cnf 
#cp /var/lib/mysql   datadir
#chown mysql:mysql $1
service mysql start