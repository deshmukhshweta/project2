#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 13, 2018 11:16:32 AM


import sys
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


def adminLoginValidation():
    username = w.admin_username.get()
    password = w.admin_password.get()
    if(username == ""):
        messagebox.showerror("Admin Login","Please Enter Username")
    else:
        if(password == ""):
            messagebox.showerror("Admin Login","Please Enter password")
        else:
            if((username =="Sathya") and (password == "naveen")):
               messagebox.showinfo("Admin Login","OK")
            else:
                messagebox.showerror("Admin Login","Invalid User")










if __name__ == '__main__':
    import AdminLogin
    #AdminLogin.vp_start_gui()


