import schedule
import time as tm
from datetime import time, timedelta, datetime

def job():
    print("Jesus Saves!")

#schedule.every().seconds.do(job)
#schedule.every().second.do(job) 'second' singular will just execute task every second
schedule.every().minutes.do(job) #'same with minutes'

while True:
    schedule.run_pending()
    tm.sleep(1)
    #tm.sleep(5) seconds


"""
import schedule
import time as tm
from datetime import time, timedelta, datetime

def job():
    print("Jesus Saves!")

schedule.every().seconds.do(job)

while True:
    schedule.run_pending()
    tm.sleep()
"""