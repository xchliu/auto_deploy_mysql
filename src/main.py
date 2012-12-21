import os,logging
from lib import ssh_conn,logs
import config 
l=logs.Log()
c=config.GlobalConfig()
models={0:"GLOBAL.PROCESS",
        1:"CONNECTION.PROCESS",
        2:"FILE.TRANSFER",
        3:"CONFIG.INSTALL"
        }
stats={1:"FINISHED",
       0:"FAILED"
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
            for r in result[1]:
                l.log(models[1],r,1)
                i=i+1
            for r in result[0]:
                l.log(models[1],r,3)
            if i>1:
                return False
            else:
                return True

def main():
    #global config 
    if c.server_key == "":
        key=None
    else:
        key=c.server_key
    inter=interactive(c.server_ip,c.server_user,c.server_pwd,c.server_port,key)
    l.log(models[0], "Auto deploy MySQL Server on server %s" % c.server_name, 3)
   
    #check server is able to connect
    if not inter.connect('uname -a'):
        l.log(models[0], "Fail to connect to server ", 1)
        return
    else:
        pass
        l.log(models[0],"Success to connect to server", 3) 
    #transfer file to server
    l.log(models[2],"Upload files in folder: %s ....." % c.scripts_path,3) 
    if inter.upload_file(c.scripts_path):
        l.log(models[2],stats[1],3)
    else:
        l.log(models[2],stats[0],1)
        return    
    #run scripts on server  /bin/bash /tmp/auto_install_mysql_apt.sh
    l.log(models[3],"Install mysql server....",3)
    if c.install_type=='apt':
        script='auto_install_mysql_apt.sh'
    else:
        script='auto_install_mysql_source.sh'
    inter.connect("sudo /bin/bash "+c.remote_path+script)
    #check the mysql server is install completed
    
    l.log(models[3],stats[1],3)
    #init mysql server configuration 
    l.log(models[3],"Config mysql server ...",3)
    inter.connect("sudo /bin/bash /tmp/general-config.sh")
    l.log(models[3],stats[1],3)
    #schema import and define  users 
    l.log(models[3],"Import the db schema and grant users ..",3)
    inter.connect("mysql -uroot   </tmp/db_schema.sql")
    l.log(models[3],stats[1],3)
if __name__=="__main__":
    main()