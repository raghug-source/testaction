import os
import sys
import subprocess
command = "zowe zos-uss issue ssh /u/RGOPALK/runbuild.sh"
# #command = "zowe --version"
x = os.system(command)
print(x)

