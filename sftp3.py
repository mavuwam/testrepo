import paramiko

host = "13.42.49.38"
username = "ec2-user"
password = "fish1234"
file_name = '1.txt'

port = 22
transport = paramiko.Transport((host, port))

destination_path = "/home/ec2-user/"+file_name
local_path = "/Users/mavuwam/Documents/myprojects/tofetch/"+file_name #if using google colab, this will work with no modifications. Otherwise, overwrite with your local file path to the file

transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put(local_path, destination_path)

sftp.close()
transport.close()