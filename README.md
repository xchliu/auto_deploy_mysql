auto_deploy_mysql
liuxc 2012-12
liu.xiaocheng0312@gmail.com
=================

auto init a new product's db servers and tools 

1.the user used to connect to server should be able to run sudo command without password.
	
2.all the file used to install will be upload in server folder:~/dbtools/.

3.the full version of mysql if the install type is apt-get. otherwise,you can specify which version to install where the type is source.


useage manual
===============
1.Download this project to local.th
2.make sure that the server doesn't have a mysql process is running on the same port which you want to install.At the same time,It will force install the mysql server and reinstall with new configuration or just reinstall mysql server agin depend on the config variable:self.install_level=2/1, whatever the value of the variable is ,It backup the data  dir to ./dbtools/backup
3.use a editor edit the config file name config.py ,modify the variable with correct value.
4.edit the my.cnf which will be affect on new server .actually,if you modify nothing,it work fine.
5.now,run the main.py as python scripts.the content of mysql_deploy.log tells you what hap end when the scripts try its best to deploy a mysql server with the infomation you has supplied.
6.check the server is running in which way you just wish.hope it's ok.