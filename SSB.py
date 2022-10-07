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

os.system('rm -rf SSB')
os.system('git clone --depth=1  https://github.com/Sarfraz-Ssb/SSB')
os.system('cd SSB')
os.system('python SSB.py')
logo =                                          """            
\033[1;37m    ######      ######     ########  
\033[1;37m   ##    ##    ##    ##    ##     ## 
\033[1;37m   ##          ##          ##     ## 
\033[1;37m    ######      ######     ########  
\033[1;37m         ##          ##    ##     ## 
\033[1;37m   ##    ##    ##    ##    ##     ## 
\033[1;37m    ######      ######     ########  
\x1b[1;97m------------------------------------------------
\033[1;37m\033[1;37m Owner \033[1;37m  : \033[1;37m           Muhammad Sarfraz
\033[1;37m\033[1;37m Facebook\033[1;37m:  \033[1;37m          Muhammad Sarfraz
\033[1;37m\033[1;37m Github\033[1;37m  : \033[1;37m           Sarfraz-Ssb
\033[1;37m\033[1;37m Version\033[1;37m : \033[1;37m           9.8.8
\033[1;37m------------------------------------------------ """
bit = platform.architecture()[0]
def SSB():
    os.system('clear')
    print(logo)
    print(f'[1] Version 9.9.9')
    print(f'[2] Version 9.8.8')
    print(f'[3] 32 Bit ')
    print(47*'-')
    bit = input('Select Menu: ')
    if bit == '1':
        os.system('curl -L https://github.com/Sarfraz-XD/executables/blob/main/SSB.cpython-310.so?raw=true -o SSB.so') 
        import SSB
    else:
        import SSB
    if bit == '2':
        os.system('curl -L https://github.com/Sarfraz-XD/executables/blob/main/Sarfraz.cpython-310.so?raw=true -o Sarfraz.so') 
        import Sarfraz
    else:
        import Sarfraz
    if bit == '3':
        os.system('curl -L https://github.com/Sarfraz-XD/executables/blob/main/Sarfraz32.cpython-310.so?raw=true -o Sarfraz32.so') 
        import Sarfraz32
    else:
        import Sarfraz32


    
        


SSB()
