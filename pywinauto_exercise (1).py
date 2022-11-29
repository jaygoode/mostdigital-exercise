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
# app.UntitledNotepad.menu_select("File->SaveAs")
# app.SaveAs.ComboBox5.select("UTF-8")
# app.SaveAs.edit1.set_text("Example-utf8.txt")
# app.SaveAs.Save.click()


def open_notepad():
    print("open notepad")
    app = Application(backend="uia").start("notepad.exe").connect(
        title="Untitled - Notepad", timeout=10)


# def close_notepad():
#     print("close notepad")


# def open_about_notepad_view():
#     print("open notepad about view")


# def get_number_of_headings():
#     print("get number of headings")


# def close_all_sub_windows():
#     print("close all sub windows")


# def open_microsoft_licence_link():
#     print("open microsoft license link")


# so it can run this code below
if __name__ == "__main__":
    app = open_notepad()  # basic Notpad application in Windows
    # open_about_notepad_view(app)
    # open_microsoft_licence_link(app)  # from notepad about view
    # # count how many NUMBERED headings there are in Lisense term view
    # # example of numbered heading: "13.	Consumer Rights, Regional Variations."
    # n_headings = get_number_of_headings(app)
    # close_all_sub_windows(app)
    # close_notepad(app)
    # assert n_headings == 15, f"Wrong number of headings: {n_headings}"
