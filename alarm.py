# https://www.101soundboards.com/sounds/59189-dungeon-cleared

# from playsound import playsound
# import time

from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("cleared.caf")


minutes = int(input("How many minutes of study: "))
seconds = int(input("How many seconds of study: "))
total_seconds = minutes * 60 + seconds


# call the alarm function with a 10-second countdown
alarm(total_seconds)
