from client import app
from datetime import datetime as dt


def sendTimingMessage():
    now = dt.now().strftime("%H:%M")
    # enter the times you want the message to be sent. The time format must be 24hrs
    sendTimes = ["6:00", "9:15", "9:30", "9:40", "22:30"]
    for i in sendTimes:
        if i == now:
            app.send_message()
