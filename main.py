import time
from plyer import notification

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None, 
        timeout=10  
    )

def drink_water_reminder():
    while True:
        # Notify to drink water every hour
        notify("Drink Water Reminder", "It's time to drink a glass of water!")
        time.sleep(3600)

if __name__ == "__main__":
    drink_water_reminder()
