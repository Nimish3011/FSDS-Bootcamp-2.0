# 2. Write a Python program to find out what version of Python you are using.

#imports the "sys" module its provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. 
#It is always available.

import sys 
print("Python Version : ", sys.version)
print("Version Info : ", sys.version_info)

import platform
print("Platform Version : ", platform.python_version())

print("Python version as tuple :", platform.python_version_tuple())