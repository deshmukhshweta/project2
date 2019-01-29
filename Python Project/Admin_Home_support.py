#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 28, 2018 09:13:36 PM


import sys
import Admin

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
def Admin_Home():
    destroy_window()
    Admin.vp_start_gui()
def Admin_Stocker():
    destroy_window()
    import StockerLogin
    StockerLogin.vp_start_gui()


def Admin_dispatcher():
    destroy_window()
    import DispatcherLogin
    DispatcherLogin.vp_start_gui()

#if __name__ == '__main__':
 #   import Admin_Home
  #  Admin_Home.vp_start_gui()

