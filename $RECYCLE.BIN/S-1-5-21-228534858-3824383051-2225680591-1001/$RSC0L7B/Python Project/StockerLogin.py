#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 20, 2018 02:44:51 AM

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

import StockerLogin_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Stocker_Login (root)
    StockerLogin_support.init(root, top)
    root.mainloop()

w = None
def create_Stocker_Login(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Stocker_Login (w)
    StockerLogin_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Stocker_Login():
    global w
    w.destroy()
    w = None


class Stocker_Login:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {Courier New} -size 13 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 21 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 16 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("487x337+384+154")
        top.title("Admin Login")
        top.configure(background="#79d8c8")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.93, relwidth=0.95)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="14")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d820d8")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=465)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.28, rely=0.06, height=41, width=214)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d820d8")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Stocker Login''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.04, rely=0.3, height=31, width=114)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d820d8")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''IDNO''')

        self.Admin_paas = Label(self.Frame1)
        self.Admin_paas.place(relx=0.04, rely=0.43, height=31, width=114)
        self.Admin_paas.configure(activebackground="#f9f9f9")
        self.Admin_paas.configure(activeforeground="black")
        self.Admin_paas.configure(background="#d820d8")
        self.Admin_paas.configure(disabledforeground="#a3a3a3")
        self.Admin_paas.configure(font=font9)
        self.Admin_paas.configure(foreground="#000000")
        self.Admin_paas.configure(highlightbackground="#d9d9d9")
        self.Admin_paas.configure(highlightcolor="black")
        self.Admin_paas.configure(text='''Phone''')

        self.Admin_username = Entry(self.Frame1)
        self.Admin_username.place(relx=0.3, rely=0.3,height=30, relwidth=0.4)
        self.Admin_username.configure(background="white")
        self.Admin_username.configure(disabledforeground="#a3a3a3")
        self.Admin_username.configure(font=font10)
        self.Admin_username.configure(foreground="#000000")
        self.Admin_username.configure(highlightbackground="#d9d9d9")
        self.Admin_username.configure(highlightcolor="black")
        self.Admin_username.configure(insertbackground="black")
        self.Admin_username.configure(selectbackground="#c4c4c4")
        self.Admin_username.configure(selectforeground="black")

        self.Admin_password = Entry(self.Frame1)
        self.Admin_password.place(relx=0.3, rely=0.44,height=30, relwidth=0.4)
        self.Admin_password.configure(background="white")
        self.Admin_password.configure(disabledforeground="#a3a3a3")
        self.Admin_password.configure(font=font10)
        self.Admin_password.configure(foreground="#000000")
        self.Admin_password.configure(highlightbackground="#d9d9d9")
        self.Admin_password.configure(highlightcolor="black")
        self.Admin_password.configure(insertbackground="black")
        self.Admin_password.configure(selectbackground="#c4c4c4")
        self.Admin_password.configure(selectforeground="black")
        self.Admin_password.configure(show="*")

        self.Admin_Button = Button(self.Frame1)
        self.Admin_Button.place(relx=0.28, rely=0.6, height=34, width=87)
        self.Admin_Button.configure(activebackground="#d9d9d9")
        self.Admin_Button.configure(activeforeground="#000000")
        self.Admin_Button.configure(background="#d820d8")
        self.Admin_Button.configure(borderwidth="0")
        self.Admin_Button.configure(command=StockerLogin_support.Stocker_validation)
        self.Admin_Button.configure(disabledforeground="#a3a3a3")
        self.Admin_Button.configure(font=font9)
        self.Admin_Button.configure(foreground="#000000")
        self.Admin_Button.configure(highlightbackground="#d9d9d9")
        self.Admin_Button.configure(highlightcolor="black")
        self.Admin_Button.configure(pady="0")
        self.Admin_Button.configure(text='''Login''')

        self.Admin_Button_1 = Button(self.Frame1)
        self.Admin_Button_1.place(relx=0.53, rely=0.61, height=34, width=87)
        self.Admin_Button_1.configure(activebackground="#d9d9d9")
        self.Admin_Button_1.configure(activeforeground="#000000")
        self.Admin_Button_1.configure(background="#d820d8")
        self.Admin_Button_1.configure(borderwidth="0")
        self.Admin_Button_1.configure(command=StockerLogin_support.Stocker_Cancel)
        self.Admin_Button_1.configure(disabledforeground="#a3a3a3")
        self.Admin_Button_1.configure(font=font9)
        self.Admin_Button_1.configure(foreground="#000000")
        self.Admin_Button_1.configure(highlightbackground="#d9d9d9")
        self.Admin_Button_1.configure(highlightcolor="black")
        self.Admin_Button_1.configure(pady="0")
        self.Admin_Button_1.configure(text='''Cancel''')






if __name__ == '__main__':
    vp_start_gui()



