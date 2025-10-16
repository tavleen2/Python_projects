import time
from plyer import notification

while True:
    notification.notify(title = "Reminder!",
                        message = "You need to drink water",
                        app_name = "HydrateMe",
                        timeout = 10)
    print("Notification sent!")
    time.sleep(60*60)