import os
import sys
command = "zowe zos-jobs submit data-set 'RGOPALK.JCL.CNTL(WHELLO)' --view-all-spool-content"
#command = "zowe --version"
os.system(command)
