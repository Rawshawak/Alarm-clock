import time
import datetime

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)
