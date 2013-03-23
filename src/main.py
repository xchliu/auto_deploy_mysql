from lib import ssh_conn,logs
import time
import config 
l=logs.Log()
c=config.GlobalConfig(1)
models={0:"GLOBAL",
        1:"CONNECTION",
        2:"TRANSFER",
        3:"CONFIG",
        4:"INSTALL"
        }
stats={1:"<< FINISHED >>",
       0:"<< FAILED >>"
       }
class interactive():
    def __init__(self,ip, username, pwd, port, key):
        self.ip=ip
        self.username=username
        self.pwd=pwd
        self.port=port
        self.key=key
        self.ftp=ssh_conn.ssh_sftp()
        self.ssh=ssh_conn.ssh_conn()
    def upload_file(self,file):
        return self.ftp.ftp(self.ip, self.username,self.pwd,self.port,self.key,file)
    def down_file(self,file):
        self.ftp.ftp(self.ip, self.username,self.pwd,self.port,self.key,file)
    def connect(self,cmd):
        result=self.ssh.ssh_connect(self.ip, self.username,self.pwd, 2,cmd)
        if not result:
            return False
        else:
            i=1
        #    for r in result[0]:
        #        l.log(models[1],r,3)
            for r in result[1]:
                l.log(models[1],r.strip("\n"),1)
                i=i+1
            if i>1:
                return False
            else:
                return True
    def connect_result(self,cmd):
        result=self.ssh.ssh_connect(self.ip, self.username,self.pwd, 2,cmd)
        if not result:
            return False
        else:
            #print result[1]
            return result[0]
def pre_config(inter):
    cmd='mkdir dbtools dbtools/backup  dbtools/init_server/ dbtools/up_file dbtools/down_file'
    inter.connect(cmd)
def check_server(inter):
    cmd='sudo netstat -lnpt|grep '+str(c.port)+'|wc -l'
    result=inter.connect_result(cmd)
    #print result[0],type(result[0]),cmd
    if int(result[0])==1:
        l.log(models[1],"Port %s has already be used!!!" % c.port,2)
        return False
    else:
        return True
def unstall(inter):
    cmd="sudo /bin/bash "+c.remote_path+"unstall_mysql_apt.sh"
    return inter.connect(cmd)
def user_manage(inter):
    l.log(models[3], "Grants users ....", 3)
    #root and users for management
    sql="delete from mysql.user where user='';\
         delete from mysql.user where user='root' and host<>'localhost';\
         grant select,super,replication client,lock tables,reload,show view on *.* to backup@'localhost' identified by 'backup';\
         grant super,replication slave,select on *.* to monitor@localhost identified by 'monitor';\
         grant replication slave on *.* to repl@'%' identified by 'repl';\
         flush privileges;\
    "
    if inter.connect("mysql -uroot  -e \"%s\"" % sql):
        l.log(models[3], "Done", 3)
        return True
    else:
        l.log(models[3], "Failed", 1)
        return False
    #dev and test accounts
    
    return True
    # init root password
def exits():
    l.log(models[0],"<<< END >>>\n\n",3)
    exit()
def main():
    #global config 
    if c.server_key == "":
        key=None
    else:
        key=c.server_key
    inter=interactive(c.server_ip,c.server_user,c.server_pwd,c.server_port,key)
    l.log(models[0],"<<< MESSAGE >>>",3)
    l.log(models[0], "Auto deploy MySQL Server on server %s" % c.server_name+":"+c.server_ip, 3)
   
    #check server is able to connect
    if not inter.connect('uname -a'):
        l.log(models[0], "Fail to connect to server ", 1)
        exits()
    else:
        l.log(models[0],"Success to connect to server", 3)
    pre_config(inter) 
    #transfer file to server
    l.log(models[2],"Upload files in folder: %s ....." % c.scripts_path,3) 
    if inter.upload_file(c.scripts_path):
        l.log(models[2],stats[1],3)
    else:
        l.log(models[2],stats[0],1)
        exits()
    #   
    if check_server(inter):
        pass
    else:
        if c.install_level==1:
            pass
            #exits()
        else:
            l.log(models[0],"Uninstall the server already running and  reinstall mysql server!!! ",2)
            unstall(inter)
    #run scripts on server  /bin/bash /tmp/auto_install_mysql_apt.sh
    l.log(models[3],"Install mysql server....",3)
    if c.install_type=='apt':
        script='auto_install_mysql_apt.sh'
    else:
        script='auto_install_mysql_source.sh'
    inter.connect("sudo /bin/bash "+c.remote_path+script)
    #check the mysql server is install completed
    l.log(models[3],"Check if the mysql service has been installed completed.",3)
    mysql_version=inter.connect_result("mysql -uroot -e 'select version()'")
    if mysql_version:
        l.log(models[3],"Done,Intalled Version:"+mysql_version[1].strip("\n"),3)
    else:
        l.log(models[3],stats[0],1)
        exits()
    #init mysql server configuration 
    l.log(models[3],"Config mysql server ...",3)
    r_conf=inter.connect("sudo /bin/bash "+c.remote_path+"general-config.sh")
    if r_conf:
        l.log(models[3],stats[1],3)
    else:
        l.log(models[3],stats[0],1)
        exits()
    #schema import and define  users
    time.sleep(60) 
    if not check_server(inter):
        l.log(models[3],"Import the db schema and grant users ..",3)
        user_manage(inter)
        r_manage=inter.connect("mysql -uroot   <"+c.remote_path+"db_schema.sql")
        if r_manage:
            l.log(models[3],stats[1],3)
        else:
            l.log(models[3],stats[0],1)
    else:
        l.log(models[3],"Service mysql failed to start after new config!! \n Abord to init schema and user grants!!!",1)
    exits()
if __name__=="__main__":
    main()