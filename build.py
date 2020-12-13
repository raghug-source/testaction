# import os
import sys
# from subprocess import PIPE, Popen
import paramiko
hostname = sys.argv[1]
hostport = sys.argv[2]
userid = sys.argv[3]
pwd = sys.argv[4]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname,username=userid, password=pwd)
cmd_to_execute = 'cd /u/RGOPALK/zappbuild'
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
print(ssh_stdout.read())
cmd_to_execute = 'git clone --branch feature2 git@github.com:raghug-source/testaction.git'
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
print(ssh_stdout.read())
cmd_to_execute = '. /etc/profile \n cd /u/RGOPALK/zappbuild/ \n git clone --branch feature2 git@github.com:raghug-source/testaction.git \n /usr/lpp/IBM/dbb/bin/groovyz /u/RGOPALK/zappbuild/origbuild.groovy --workspace /u/RGOPALK/zappbuild --application testaction --outDir /u/RGOPALK/zappbuild/out --hlq RGOPALK.RAG --fullBuild'
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
output_msg = ssh_stdout.read()
print(output_msg)
if '** Build State : ERROR' in output_msg:
    raise SystemExit('Error: Build Ended in Error')
