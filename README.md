Documentation for auto_deploy_mysql 

liuxc 2012-12	liu.xiaocheng0312@gmail.com

Summary
=================
The main goal of this tool is deploy a new product environment  mysql server autonomously.
Tasks  will be done during the whole process:
1.Pre-config.A folder for server manage locate in the home folder,all the files used to install will be upload in server 
folder:~/dbtools/init_server/. and its structure would be :

	.
	|-- backup
	|   |-- my.cnf.old
	|   `-- mysql 
	|-- down_file
	|-- init_server
	|   |-- auto_install_mysql_apt.sh
	|   |-- auto_install_mysql_source.sh
	|   |-- db_schema.sql
	|   |-- general-config.sh
	|   |-- tool_list.py
	|   `-- unstall_mysql_apt.sh
	`-- up_file

2.Instal.There is two way to install mysql server:use apt-get or compile from the source code,which can be configured in the file config.py 
or variable install_type where initialize the class named GlobalConfig.

3.Config.A common config file (my.cnf) for mysql will replace the old one after the mysql has been installed successfully, and new file such as
idb* and the log files.all the origial file will be backup into folder backup.

4.DB initialize.No matter the file db_schema.sql is empty or not,we will run it to create the databases,tables,procedures,views and so on for the first time.
Thus，it's very import to make sure that the sqls have no syntax error.

5.By default ,unused user will delete from table user;the user root@localhost will be retained and other root related user will been drop away.
Users for manage such as monitor and backup will been created at the end of entire process.


Commands
=================
1.Python 2.7 is required,module paramiko and MySQLdb should be installed and will be used to connect to server.

2.The user used to connect to server should be able to run sudo command without password.
	
3.The full version of mysql should be specified if the install type is source-code. 

How to use
===============
1.Get code of this tool.

2.Make sure that the server doesn't have a mysql process is running on the same port which you want to install.
Even so,It will force unstall the mysql server and reinstall with new configuration or just reinstall mysql server again depend 
on the config variable:self.install_level=2/1, whatever the value of the variable is ,it backup the data  to ./dbtools/backup

3.Use a editor edit the config file name config.py ,modify the variable with correct value.

4.Edit the my.cnf which will be affect on new server .actually,if you modify nothing,it still work but I am worry about the performance.

5.Run the main.py as python scripts.the content of mysql_deploy.log tells you what is happening when the scripts try its best to deploy 
a mysql server with the configuration you has supplied.

6.Check the server is running in the way as you wish.Hope it's ok.
