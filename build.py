# import os
# import sys
# from subprocess import PIPE, Popen
import paramiko
hostname = sys.argv[1]
hostport = sys.argv[2]
userid = sys.argv[3]
pwd = sys.argv[4]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname,username=userid, password=pwd)
cmd_to_execute = 'cd /u/RGOPALK;ls'
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
print(ssh_stdout.read())

