#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 27, 2018 03:26:36 PM

import sys

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

import DispatcherHome_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Dispatcher_Home (root)
    DispatcherHome_support.init(root, top)
    root.mainloop()

w = None
def create_Stocker_Home(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Dispatcher_Home (w)
    DispatcherHome_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Stocker_Home():
    global w
    w.destroy()
    w = None


class Dispatcher_Home:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font9 = "-family {Segoe UI} -size 15 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("279x313+268+143")
        top.title("Dispatcher Home")
        top.configure(background="#d9d9d9")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.04, rely=0.03, relheight=0.94, relwidth=0.91)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ffca85")
        self.Frame1.configure(width=255)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.08, rely=0.07, height=44, width=207)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffca85")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(command=DispatcherHome_support.dispatcher_change_password)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Change Password''')
        self.Button1.configure(width=207)

        self.Button1_1 = Button(self.Frame1)
        self.Button1_1.place(relx=0.08, rely=0.31, height=44, width=207)
        self.Button1_1.configure(activebackground="#d9d9d9")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#ffca85")
        self.Button1_1.configure(borderwidth="0")
        self.Button1_1.configure(command=DispatcherHome_support.dispatcher_View_Order)
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font=font9)
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''View Order''')

        self.Button1_2 = Button(self.Frame1)
        self.Button1_2.place(relx=0.08, rely=0.55, height=44, width=207)
        self.Button1_2.configure(activebackground="#d9d9d9")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#ffca85")
        self.Button1_2.configure(borderwidth="0")
        self.Button1_2.configure(command=DispatcherHome_support.dispatcher_Sent_Orders)
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(font=font9)
        self.Button1_2.configure(foreground="#000000")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''Sent Order's''')

        self.Button1_3 = Button(self.Frame1)
        self.Button1_3.place(relx=0.08, rely=0.79, height=44, width=207)
        self.Button1_3.configure(activebackground="#d9d9d9")
        self.Button1_3.configure(activeforeground="#000000")
        self.Button1_3.configure(background="#ffca85")
        self.Button1_3.configure(borderwidth="0")
        self.Button1_3.configure(command=DispatcherHome_support.dispatcher_logout)
        self.Button1_3.configure(disabledforeground="#a3a3a3")
        self.Button1_3.configure(font=font9)
        self.Button1_3.configure(foreground="#000000")
        self.Button1_3.configure(highlightbackground="#d9d9d9")
        self.Button1_3.configure(highlightcolor="black")
        self.Button1_3.configure(pady="0")
        self.Button1_3.configure(text='''Logout''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)






