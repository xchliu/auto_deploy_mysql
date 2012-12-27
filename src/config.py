class GlobalConfig():
    def __init__(self,type):
        #config for app itself
        self.install_type='apt'
        self.install_level=1    #1 install only   2 unstall if there is a mysql server is running on the same port
        self.remote_path='./dbtools/init_server/'
        self.log_path='/tmp/mysql_deploy.log'
        self.scripts_path='scripts/'
        if type == 1:
    #server base information
            self.project_name=''
            self.server_name='test'
            self.server_ip='10.2.25.2'
            self.server_user='ubuntu'
            self.server_pwd='ubuntu'
            self.server_key=''
            self.server_port=22
            self.server_role='master'
            #install configuration
            self.data_dir=''
            self.log_dir=''
            self.port=3306
        else:
            #get config from the backend database
            pass
        
        