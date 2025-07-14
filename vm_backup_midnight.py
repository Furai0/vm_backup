
import time
from datetime import datetime
from vm_backup import vm_backup

while True:
    time.sleep(31)
    now = datetime.now()
    if now.hour == 3 and now.minute == 0:
        vm_backup()
