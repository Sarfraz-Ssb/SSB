#coding=utf-8
import os, sys, platform

os.system('rm -rf Sarfraz.so Sarfraz32.so')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf Sarfraz.so Sarfraz32.so')
except:
    pass


bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Sarfraz.so'):
        os.system('curl -L https://github.com/SSB-143/executables/blob/main/Sarfraz.cpython-311.so?raw=true -o Sarfraz.so') 
        import Sarfraz
    else:
        import Sarfraz

elif bit == '32bit':
    if not os.path.isfile('Sarfraz32.so'):
        os.system('curl -L https://github.com/SSB-143/executables/blob/main/Sarfraz32.cpython-311.so?raw=true -o Sarfraz32.so') 
        import Sarfraz32
    else:
        import Sarfraz32
