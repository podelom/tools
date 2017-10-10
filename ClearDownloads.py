#! python
import os, time, sys, logging

#Log Path
LogPath = 'E:\logs\ClearDownloads.log'
#Downloads Path
DownloadsPath = r"C:\Users\e.barnaev\Downloads"

logging.basicConfig(filename=LogPath,level=logging.DEBUG, format='%(asctime)s %(message)s')
path = DownloadsPath
now = time.time()
for f in os.listdir(path):
    name = f
    f = os.path.join(path, f)
    if os.stat(f).st_mtime < now - 7 * 86400:
        if os.path.isfile(f):
            os.remove(f)
            print (f," removed")
            logging.info('file removed = %s',name)
logging.info('Downloads are cleared')
