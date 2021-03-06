#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 31, 2018 01:13:21 PM


import sys
from firebase import firebase
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

def dispatcher_delete():
    print('DispatcherRegistration_support.dispatcher_delete')
    sys.stdout.flush()

def dispatcher_save():
    print('DispatcherRegistration_support.dispatcher_save')
    sys.stdout.flush()

def dispatcher_view():
    print('DispatcherRegistration_support.dispatcher_view')
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
def dautogen_id():
        fire = firebase.FirebaseApplication("https://python-project-2d5d6.firebaseio.com/merchant/employee/Dispatcher",None)
        result = fire.get("dispatcher", None)
        idno = ""
        if result == None:
            idno = "120"
        else:
            for x in result:
                pass
            id = int(x)
            id = id + 1
            idno = str(id)

        return idno


def dispatcher_save():
    idno = dautogen_id()
    name = w.Dispatcher_username.get()
    cno = w.Dispatcher_phone.get()
    password = w.Dispatcher_pass.get()

    if name == "":
        messagebox.showerror("Registration", "Enter Name")
    elif cno == "":
        messagebox.showerror("Registration", "Enter Phone No")
    elif password == "":
        messagebox.showerror("Registration", "Enter Password")
    else:
        fire = firebase.FirebaseApplication("https://python-project-2d5d6.firebaseio.com/merchant/employee/Dispatcher",None)
        fire.put("dispatcher", idno, {"name": name, "phone": cno, "password": password})
        messagebox.showinfo("Registration", "Saved")
        destroy_window()


def dispatcher_view():
    idno = w.View_Id_Entry.get()
    if idno == "":
        messagebox.showerror("View", "Enter Idno")
    else:
        fire = firebase.FirebaseApplication("https://python-project-2d5d6.firebaseio.com/merchant/employee/dispatcher",None)
        result = fire.get("dispatcher", idno)
        if result == None:
            messagebox.showerror("View", "Invalid Idno")
            w.view_stocker_id.delete(0, "end")
        else:
            name = result["name"]
            pno = result["phone"]
            w.Label2_5.configure(text=pno)
            w.Label2_4.configure(text=name)


def dispatcher_delete():
    idno = w.View_Id_Entry.get()
    if idno == "":
        messagebox.showerror("View", "Enter Idno")
    else:
        ans = messagebox.askyesno("Dispatcher Delete", "Are You Sure")
        if ans:
            fire = firebase.FirebaseApplication("https://python-project-2d5d6.firebaseio.com/merchant/employee/dispatcher", None)
            fire.delete("dispatcher", idno)
            messagebox.showinfo("Delete confirmation","Record Deleted")
            destroy_window()

#if __name__ == '__main__':
  #  import DispatcherRegistration
   # DispatcherRegistration.vp_start_gui()


