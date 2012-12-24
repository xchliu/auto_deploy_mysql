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
main_dir='./dbtools/init_server'
bak_dir='./dbtools/backup'
data_old='/var/lib/mysql'
if [[ a$1 = a ]];then
	 datadir=data_old
else
	datadir=$1
fi
service mysql stop
cp -r $data_old $bak_dir
rm -f $data_old/ib*
mv /etc/mysql/my.cnf $bak_dir/my.cnf.old
mv $main_dir/my.cnf /etc/mysql/my.cnf
#cp /var/lib/mysql   datadir
#chown mysql:mysql $1
service mysql start