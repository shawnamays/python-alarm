# https://www.101soundboards.com/sounds/59189-dungeon-cleared

# from playsound import playsound
# import time

from playsound import playsound
import time

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{minutes_left:02d}:{seconds_left:02d}")

    playsound("cleared.caf")


alarm(10)
