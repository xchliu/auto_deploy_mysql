#!/bin/bash
#===============================================================================
#
#          FILE:  auto_install_mysql_source.sh
#         USAGE:  sudo ./auto_install_mysql_source.sh
#   DESCRIPTION:  auto install mysql-server with apt-get 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  sudo privileges is asked when running this script
#        AUTHOR:  xchliu
#       COMPANY:
#       VERSION:  1.0
#       CREATED:  03/13/2012
#      REVISION:  ---
#===============================================================================
# define the variables
prefix_dir=/mysql3308
data_dir=/data3308
port=3308
#log_dir=/var/log/mysql
set_file=mysql-5.5.21
tar_file=mysql-5.5.21.tar.gz
version=MySQL-5.5

#check user
if [ $(id -u) -ne  0 ];then
	echo -e "\033[31;5m Error:you should run this script as root!!\033[0m"
	exit 1
fi
# add user
if [ -z "$(id mysql &>/dev/null)" ];then
  echo "user mysql already exist."
else 
  `groupadd mysql`
  `useradd mysql -d /dev/null -s /sbin/nologin -M -g mysql mysql`
fi

# check the dir
if [ -d $prefix_dir ];then
   echo "$prefix_dir is alreadly exist."
else
   `mkdir $prefix_dir`
fi
if [ -d $data_dir ];then
   echo "$data_dir is alreadly exist."
else
   `mkdir $data_dir`
fi
if [ -d $log_dir ];then 
   echo "$log_dir is alreadly exist."
else
    mkdir $log_dir
fi
  
# set up the relay package
for packages in ncurses-dev  g++ libtool bison chkconfig cmake;
# g++-4.3 g++-4.3-multilib libtool ; 
#libtool-libs;
do 
	echo -e "\033[32;5m ##########install $packages now, wait,,,,,\033[0m"
	apt-get install $packages;
done
#get the setup packeget
if [ -f $tar_file ];then
   echo use the exist tar file.
else
wget http://mysql.cdpa.nsysu.edu.tw/Downloads/$version/$tar_file
fi
# start install
if [ -d $set_file ];then
rm -rf $set_file
fi
if [ -f $tar_file ]; then 
	`tar -zvxf $tar_file`
   	cd $set_file
	pwd	
	cmake -DCMAKE_INSTALL_PREFIX=$prefix_dir/ -DMYSQL_DATADIR=$data_dir -DMYSQL_UNIX_ADDR=$prefix_dir/mysqld.sock -DWITH_INNOBASE_STORAGE_ENGINE=1 -DENABLED_LOCAL_INFILE=1 -DMYSQL_TCP_PORT=$port -DEXTRA_CHARSET=ALL -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DMYSQL_USER=mysql 	
	echo -e "\033[32;5m #########begin install ,,,,, \033[0m"
	make && make install
else
    echo -e "\033[31;5m setup tar file doesn't exist!\033[0m"
    exit 1
fi

# do the other config after make install
cp ./support-files/my-large.cnf $prefix_dir/my.cnf
$prefix_dir/scripts/mysql_install_db --user=mysql --basedir=$prefix_dir --datadir=$data_dir
# --defaults-file=$prefix_dir/my.cnf --pid-file=$prefix_dir/mysql.pid
chown -R mysql:mysql $prefix_dir
chown -R mysql:mysql $data_dir
chown -R mysql:mysql $log_dir
$prefix_dir/bin/mysqld_safe --defaults-file=$prefix_dir/my.cnf --user=mysql &

cp ./support-files/mysql.server /etc/init.d/mysql5
chmod 755 /etc/init.d/mysql5
chkconfig -add mysql3308
chkconfig mysql3308 on


#my.cnf
echo "please config the my.cnf file!"

