from pyautogui import *
from tkinter import *
from time import sleep
from pyperclip import paste
import keyboard
import time

# Create Window
root = Tk()
root.title("eClinicalAuto")

# Create Frame
frame = Frame(root, height=200, width=600)
frame.grid(row=0, column=0)

# Prints the current mouse coordinates to console after user presses q on top of desired location
def getMousePos():
    # Create New Window
    root_mousePos = Toplevel(frame)
    root_mousePos.title("Mouse Position")

    # Label for the mouse position
    label_mousePosition = Label(root_mousePos, text="Mouse Position")
    label_mousePosition.grid(row=0, column=0)

    # Entry field for user to copy desired mouse position
    mousePositionEntry = Entry(root_mousePos)
    mousePositionEntry.grid(row=0, column=1)
    while keyboard.is_pressed("q") == False:
        mousePosition= str(position())# Get the current mouse position
        # Update mouse position entry with new history variable
        mousePositionEntry.delete(0, END)
        mousePositionEntry.insert(0, mousePosition)

# Enters Address, Phone Number, Responsible Party, PCP, and Insurance to Patient Info
def enterPatientInfo():

    # Create New Window
    root_enterPatientInfo = Toplevel(frame)
    root_enterPatientInfo.title("Enter Patient Info")

    # Create Labels
    label_address = Label(root_enterPatientInfo, text="Address")
    label_address.grid(row=0, column=0)
    label_zipcode = Label(root_enterPatientInfo, text="Zipcode")
    label_zipcode.grid(row=1, column=0)
    label_phone = Label(root_enterPatientInfo, text="Phone")
    label_phone.grid(row=2, column=0)
    label_primaryInsuranceName = Label(root_enterPatientInfo, text="Primary Insurance Name")
    label_primaryInsuranceName.grid(row=3, column=0)
    label_primarySubscriberNum = Label(root_enterPatientInfo, text="Primary Insurance Number")
    label_primarySubscriberNum.grid(row=4, column=0)
    label_secondaryInsuranceName = Label(root_enterPatientInfo, text="Secondary Insurance Name")
    label_secondaryInsuranceName.grid(row=5, column=0)
    label_secondarySubscriberNum = Label(root_enterPatientInfo, text="Secondary Insurance Number")
    label_secondarySubscriberNum.grid(row=6, column=0)
    label_ssn = Label(root_enterPatientInfo, text="SSN")
    label_ssn.grid(row=7, column=0)

    # Create Entries
    entry_address = Entry(root_enterPatientInfo)
    entry_address.grid(row=0, column=1)
    entry_zipcode = Entry(root_enterPatientInfo)
    entry_zipcode.grid(row=1, column=1)
    entry_phone = Entry(root_enterPatientInfo)
    entry_phone.grid(row=2, column=1)
    entry_primaryInsuranceName = Entry(root_enterPatientInfo)
    entry_primaryInsuranceName.grid(row=3, column=1)
    entry_primarySubscriberNum = Entry(root_enterPatientInfo)
    entry_primarySubscriberNum.grid(row=4, column=1)
    entry_secondaryInsuranceName = Entry(root_enterPatientInfo)
    entry_secondaryInsuranceName.grid(row=5, column=1)
    entry_secondarySubscriberNum = Entry(root_enterPatientInfo)
    entry_secondarySubscriberNum.grid(row=6, column=1)
    entry_ssn = Entry(root_enterPatientInfo)
    entry_ssn.grid(row=7, column=1)

    # Create Capitalize Name Check Button and Variable
    capsNameState = IntVar()
    check_capitalizeName = Checkbutton(root_enterPatientInfo, text="Caps name?", variable=capsNameState)
    check_capitalizeName.grid(row=8, column=0, columnspan=2)

    # Create Radio Buttons
    label_facilitySelect = Label(root_enterPatientInfo, text="Default Facility")
    label_facilitySelect.grid(row=9, column=0, columnspan=2)
    radio_facilitySelect =  IntVar()
    radio_Aspen = Radiobutton(root_enterPatientInfo, text="Aspen", variable=radio_facilitySelect, value=1)
    radio_Aspen.grid(row=10, column=0)
    radio_Princeton = Radiobutton(root_enterPatientInfo, text="Princeton", variable=radio_facilitySelect, value=2)
    radio_Princeton.grid(row=10, column=1)
    radio_Mcclure = Radiobutton(root_enterPatientInfo, text="Mcclure", variable=radio_facilitySelect, value=3)
    radio_Mcclure.grid(row=11, column=0)
    radio_Moraga = Radiobutton(root_enterPatientInfo, text="Neuro", variable=radio_facilitySelect, value=4)
    radio_Moraga.grid(row=11, column=1)
    radio_Marin = Radiobutton(root_enterPatientInfo, text="Princeton", variable=radio_facilitySelect, value=5)
    radio_Marin.grid(row=12, column=0)
    radio_Legacy = Radiobutton(root_enterPatientInfo, text="Legacy", variable=radio_facilitySelect, value=6)
    radio_Legacy.grid(row=12, column=1)
    radio_Oakland = Radiobutton(root_enterPatientInfo, text="Oakland", variable=radio_facilitySelect, value=7)
    radio_Oakland.grid(row=13, column=0)
    radio_Other = Radiobutton(root_enterPatientInfo, text="Other", variable=radio_facilitySelect, value=8)
    radio_Other.grid(row=13, column=1)

    # Create Variables 
    address = StringVar()
    zipcode = StringVar()
    phone = StringVar()
    primaryInsuranceName = StringVar()
    primarySubscriberNum = StringVar()
    secondaryInsuranceName = StringVar()
    secondarySubscriberNum = StringVar()
    ssn = StringVar()
    facilityName = StringVar()


    # Get information from entries and assign to variables
    def getInfoFromEntries():
        # Address
        if entry_address.get() == "":
            address.set("2512 Telegraph Ave")
        else:
            address.set(entry_address.get())
        # Zipcode
        if entry_zipcode.get() == "":
            zipcode.set("94704")
        else:
            zipcode.set(entry_zipcode.get())
        # Phone
        if entry_phone.get() == "":
            phone.set("")
        else:
            phone.set(entry_phone.get())
        # Primary Insurance
        if entry_primaryInsuranceName.get() == "":
            primaryInsuranceName.set("No Insurance")
        else:
            primaryInsuranceName.set(entry_primaryInsuranceName.get())
        # Primary Insurance Number
        if entry_primarySubscriberNum.get() == "":
            primarySubscriberNum.set("000000")
        else:
            primarySubscriberNum.set(entry_primarySubscriberNum.get())
        # Secondary Insurance Name
        if entry_secondaryInsuranceName.get() == "":
            secondaryInsuranceName.set("NONE")
        else:
            secondaryInsuranceName.set(entry_secondaryInsuranceName.get())
        # Secondary Insurance Number
        if entry_secondarySubscriberNum.get() == "":
            secondarySubscriberNum.set("000000")
        else:
            secondarySubscriberNum.set(entry_secondarySubscriberNum.get())
        # SSN
        if entry_ssn.get() == "":
            ssn.set("")
        else:
            ssn.set(entry_ssn.get())
        # Facility
        if radio_facilitySelect.get() == 1:
            facilityName.set("Aspen")
        elif radio_facilitySelect.get() == 2:
            facilityName.set("Princeton")
        elif radio_facilitySelect.get() == 3:
            facilityName.set("Mcclure")
        elif radio_facilitySelect.get() == 4:
            facilityName.set("Neuro")
        elif radio_facilitySelect.get() == 5:
            facilityName.set("Princeton")
        elif radio_facilitySelect.get() == 6:
            facilityName.set("Legacy")
        elif radio_facilitySelect.get() == 7:
            facilityName.set("Oakland")
        else:
            facilityName.set("SkilledMD")
        
        print(capsNameState.get())

    # Begin to autofill fields
    def beginAutoPatientInfo():
        getInfoFromEntries()
        
        # Click on Info Button
        time.sleep(1) # Delay to let user let go of mouse
        moveTo(820, 291, duration=0)
        click()
        time.sleep(2) # Delay for patient info to load

         # Capitalize name
        if capsNameState.get() == 1:
            # Cut Last Name, Caps it, Then Paste
            moveTo(843, 269)
            dragTo(637, 270, duration=2)
            keyDown("ctrl")
            press("x")
            keyUp("ctrl")
            lastName = str(paste()).upper()
            write(lastName)

            # Cut First Name, Caps it, Then Paste
            moveTo(891, 293)
            dragTo(702, 294, duration=2)
            keyDown("ctrl")
            press("x")
            keyUp("ctrl")
            firstName = str(paste()).upper()
            write(firstName)

        # Enter address info
        moveTo(813, 333, duration=0)
        click()
        write(address.get().title())

        # Enter zip info
        moveTo(824, 408, duration=0)
        click()
        write(zipcode.get())

        # Enter phone info
        moveTo(717, 435, duration=0)
        click()
        write(phone.get())

        # Enter Responsible Party
        moveTo(765, 501, duration=0)
        click()
        # Confirm Responsible Party
        moveTo(908, 649, duration=0)
        click()

        # Enter PCP
        moveTo(1283, 246, duration=0)
        click()
        # Select PCP
        moveTo(1265, 269, duration=0)
        click()

        # Enter SSN info
        moveTo(1082, 415, duration=0)
        click()
        write(ssn.get())

        # Click on Add Insurance Button
        moveTo(1124, 658, duration=0)
        click()
        time.sleep(1) # Delay to let insurance field load
        # Search for primary insurance
        write(primaryInsuranceName.get().upper())
        time.sleep(.5) # Delay to let filtered insurance load
        # Select top result found
        moveTo(1116, 438, duration=0)
        click()
        moveTo(1274, 763, duration=0)
        click()
        time.sleep(.5) # Delay to let filtered insurance load
        # Check Primary Insurance Checkbox
        moveTo(856, 308, duration=0)
        click()
        # Enter Primary Subscriber Number
        moveTo(693, 472, duration=0)
        click()
        write(primarySubscriberNum.get().upper())
        # Save Primary Insurance Info
        moveTo(1263, 790, duration=0)
        click()

        if secondaryInsuranceName.get() != "NONE" and secondarySubscriberNum.get() != "000000":
            # Click on Add Insurance Button
            moveTo(1124, 658, duration=0)
            click()
            time.sleep(1) # Delay to let insurance field load
            # Search for secondary insurance
            write(secondaryInsuranceName.get().upper())
            time.sleep(.5) # Delay to let filtered insurance load
            # Select top result found
            moveTo(1116, 438, duration=0)
            click()
            moveTo(1274, 763, duration=0)
            click()
            time.sleep(.5) # Delay to let filtered insurance load
            # Check Secondary Insurance Checkbox
            moveTo(857, 330, duration=0)
            click()
            # Enter Secondary Subscriber Number
            moveTo(693, 472, duration=0)
            click()
            write(secondarySubscriberNum.get().upper())
            # Save Secondary Insurance Info
            moveTo(1263, 790, duration=0)
            click()

        # Click Additional Info
        moveTo(679, 867, duration=0)
        click()
        sleep(1.5) # Delay to let Additional info load
        # Click Facility Search
        moveTo(1250, 597, duration=0)
        click()
        # Search for Facility
        write(facilityName.get().upper())
        moveTo(824, 420, duration=0)
        # Confirm Facility
        moveTo(1237, 754, duration=0)
        click()
        sleep(.5) # Delay to let facility load
        moveTo(1016, 596, duration=0)
        click()
        # Save Additional Info Changes
        moveTo(1206, 881, duration=0)
        click()
        sleep(1.5) # Delay to let main menu load

        # Validate Address and allow for human review
        moveTo(916, 384, duration=0)
        click()

    # Create Submit Button
    button_submitPatientInfo = Button(root_enterPatientInfo, text="Submit", padx=5, pady=5, command=beginAutoPatientInfo)
    button_submitPatientInfo.grid(row=14, column=0, columnspan=2)
    

