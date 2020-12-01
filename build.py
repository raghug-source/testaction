import os
import sys
from subprocess import PIPE, Popen
hostname = sys.argv[1]
hostport = sys.argv[2]
userid = sys.argv[3]
pwd = sys.argv[4]

command = "zowe zos-uss issue ssh /u/RGOPALK/runbuild.sh --host " + hostname +  ' --port ' + hostport + ' --user ' + userid + ' --password ' +  pwd
process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
print(process.communicate[0])


