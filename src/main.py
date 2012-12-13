from lib import ssh_conn

def main():
    ssh=ssh_conn.ssh_conn()
    result=ssh.main('10.2.1.218', 'ubuntu','ubuntu', 2, 'free')
    if result[1]=='':
        print result[1]
    else:
        print result[0]
    ftp=ssh_conn.ssh_sftp()
    ftp.ftp('10.2.1.218', 'ubuntu', 'ubuntu', 22, None, '/tmp/1')
    
if __name__=="__main__":
    main()