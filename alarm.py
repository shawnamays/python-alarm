# https://www.101soundboards.com/sounds/59189-dungeon-cleared







from playsound import playsound
import time
import tkinter as tk
from playsound import playsound
import time



# Create the Tkinter window here with this code.  This is where we can add our GUI elements.

window = tk.Tk()
window.title("Study Timer")
# When you run the code with this,
# a little window pops up on the screen, how cool! 
# We still need to further customize it though.



# Now lets create a label to DISPLAY THE TIME REMAINING
time_label = tk.Label(window, text="00:00")
time_label.pack()
# When you run the code with this, 
# the numbers pop up in the window, how cool! 
# There's more to be done though....

# We need to add a BUTTON to our window, so a user can click on it to start their countdown.
start_button = tk.Button(window, text="Start Study Timer")
start_button.pack()

# We need an ENTRY FIELD where the user can input their time
minutes_entry = tk.Entry(window)
minutes_entry.pack()
seconds_entry = tk.Entry(window)
seconds_entry.pack()






########################### The start of the FUNCTIONALITY of my alarm clock ###########

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

# We need to CONNECT THE BUTTON to our countdown function established below.
start_button.config(command=alarm)

# call the alarm function
alarm(total_seconds)

window.mainloop()






##################### !!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!! NOT SURE IF THE FOLLOWING CODE HELPS OR NOT #########################
# import tkinter as tk
# from playsound import playsound
# import time

# # Create the Tkinter window here with this code. This is where we can add our GUI elements.
# window = tk.Tk()
# window.title("Study Timer")

# # Now let's create a label to display the time remaining
# time_label = tk.Label(window, text="00:00")
# time_label.pack()

# # We need to add a button to our window so a user can click on it to start their countdown.
# start_button = tk.Button(window, text="Start Study Timer")
# start_button.pack()

# # We need an entry field where the user can input their time
# minutes_entry = tk.Entry(window)
# minutes_entry.pack()
# seconds_entry = tk.Entry(window)
# seconds_entry.pack()


# def alarm(seconds):
#     time_elapsed = 0

#     while time_elapsed < seconds:
#         time.sleep(1)
#         time_elapsed += 1

#         time_left = seconds - time_elapsed
#         minutes_left = time_left // 60
#         seconds_left = time_left % 60

#         time_label.config(text=f"{minutes_left:02d}:{seconds_left:02d}")

#     playsound("cleared.caf")


# def start_timer():
#     minutes = int(minutes_entry.get())
#     seconds = int(seconds_entry.get())
#     total_seconds = minutes * 60 + seconds
#     alarm(total_seconds)

# # We need to connect the button to our countdown function established below.
# start_button.config(command=start_timer)

# window.mainloop()

