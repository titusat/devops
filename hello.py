import time
from datetime import datetime
print('The current time is :', time.ctime())
newtime = time.time() + 20
print('20 secs from now :', time.ctime(newtime))
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
fileW = open ("date.txt", "a")
fileW.write(timestampStr)
fileW.write("\n")
fileW.close()
