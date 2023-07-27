import paramiko

# create ssh client 
ssh_client = paramiko.SSHClient()

# remote server credentials
host = "13.42.34.251"
username = "ec2-user"
password = "fish1234"
port = 22

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,port=port,username=username,password=password)

# create an SFTP client object
ftp = ssh_client.open_sftp()

# upload a file to the remote server
files = ftp.put("/Users/mavuwam/Documents/myprojects/tofetch/1.txt","/home/ec2-user/")

# close the connection
ftp.close()
ssh_client.close()