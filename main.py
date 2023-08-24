from client import app
from datetime import datetime as dt


def sendTimingMessage(message: str):
    now = dt.now().strftime("%H:%M")
    # enter the times you want the message to be sent. The time format must be 24hrs
    send_times = ["6:00", "9:15", "9:30", "9:40", "22:30", "22:41"]
    # for i in send_times:
    #     if i == str(now):

    app.send_message(chat_id="507720349", text=message)


if __name__ == "__main__":
    sendTimingMessage("Test-1")
