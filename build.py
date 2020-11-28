import os
import sys
command = "zowe zos-jobs submit data-set 'RGOPALK.JCL.CNTL(HELLO)' --view-all-spool-content"
#command = "zowe --version"
os.system(command)
