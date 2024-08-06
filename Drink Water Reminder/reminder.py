from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Drink Water",
            message="Hello, drink water pls.",
            app_icon="E:\Work\Python Projects\Drink Water Reminder\waterglass.ico",
            timeout=15
            )
        time.sleep(60*60)
