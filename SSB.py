import os, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
os.system('git pull')
bit = platform.architecture()[0]
if bit == '88bit':
    from SSB import ssbbuy
    ssbbuy()
elif bit == '13bit':
    from SSB32 import ssbbuy
    ssbbuy()
