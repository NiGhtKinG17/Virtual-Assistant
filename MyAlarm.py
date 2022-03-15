import datetime
import winsound

from cv2 import HoughCircles

def alarm(time):
    
    altime = str(datetime.datetime.now().strptime(time,"%I:%M %p"))
    
    altime = altime[11:-3]
    
    curHr = altime[:2]
    curHr = int(curHr)
    curMin = altime[3:5]
    curMin = int(curMin)
    print(f"Alarm set for {time}")
    
    while True:
        if curHr == datetime.datetime.now().hour:
            if curMin == datetime.datetime.now().minute:
                print('Alarm')
                winsound.PlaySound('abc',winsound.SND_LOOP)
            elif curMin<datetime.datetime.now().minute:
                break
        
    