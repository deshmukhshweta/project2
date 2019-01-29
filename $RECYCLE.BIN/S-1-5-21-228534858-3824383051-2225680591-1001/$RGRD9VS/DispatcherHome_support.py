#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 31, 2018 03:06:51 PM


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

def dispatcher_add_product():
    print('DispatcherHome_support.dispatcher_add_product')
    sys.stdout.flush()

def dispatcher_ch_pass():
    print('DispatcherHome_support.dispatcher_ch_pass')
    sys.stdout.flush()

def dispatcher_logout():
    print('DispatcherHome_support.dispatcher_logout')
    sys.stdout.flush()

def dispatcher_view_product():
    print('DispatcherHome_support.dispatcher_view_product')
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

if __name__ == '__main__':
    import DispatcherHome
    DispatcherHome.vp_start_gui()


