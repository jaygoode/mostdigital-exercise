# pywinauto_exercise.py

# suggested imports (requires first installing the pywinauto library)
import re  # optional
import pywinauto
from pywinauto.application import Application
import time


# instructions:
# - pip install (--user) -r pywinauto
# - initialize the needed functions below and figure out what kind of
#   substeps those functions will need to perform the task at hand
# - documentation (check out "getting started" section of pywinauto library):
#   - https://pywinauto.readthedocs.io/en/latest/


# implement your code here

# app.UntitledNotepad.type_keys("%FX")
# app.SaveAs.ComboBox5.select("UTF-8")
# app.SaveAs.edit1.set_text("Example-utf8.txt")
# app.SaveAs.Save.click()

# open notepad app. app variable starts and connects to the notepad window named 'Untitled - Notepad'
# def open_notepad():
print("open notepad")
app = Application(backend="uia").start("notepad.exe").connect(
    title="Untitled - Notepad", timeout=10)

# function to open the about window found in Help dropdown menu
# def open_about_notepad_view(app):
print("opening notepad 'about' view")
fileMenu = app.UntitledNotepad.child_window(
    title="Help", control_type="MenuItem").wrapper_object()
fileMenu.click_input()
newWindow = app.UntitledNotepad.child_window(
    title="About Notepad", control_type="MenuItem").wrapper_object()
newWindow.click_input()


# def get_number_of_headings():
#     print("get number of headings")


# def close_all_sub_windows():
#     print("close all sub windows")

# function to open microsoft license link in the about window, licenseLink variable targets the link.
# def open_microsoft_license_link():
print("open microsoft license link")
licenseLink = app.UntitledNotepad.child_window(
    title="Microsoft Software License Terms", control_type="Hyperlink").wrapper_object()
licenseLink.click_input()
app.UntitledNotepad.print_control_identifiers()

# function to close the notepad, close variable targets close button on notepad window


def close_notepad():
    print("closing notepad")
    close = app.UntitledNotepad.child_window(
        title="Close", control_type="Button").wrapper_object()
    close.click_input()

# so it can run this code below
# if __name__ == "__main__":
#     app = open_notepad()  # basic Notpad application in Windows
#     open_about_notepad_view(app)
#     open_microsoft_licence_link(app)  # from notepad about view
#     # count how many NUMBERED headings there are in Lisense term view
#     # example of numbered heading: "13.	Consumer Rights, Regional Variations."
#     n_headings = get_number_of_headings(app)
#     close_all_sub_windows(app)
#     close_notepad(app)
#     assert n_headings == 15, f"Wrong number of headings: {n_headings}"
