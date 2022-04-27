import os, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from SSB import ssbbuy
    ssbbuy()
elif bit == '32bit':
    from SSB32 import ssbbuy
    ssbbuy()
