#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 04, 2018 01:59:04 AM


import sys
from firebase import  firebase as fb
from tkinter import messagebox

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
def Dispatcher_login():
    global idno
    idno = w.Dispatcher_name.get()
    password = w.Dispatcher_password.get()
    if(idno == ""):
        messagebox.showerror("Dispatcher Login","Please Enter Username")
    else:

        if(password == ""):

         messagebox.showerror("Dispatcher Login","Please Enter Password")


        else:

            fire = fb.FirebaseApplication("https://merchant-1995r.firebaseio.com/merchant/employee/dispatcher",None)
            result = fire.get("dispatcher",idno)
            if result != None:

                if result["password"] == password:
                    destroy_window()
                    import DispatcherHome
                    DispatcherHome.vp_start_gui()

                else:
                    print("Invalid Password")
            else:
                print("Invalid Idno")

    return idno

if __name__ == '__main__':
    import dispatcherlogin
    dispatcherlogin.vp_start_gui()

