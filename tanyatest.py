import os
import pysftp
import time
import datetime
import paramiko

billingPath = '.' 
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

class My_Connection(pysftp.Connection):
    def __init__(self, *args, **kwargs):
        self._sftp_live = False
        self._transport = None
        super().__init__(*args, **kwargs)

try:
     while True:
            print(datetime.datetime.now())
            os.chdir(billingPath)
            files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
            lastFive = list([])
            lastFive = files[-5:]
            print(lastFive)
            with pysftp.Connection('18.134.135.166', username='ec2-user', password='fish1234') as sftp:
                for file in lastFive:
                    print(file)
                    if file[0:9]=='PayPoint_':
                        print('is moving')
                        sftp.put(os.path.join(billingPath,file))
            print(time.sleep)
            time.sleep(60*60*24)
        
except paramiko.ssh_exception.SSHException as e:
    print('SSH error, you need to add the public key of your remote in your local known_hosts file first.', e)
