#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/3017062245271082/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Sarfraz.so Sarfraz32.so SSB.so')
except:
    pass
os.system('rm -rf Sarfraz.so Sarfraz32.so SSB.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('SSB.so'):
        os.system('curl -L https://github.com/Sarfraz-XD/executables/blob/main/SSB.cpython-310.so?raw=true -o SSB.so') 
        import SSB
    else:
        import SSB
elif bit == '32bit':
    if not os.path.isfile('Sarfraz32.so'):
        os.system('curl -L https://github.com/Sarfraz-XD/executables/blob/main/Sarfraz32.cpython-310.so?raw=true -o Sarfraz32.so') 
        import Sarfraz32
    else:
        import Sarfraz32
