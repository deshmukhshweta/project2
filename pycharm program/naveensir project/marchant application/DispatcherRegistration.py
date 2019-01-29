#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 10, 2018 02:08:35 AM

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

import DispatcherRegistration_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = DispatcherRegistration (root)
    DispatcherRegistration_support.init(root, top)
    root.mainloop()

w = None
def create_DispatcherRegistration(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = DispatcherRegistration (w)
    DispatcherRegistration_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_DispatcherRegistration():
    global w
    w.destroy()
    w = None


class DispatcherRegistration:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Courier New} -size 13 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 20 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("729x398+303+120")
        top.title("DispatcherRegistration")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.01, rely=0.01, relheight=0.99, relwidth=0.99)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="10")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#0cf4ae")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=725)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.03, rely=0.06, height=43, width=302)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#0cf4ae")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Dispatcher Registration''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.04, rely=0.41, height=34, width=62)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#0cf4ae")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Name''')

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.04, rely=0.54, height=34, width=65)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#0cf4ae")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font11)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Phone''')

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.03, rely=0.69, height=34, width=95)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#0cf4ae")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font11)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Password''')

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.04, rely=0.27, height=34, width=48)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#0cf4ae")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font11)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Idno''')

        self.Label6 = Label(self.Frame1)
        self.Label6.place(relx=0.22, rely=0.26, height=34, width=56)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#0cf4ae")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font11)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''..........''')
        idno=DispatcherRegistration_support.dautogen_id()
        self.Label6.configure(text=idno)

        self.Dispatcher_username = Entry(self.Frame1)
        self.Dispatcher_username.place(relx=0.19, rely=0.42, height=22
                , relwidth=0.22)
        self.Dispatcher_username.configure(background="white")
        self.Dispatcher_username.configure(borderwidth="0")
        self.Dispatcher_username.configure(disabledforeground="#a3a3a3")
        self.Dispatcher_username.configure(font=font10)
        self.Dispatcher_username.configure(foreground="#000000")
        self.Dispatcher_username.configure(highlightbackground="#d9d9d9")
        self.Dispatcher_username.configure(highlightcolor="black")
        self.Dispatcher_username.configure(insertbackground="black")
        self.Dispatcher_username.configure(selectbackground="#c4c4c4")
        self.Dispatcher_username.configure(selectforeground="black")

        self.Dispatcher_phone = Entry(self.Frame1)
        self.Dispatcher_phone.place(relx=0.19, rely=0.56, height=22
                , relwidth=0.22)
        self.Dispatcher_phone.configure(background="white")
        self.Dispatcher_phone.configure(borderwidth="0")
        self.Dispatcher_phone.configure(disabledforeground="#a3a3a3")
        self.Dispatcher_phone.configure(font=font10)
        self.Dispatcher_phone.configure(foreground="#000000")
        self.Dispatcher_phone.configure(highlightbackground="#d9d9d9")
        self.Dispatcher_phone.configure(highlightcolor="black")
        self.Dispatcher_phone.configure(insertbackground="black")
        self.Dispatcher_phone.configure(selectbackground="#c4c4c4")
        self.Dispatcher_phone.configure(selectforeground="black")

        self.Dispatcher_password = Entry(self.Frame1)
        self.Dispatcher_password.place(relx=0.2, rely=0.71, height=22
                , relwidth=0.22)
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

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.3, rely=0.81, height=43, width=68)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#0cf4ae")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(command=DispatcherRegistration_support.save_dispatcher)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Save''')

        self.Frame2 = Frame(self.Frame1)
        self.Frame2.place(relx=0.46, rely=0.03, relheight=0.95, relwidth=0.0)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#111111")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=-5)

        self.Label1_3 = Label(self.Frame1)
        self.Label1_3.place(relx=0.52, rely=0.04, height=43, width=282)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#0cf4ae")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(font=font9)
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''View  Dispatcher''')

        self.Lable_111 = Label(self.Frame1)
        self.Lable_111.place(relx=0.49, rely=0.27, height=34, width=48)
        self.Lable_111.configure(activebackground="#f9f9f9")
        self.Lable_111.configure(activeforeground="black")
        self.Lable_111.configure(background="#0cf4ae")
        self.Lable_111.configure(disabledforeground="#a3a3a3")
        self.Lable_111.configure(font=font11)
        self.Lable_111.configure(foreground="#000000")
        self.Lable_111.configure(highlightbackground="#d9d9d9")
        self.Lable_111.configure(highlightcolor="black")
        self.Lable_111.configure(text='''Idno''')

        self.Dispatcher_id = Entry(self.Frame1)
        self.Dispatcher_id.place(relx=0.61, rely=0.29,height=22, relwidth=0.28)
        self.Dispatcher_id.configure(background="white")
        self.Dispatcher_id.configure(borderwidth="0")
        self.Dispatcher_id.configure(disabledforeground="#a3a3a3")
        self.Dispatcher_id.configure(font=font10)
        self.Dispatcher_id.configure(foreground="#000000")
        self.Dispatcher_id.configure(highlightbackground="#d9d9d9")
        self.Dispatcher_id.configure(highlightcolor="black")
        self.Dispatcher_id.configure(insertbackground="black")
        self.Dispatcher_id.configure(selectbackground="#c4c4c4")
        self.Dispatcher_id.configure(selectforeground="black")

        self.Label2_7 = Label(self.Frame1)
        self.Label2_7.place(relx=0.48, rely=0.5, height=34, width=62)
        self.Label2_7.configure(activebackground="#f9f9f9")
        self.Label2_7.configure(activeforeground="black")
        self.Label2_7.configure(background="#0cf4ae")
        self.Label2_7.configure(disabledforeground="#a3a3a3")
        self.Label2_7.configure(font=font11)
        self.Label2_7.configure(foreground="#000000")
        self.Label2_7.configure(highlightbackground="#d9d9d9")
        self.Label2_7.configure(highlightcolor="black")
        self.Label2_7.configure(text='''Name''')

        self.Label3_8 = Label(self.Frame1)
        self.Label3_8.place(relx=0.49, rely=0.65, height=34, width=65)
        self.Label3_8.configure(activebackground="#f9f9f9")
        self.Label3_8.configure(activeforeground="black")
        self.Label3_8.configure(background="#0cf4ae")
        self.Label3_8.configure(disabledforeground="#a3a3a3")
        self.Label3_8.configure(font=font11)
        self.Label3_8.configure(foreground="#000000")
        self.Label3_8.configure(highlightbackground="#d9d9d9")
        self.Label3_8.configure(highlightcolor="black")
        self.Label3_8.configure(text='''Phone''')

        self.Label7 = Label(self.Frame1)
        self.Label7.place(relx=0.66, rely=0.51, height=34, width=136)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#0cf4ae")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font11)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''................''')

        self.Label8 = Label(self.Frame1)
        self.Label8.place(relx=0.6, rely=0.66, height=34, width=216)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#0cf4ae")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font11)
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''..............''')

        self.Button1_9 = Button(self.Frame1)
        self.Button1_9.place(relx=0.69, rely=0.36, height=43, width=68)
        self.Button1_9.configure(activebackground="#d9d9d9")
        self.Button1_9.configure(activeforeground="#000000")
        self.Button1_9.configure(background="#0cf4ae")
        self.Button1_9.configure(borderwidth="0")
        self.Button1_9.configure(command=DispatcherRegistration_support.view_dispatcher)
        self.Button1_9.configure(disabledforeground="#a3a3a3")
        self.Button1_9.configure(font=font11)
        self.Button1_9.configure(foreground="#000000")
        self.Button1_9.configure(highlightbackground="#d9d9d9")
        self.Button1_9.configure(highlightcolor="black")
        self.Button1_9.configure(pady="0")
        self.Button1_9.configure(text='''View''')

        self.Button1_10 = Button(self.Frame1)
        self.Button1_10.place(relx=0.75, rely=0.82, height=43, width=98)
        self.Button1_10.configure(activebackground="#d9d9d9")
        self.Button1_10.configure(activeforeground="#000000")
        self.Button1_10.configure(background="#0cf4ae")
        self.Button1_10.configure(borderwidth="0")
        self.Button1_10.configure(command=DispatcherRegistration_support.delete_dispatcher)
        self.Button1_10.configure(disabledforeground="#a3a3a3")
        self.Button1_10.configure(font=font11)
        self.Button1_10.configure(foreground="#000000")
        self.Button1_10.configure(highlightbackground="#d9d9d9")
        self.Button1_10.configure(highlightcolor="black")
        self.Button1_10.configure(pady="0")
        self.Button1_10.configure(text='''Delete''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)








if __name__ == '__main__':
    vp_start_gui()


