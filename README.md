# eClinicalAuto
Program to automate mouseclicks and keyboard inputs on desktop eClinicalWords V11.

## Purpose
Developed for SkilledMD to increase company workflow by eliminating human mouse input

## Tools Used
Tkinter
PyAutoGUI
PyperClip

## Features
Q for Current Mouse Position
- Used for debug and future development
- Displays current x and y coordinates of the mouse when "Q" is pressed

Enter Patient Info
- Opens a form to fill out with patient information
- Once submit button is pressed, computer automatically fills in supplied information on eClinicalWorks

Post ERA's
- Clicks on ERA and ePosts indefinately until "Q" is held down to interrupt the loop

Lock Notes
- Selects all notes on date of service
- Clicks Lock Notes and waits for an arbitrary amount of time until moving to next date of service
- Loops indefinately until "Q" is held down to interrupt the loop
