class user_command():
    def __init__(self):
        pass
        self.monitor="grant super,replication slave,select on *.* to monitor@'localhost' identified by 'monitor'"
        self.backuper="grant select,super,replication client,lock tables,reload,show view on *.* to backup@'localhost' identified by 'backup'"
        self.replicator="grant replication slave on *.* to repl@'%' identified by 'repl'"

