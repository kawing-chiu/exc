import os
import subprocess


print("pwd command:")
subprocess.call(['pwd'])
print("PWD environ varible:", os.environ['PWD'])
print("HOME environ varible:", os.environ['HOME'])
print("real user id:", os.getuid())
print("effective user id:", os.geteuid())
