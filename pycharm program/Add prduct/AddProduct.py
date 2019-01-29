#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 04, 2018 10:41:35 PM

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

import AddProduct_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Add_Product (root)
    AddProduct_support.init(root, top)
    root.mainloop()

w = None
def create_Add_Product(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Add_Product (w)
    AddProduct_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Add_Product():
    global w
    w.destroy()
    w = None


class Add_Product:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 14 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("366x450+430+133")
        top.title("Add Product")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=0.99, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#a3f4f1")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=365)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.14, rely=0.03, height=31, width=264)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#a3f4f1")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Add Product''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.01, rely=0.17, height=31, width=114)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#a3f4f1")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''P Number''')

        self.Label2_1 = Label(self.Frame1)
        self.Label2_1.place(relx=0.03, rely=0.32, height=31, width=84)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#a3f4f1")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=font9)
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''P Name''')

        self.Label2_2 = Label(self.Frame1)
        self.Label2_2.place(relx=0.03, rely=0.47, height=31, width=74)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#a3f4f1")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font9)
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''P Price''')

        self.Label2_3 = Label(self.Frame1)
        self.Label2_3.place(relx=0.01, rely=0.64, height=31, width=114)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#a3f4f1")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font=font9)
        self.Label2_3.configure(foreground="#000000")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''P Quantity''')

        self.P_Number = Entry(self.Frame1)
        self.P_Number.place(relx=0.37, rely=0.18,height=30, relwidth=0.5)
        self.P_Number.configure(background="white")
        self.P_Number.configure(disabledforeground="#a3a3a3")
        self.P_Number.configure(font="TkFixedFont")
        self.P_Number.configure(foreground="#000000")
        self.P_Number.configure(highlightbackground="#d9d9d9")
        self.P_Number.configure(highlightcolor="black")
        self.P_Number.configure(insertbackground="black")
        self.P_Number.configure(selectbackground="#c4c4c4")
        self.P_Number.configure(selectforeground="black")

        self.P_Name = Entry(self.Frame1)
        self.P_Name.place(relx=0.38, rely=0.32,height=30, relwidth=0.5)
        self.P_Name.configure(background="white")
        self.P_Name.configure(disabledforeground="#a3a3a3")
        self.P_Name.configure(font="TkFixedFont")
        self.P_Name.configure(foreground="#000000")
        self.P_Name.configure(highlightbackground="#d9d9d9")
        self.P_Name.configure(highlightcolor="black")
        self.P_Name.configure(insertbackground="black")
        self.P_Name.configure(selectbackground="#c4c4c4")
        self.P_Name.configure(selectforeground="black")

        self.P_Price = Entry(self.Frame1)
        self.P_Price.place(relx=0.38, rely=0.48,height=30, relwidth=0.5)
        self.P_Price.configure(background="white")
        self.P_Price.configure(disabledforeground="#a3a3a3")
        self.P_Price.configure(font="TkFixedFont")
        self.P_Price.configure(foreground="#000000")
        self.P_Price.configure(highlightbackground="#d9d9d9")
        self.P_Price.configure(highlightcolor="black")
        self.P_Price.configure(insertbackground="black")
        self.P_Price.configure(selectbackground="#c4c4c4")
        self.P_Price.configure(selectforeground="black")

        self.P_Quantity = Entry(self.Frame1)
        self.P_Quantity.place(relx=0.38, rely=0.64,height=30, relwidth=0.5)
        self.P_Quantity.configure(background="white")
        self.P_Quantity.configure(disabledforeground="#a3a3a3")
        self.P_Quantity.configure(font="TkFixedFont")
        self.P_Quantity.configure(foreground="#000000")
        self.P_Quantity.configure(highlightbackground="#d9d9d9")
        self.P_Quantity.configure(highlightcolor="black")
        self.P_Quantity.configure(insertbackground="black")
        self.P_Quantity.configure(selectbackground="#c4c4c4")
        self.P_Quantity.configure(selectforeground="black")

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.38, rely=0.77, height=34, width=67)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#a3f4f1")
        self.Button1.configure(command=AddProduct_support.Add_product_save)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Save''')

        self.Button1_1 = Button(self.Frame1)
        self.Button1_1.place(relx=0.7, rely=0.77, height=34, width=67)
        self.Button1_1.configure(activebackground="#d9d9d9")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#a3f4f1")
        self.Button1_1.configure(command=AddProduct_support.Add_product_Cancel)
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font=font9)
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Cancel''')






if __name__ == '__main__':
    vp_start_gui()



