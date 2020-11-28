import os
import time
import sys
# from zowe.zos_jobs_for_zowe_sdk import Jobs
# hostname = sys.argv[1]
# hostport = sys.argv[2]
# host = hostname + ':' + hostport
# userid = sys.argv[3]
# pwd = sys.argv[4]

# connection = {
#     "host_url": host,
#     "user": userid,
#     "password": pwd,
#     "ssl_verification": False
# }

# my_jobs = Jobs(connection)
# result = my_jobs.submit_from_mainframe('RGOPALK.JCL.CNTL(RUN)')
# time.sleep(15)
# rc = my_jobs.get_job_status(result['jobname'],result['jobid'])
# print(rc)
print(os.listdir('./'))
