import hashlib
from notify_run import Notify
import time
import datetime
import urllib
notify=Notify()

url = "http://www.dota2.com/news/updates/"   #Your URL here

sleeptime = 300    #sleeptime
def getHash():
    r = urllib.request.urlopen(url)
    the_page = r.read()
    return hashlib.sha224(the_page).hexdigest()
current_hash = getHash()      # much update needed here

while 1:
    if getHash() == current_hash:
        print('Nothing')
    else:
        notify.send(f"New Patch Out at {datetime.datetime.now()}")
        break
    time.sleep(sleeptime)
