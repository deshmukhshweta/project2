#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 15, 2018 02:21:27 PM

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

import dispatcherlogin_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = DispatcherLogin_ (root)
    dispatcherlogin_support.init(root, top)
    root.mainloop()

w = None
def create_DispatcherLogin_(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = DispatcherLogin_ (w)
    dispatcherlogin_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_DispatcherLogin_():
    global w
    w.destroy()
    w = None


class DispatcherLogin_:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Courier New} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 20 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("411x332+320+117")
        top.title("DispatcherLogin ")
        top.configure(background="#0cf4ae")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.02, relheight=0.98, relwidth=0.99)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="10")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#0cf4ae")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=405)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.11, rely=0.34, height=64, width=112)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#0cf4ae")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Idno''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.14, rely=0.51, height=64, width=115)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#0cf4ae")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Password''')

        self.Dispatcher_name = Entry(self.Frame1)
        self.Dispatcher_name.place(relx=0.48, rely=0.39, height=30, relwidth=0.4)

        self.Dispatcher_name.configure(background="white")
        self.Dispatcher_name.configure(borderwidth="0")
        self.Dispatcher_name.configure(disabledforeground="#a3a3a3")
        self.Dispatcher_name.configure(font=font10)
        self.Dispatcher_name.configure(foreground="#000000")
        self.Dispatcher_name.configure(highlightbackground="#d9d9d9")
        self.Dispatcher_name.configure(highlightcolor="black")
        self.Dispatcher_name.configure(insertbackground="black")
        self.Dispatcher_name.configure(selectbackground="#c4c4c4")
        self.Dispatcher_name.configure(selectforeground="black")

        self.Dispatcher_password = Entry(self.Frame1)
        self.Dispatcher_password.place(relx=0.48, rely=0.56, height=30
                , relwidth=0.4)
        self.Dispatcher_password.configure(background="white")
        self.Dispatcher_password.configure(borderwidth="0")
        self.Dispatcher_password.configure(disabledforeground="#a3a3a3")
        self.Dispatcher_password.configure(font=font10)
        self.Dispatcher_password.configure(foreground="#000000")
        self.Dispatcher_password.configure(highlightbackground="#d9d9d9")
        self.Dispatcher_password.configure(highlightcolor="black")
        self.Dispatcher_password.configure(insertbackground="black")
        self.Dispatcher_password.configure(selectbackground="#c4c4c4")
        self.Dispatcher_password.configure(selectforeground="black")
        self.Dispatcher_password.configure(show="*")

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.62, rely=0.74, height=43, width=76)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#0cf4ae")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(command=dispatcherlogin_support.Dispatcher_login)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.2, rely=0.09, height=43, width=223)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#0cf4ae")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Dispatcher Login''')






if __name__ == '__main__':
    vp_start_gui()


