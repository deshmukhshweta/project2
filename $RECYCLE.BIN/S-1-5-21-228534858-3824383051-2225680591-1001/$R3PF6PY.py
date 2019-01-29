#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 26, 2018 06:51:03 PM


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

def dispatcher_autogen_id():
    fire = fb.FirebaseApplication("https://merchant-application-e1450.firebaseio.com/merchant/employee/dispatcher",None)
    result = fire.get("dispatcher",None)
    idno = ""
    if result == None:
        idno = "1001"
    else:
        for x in result:
            pass
        id = int(x)
        id = id + 1
        idno = str(id)

    return idno



def save_dispatcher():
    idno = dispatcher_autogen_id()
    name = w.stocker_name.get()
    cno = w.stocker_phone.get()
    password = w.stocker_password.get()

    if name == "":
        messagebox.showerror("Registration","Enter Name")
    elif cno == "":
        messagebox.showerror("Registration", "Enter Phone No")
    elif password == "":
        messagebox.showerror("Registration", "Enter Password")
    else:
        fire = fb.FirebaseApplication("https://merchant-application-e1450.firebaseio.com/merchant/employee/dispatcher",None)
        fire.put("dispatcher",idno,{"name":name,"phone":cno,"password":password})
        messagebox.showinfo("Registration","Employee Saved")
        destroy_window()


def view_dispatcher():
    idno = w.view_stocker_id.get()
    if idno == "":
        messagebox.showerror("View","Enter Idno")
    else:
        fire = fb.FirebaseApplication("https://merchant-application-e1450.firebaseio.com/merchant/employee/dispatcher",None)
        result = fire.get("dispatcher", idno)
        if result == None:
            messagebox.showerror("View","Invalid Idno")
            w.view_stocker_id.delete(0,"end")
        else:
            name = result["name"]
            pno = result["phone"]
            w.view_stockter_cno.configure(text=pno)
            w.view_stocker_name.configure(text=name)


def delete_dispatcher():
    idno = w.view_stocker_id.get()
    if idno == "":
        messagebox.showerror("View","Enter Idno")
    else:
        ans = messagebox.askyesno("Stocker Delete","Conformation")
        if ans:
            fire = fb.FirebaseApplication("https://merchant-application-e1450.firebaseio.com/merchant/employee/dispatcher",None)
            fire.delete("dispatcher",idno)
            destroy_window()



