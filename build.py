import os
import sys
from subprocess import PIPE, run
hostname = sys.argv[1]
hostport = sys.argv[2]
userid = sys.argv[3]
pwd = sys.argv[4]

command = "zowe zos-uss issue ssh /u/RGOPALK/runbuild.sh --host " + hostname +  ' --port ' + hostport + ' --user ' + userid + ' --password ' +  pwd
result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
print(result.stdout)


