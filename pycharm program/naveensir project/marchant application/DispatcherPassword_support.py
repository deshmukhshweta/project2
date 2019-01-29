#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 18, 2018 08:39:31 PM


import sys
from tkinter import messagebox
from firebase import firebase

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

def Dispatcher_Password():
    from dispatcherlogin_support import idno
    OldP = w.Old_password.get()
    Newp = w.New_password.get()
    Retp = w.retype_password.get()
    if OldP == "":
        messagebox.showerror("password","Please Enter Your Current Password")
    else:
        if Newp =="":
            messagebox.showerror("Password","Please Enter New Password")
        else:
            if Retp =="":
                messagebox.showerror("password","Please Retype Of New Password")
            else:
                fire = firebase.FirebaseApplication("https://merchant-1995r.firebaseio.com/merchant/employee/dispatcher", None)
                result = fire.get("dispatcher",idno)
                paas =result ["password"]
                na = result["name"]
                con = result["phone"]
                if OldP == paas:
                    if Newp == Retp:
                        fire = firebase.FirebaseApplication("https://merchant-1995r.firebaseio.com/merchant/employee/dispatcher",None)
                        fire.put("dispatcher",idno,{"name":na,"password":Retp,"phone":con})
                        messagebox.showinfo("Paasword changed","Password Changed Successfully")
                        destroy_window()
                        import DispatcherHome
                        DispatcherHome.vp_start_gui()
                    else:
                        messagebox.showerror("Password Input","Retype Password Not matching")
                else:
                    messagebox.showerror("Password","Please Enter Your Old Password First")


if __name__ == '__main__':
    import DispatcherPassword
    DispatcherPassword.vp_start_gui()

