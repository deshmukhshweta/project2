#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 31, 2018 01:27:50 PM


import sys
from firebase import firebase
from tkinter import messagebox
import DispatcherHome
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def dispatcher_login():
    print('DispatcherLogin_support.dispatcher_login')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
idno = ""
def dispatcher_login():
    global idno
    idno = w.Dispatcher_username.get()
    password = w.Dispatcher_password.get()
    if (idno == ""):
        messagebox.showerror("Dispatcher Login", "Please Enter Username")
    else:
        if (password == ""):
            messagebox.showerror("Dispatcher Login", "Please Enter Password")
        else:
            fire = firebase.FirebaseApplication("https://python-project-2d5d6.firebaseio.com/merchant/employee/Dispatcher",None)
            result = fire.get("dispatcher", idno)
            if result != None:
                if result["password"] == password:
                    destroy_window()
                    DispatcherHome.vp_start_gui()
                else:
                    messagebox.showerror("Password","Password Not Matching")
            else:
                messagebox.showerror("IdNo","Invalid IDNO")

    return idno
#if __name__ == '__main__':
 #   import DispatcherLogin
  #  DispatcherLogin.vp_start_gui()


