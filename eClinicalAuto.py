import pyautogui as pygui
import tkinter as tk
import time
import pyperclip


def getPosition():
    time.sleep(1)
    print(pygui.position())


def moveMouse():

    # Get Info
    address = pygui.prompt(text="What is the street?", title="", default="")
    zipCode = pygui.prompt(text="What is the zip code?", title="", default="")
    phone = pygui.prompt(text="What is the phone number?", title="", default="")
    insurance = pygui.prompt(text="What is the insurance?", title="", default="")
    subnum = pygui.prompt(text="What is the primary subscriber number?", title="", default="")

    # Enter info screen
    time.sleep(1)
    pygui.moveTo(820, 291, duration=0)
    pygui.click()

    # Move to Address
    pygui.moveTo(813, 333, duration=0)
    pygui.click()
    # Enter address into box
    pygui.write(address.title())
    # Move to Zip
    pygui.moveTo(824, 408, duration=0)
    pygui.click()
    # Enter zip into box
    time.sleep(.5)
    pygui.write(zipCode)
    # Move to Validate
    pygui.moveTo(895, 384, duration=0)
    pygui.click()
    # Move to Fix Address
    time.sleep(3)
    pygui.moveTo(773, 496, duration=0)
    pygui.click()
    # Apply Fix
    time.sleep(.8)
    pygui.moveTo(992, 533, duration=0)
    pygui.click()
    # Close box
    time.sleep(2)
    pygui.moveTo(848, 568, duration=0)
    pygui.click()

    # Phone
    pygui.moveTo(717, 435, duration=0)
    pygui.click()
    # Enter phone into box
    time.sleep(.5)
    pygui.write(phone)
    # Responsible Party
    pygui.moveTo(765, 501, duration=0)
    pygui.click()
    # Confirm Resp Party
    pygui.moveTo(908, 649, duration=0)
    pygui.click()
    # PCP
    pygui.moveTo(1283, 246, duration=0)
    pygui.click()
    # Select PCP
    pygui.moveTo(1265, 269, duration=0)
    pygui.click()

    # Add Ins
    pygui.moveTo(1124, 658, duration=0)
    pygui.click()
    # Search Ins
    time.sleep(.5)
    pygui.write(insurance.upper())
    # Select top result found
    time.sleep(.5)
    pygui.moveTo(1116, 438, duration=0)
    pygui.click()
    pygui.moveTo(1274, 763, duration=0)
    pygui.click()
    # Primary Checkbox
    time.sleep(.5)
    pygui.moveTo(856, 308, duration=0)
    pygui.click()
    # Primary Sub
    pygui.moveTo(693, 472, duration=0)
    pygui.click()
    pygui.write(subnum.upper())
    # Confirm Primary
    pygui.moveTo(1263, 790, duration=0)
    pygui.click()


def eraMouse():
    loopNum = pygui.prompt(text="How many times to loop?", title="", default="")
    for i in range(0, int(loopNum)):
        # Select first ERA
        pygui.moveTo(441, 338, duration=0)
        pygui.click()
        # ePost
        pygui.moveTo(659, 152, duration=0)
        pygui.click()
        time.sleep(3)
        # Close
        pygui.moveTo(1176, 770, duration=0)
        pygui.click()


def lockNotes():
    loopNum = pygui.prompt(text="How many times to loop?", title="", default="")
    for i in range(0, int(loopNum)):
        # Select all
        pygui.moveTo(122, 220, duration=0)
        pygui.click()
        # Lock notes
        pygui.moveTo(600, 1022, duration=0)
        pygui.click()
        time.sleep(2)
        # OK
        pygui.moveTo(1085, 598, duration=0)
        pygui.click()
        # Next Date
        pygui.moveTo(811, 195, duration=0)
        pygui.click()


root = tk.Tk()
frame = tk.Frame(root, height=200, width=600)
frame.grid(row=0, column=0)

button = tk.Button(frame, text="Get Position", command=getPosition)
button.grid(row=0, column=0)

button1 = tk.Button(frame, text="Test Auto", command=moveMouse)
button1.grid(row=0, column=1)

button2 = tk.Button(frame, text="ERA", command=eraMouse)
button2.grid(row=0, column=2)

button3 = tk.Button(frame, text="Lock", command=lockNotes)
button3.grid(row=0, column=3)

root.mainloop()