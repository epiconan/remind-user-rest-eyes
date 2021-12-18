from win10toast import ToastNotifier #this allows us to make the notifications
from time import sleep #ability to wait a certain amount of time
import win32api #ability to detect mouse movement
import random #ability to pick a random insult

insult_list = [ #this is a list of insults that will be used if the user does not comply
"If you keep this up a newborn child will have better vision than you",
"Exhibit some self-control, you animal!",
"You're going to become blind as a bat",
"You're going to look so ugly with glasses",
"Go touch some grass",
"When was the last time you were outdoors?",
"Oh you've been playing a while why not take a break?",
"Please. Protect your eyes. The damage is irreversible."
]

my_notification = ToastNotifier() #creates an object in the notification class created by the module

while True: #endlessly repeats this part until...
    try: #attempts the following variable assignment
        #converts the string into an integer, and then multiplies by 60 to convert into seconds
        time_interval_cycle = 60 * int(input('How often do you want to be reminded to rest your eyes, in minutes:\n'))
        break #if it reaches here, it breaks out of the while True loop because the above code worked
    except ValueError: #it "catches" the error, if the user types a string or a non-integer, it won't crash the program
        print('Enter an integer!') #it simply reminds the user to enter an integer and the loop continues
while True: #same logic as above
    try:
        time_interval_per_cycle = int(input('How many seconds do you want to rest your eyes each time?\n'))
        break
    except ValueError:
        print('Enter an integer!')

while True:
    sleep(time_interval_cycle) #it waits for 20 minutes (or however long you want)
    my_notification.show_toast('Alert!', 'Please start resting your eyes.')
    # creates a notification that tells the user to start resting eyes
    for a in range(1, time_interval_per_cycle + 1):
        # this is a for loop for however long you want to rest your eyes, ex. 20 seconds
        savedPos = win32api.GetCursorPos() #gets the cursor location
        sleep(1) #waits a second (for the 20 seconds rest)
        if savedPos != win32api.GetCursorPos():
            # checks if the old cursor position is different from the current one
            # if so, it must mean that the user moved the mouse during the 20 second resting timeframe
            my_notification.show_toast('Alert!', (random.choice(insult_list)))
            # makes a notification with a random insult, it also pauses the timer by default
            #(resumes when the notification leaves)
    my_notification.show_toast('Alert!', 'You may return to use the computer')
    # when the for loop above is done, it means that the 20 seconds or whatever is finished
    # this means the user can return to whatever they are doing, and it restarts the loop, waiting for 20 min again
