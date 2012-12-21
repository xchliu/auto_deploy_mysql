class GlobalConfig():
    def __init__(self):

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
        
        
        #config for app itself
        self.install_type='apt'
        self.remote_path='./dbtools/init_server/'
        self.log_path='/tmp/mysql_deploy.log'
        self.scripts_path='scripts/'