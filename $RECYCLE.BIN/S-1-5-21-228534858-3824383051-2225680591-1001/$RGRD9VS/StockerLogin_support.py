#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 27, 2018 02:27:42 PM


import sys
from tkinter import messagebox
from firebase import firebase as fb

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

import StockerHome
def stockerLoginValidation():
    idno = w.admin_username.get()
    password = w.admin_password.get()
    if(idno == ""):
        messagebox.showerror("Stocker Login","Please Enter Username")
    else:
        if(password == ""):
            messagebox.showerror("Stocker Login","Please Enter Password")
        else:
            fire = fb.FirebaseApplication("https://merchant-application-e1450.firebaseio.com/merchant/employee/stocker",None)
            result = fire.get("stocker", idno)
            if result != None:
                if result["password"] == password:
                    destroy_window()
                    StockerHome.vp_start_gui()
                else:
                    print("Invalid Password")
            else:
                print("Invalid Idno")







