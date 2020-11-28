import os
import time
import sys
from zowe.zos_jobs_for_zowe_sdk import Jobs
from zowe.zos_files_for_zowe_sdk import Files
hostname = sys.argv[1]
hostport = sys.argv[2]
host = hostname + ':' + hostport
userid = sys.argv[3]
pwd = sys.argv[4]

connection = {
    "host_url": host,
    "user": userid,
    "password": pwd,
    "ssl_verification": False
}
my_files = Files(connection)
##################################################################
basepath = './'
folders = os.listdir(basepath)
ignored = ['.git','.github']
#print(dir)
for folder in folders:
    path = os.path.join(basepath,folder)
    if os.path.isdir(path):
        if folder not in ignored:
            pdstype = folder
            for file in os.listdir(path):
                memname = file.split('.')[0]
                localfile = './' + folder + '/' + file
                pdsname = 'RGOPALK.RAG.' + pdstype + '(' + memname + ')'
                my_files.upload_file_to_dsn(localfile,pdsname)
##########################################################################
# my_jobs = Jobs(connection)
# result = my_jobs.submit_from_mainframe('RGOPALK.JCL.CNTL(RUN)')
# time.sleep(15)
# rc = my_jobs.get_job_status(result['jobname'],result['jobid'])
# print(rc)