# Attempts to post all ERA's until user interrupt
def postERA():
    sleep(1) # Delay to let user let go of mouse
    while keyboard.is_pressed("q") == False:
            # Select first ERA
            moveTo(441, 338, duration=0)
            click()
            # ePost
            moveTo(659, 152, duration=0)
            click()
            sleep(3)
            # Close
            moveTo(1176, 770, duration=0)
            click()

# Attempts to lock all notes until user interrupt
def lockNotes():
    sleep(1) # Delay to let user let go of mouse
    while keyboard.is_pressed("q") == False:
        # Select all
        moveTo(122, 220, duration=0)
        click()
        # Lock notes
        moveTo(600, 1022, duration=0)
        click()
        sleep(5)
        # Next Date
        moveTo(811, 195, duration=0)
        click()

# Button to get the current mouse position for function development, user presses q on top of desired element to get coordinates
button_getMousePos = Button(frame, text="Q for Current Mouse Position", command=getMousePos, height=2, width=35, padx=5, pady=5)
button_getMousePos.grid(row=0, column=0, columnspan=2)

# Button to enter patient information automatically
button_enterPtInfo = Button(frame, text="Enter Patient Info", command=enterPatientInfo, height=2, width=35, padx=5, pady=5)
button_enterPtInfo.grid(row=1, column=0)

# Button to ePost ERA's automatically
button_postERA = Button(frame, text="Post ERAs", command=postERA, height=2, width=35, padx=5, pady=5)
button_postERA.grid(row=2, column=0)

# Button to lock notes automatically
button_lockNotes = Button(frame, text="Lock Notes", command=lockNotes, height=2, width=35, padx=5, pady=5)
button_lockNotes.grid(row=3, column=0)

root.mainloop()