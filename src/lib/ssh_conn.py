#coding utf8
import paramiko,threading,os,sys
class ssh_conn():
    def __init__(self):
        self.ssh=paramiko.SSHClient()
    def ssh2(self,ip,username,pwd,type):
        try:
            if type==1:
                key=paramiko.RSAKey.from_private_key_file(pwd)
                self.ssh.load_system_host_keys()
                self.ssh.connect(ip,22,username,pkey=key,timeout=10)
            else:
                self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh.connect(ip,22,username,pwd,timeout=5)
        except Exception,ex:
            print ex
    def close(self):
        self.ssh.close()
    def commmad(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        out=stdout.readlines()
        err=stderr.readlines()
        return out,err
    def main(self,ip,username,pwd,type,cmd):
        self.ssh2(ip, username,pwd,type)
        return self.commmad(cmd)
class ssh_sftp():
    def __init__(self):
        pass
    def ftp(self,ip,username,pwd,port,key,file):
        self.ssh=paramiko.Transport((ip,port))
        self.ssh.connect(username=username,password=pwd,pkey=key)
        sftp=paramiko.SFTPClient.from_transport(self.ssh)
        sftp.put(file,'/tmp/')
        