#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 03, 2018 12:55:06 AM


import sys
from tkinter import messagebox

from firebase import firebase
from firebase.firebase import FirebaseApplication
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

def Add_product_save():
    print('AddProduct_support.Add_product_save')
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

def Add_product_Cancel():
    destroy_window()
    import Stocker_Home
    Stocker_Home.vp_start_gui()

def Add_product_save():
    PNo = w.P_Number.get()
    Pname = w.P_Name.get()
    PPri = w.P_Price.get()
    Pqun = w.P_Quantity.get()
    if PNo == "":
        messagebox.showerror("Product Number","Please Enter Product Number")
    elif Pname == "":
        messagebox.showerror("Product Name ","Please Enter Product Name")
    elif PPri == "":
        messagebox.showerror("Product Price","Please Enter Product Price")
    elif Pqun == "":
        messagebox.showerror("Product Quantity","Please Enter Product Quantity")
    else:
        if (check_pno(PNo)):
            try:
                PChane = float(PPri)
                pqty = int(Pqun)
                fire = firebase.FirebaseApplication("https://python-project-2d5d6.firebaseio.com/merchant/Product", None)
                fire.put("Product", PNo, {"ProductName": Pname, "ProductPrice": PChane, "ProductQuantity": pqty})
                messagebox.showinfo("Add Product", "Product Saved")
                #destroy_window()
            except ValueError:
                messagebox.showerror("Add Product", "Please Enter A Valid Input")

def check_pno(PNo):
    fire = firebase.FirebaseApplication("https://python-project-2d5d6.firebaseio.com/merchant/Product", None)
    result = fire.get("Product", None)
    if result != None:
         for key in result.keys():
             if key == PNo:
                 messagebox.showerror("Add Product", "Product No Is Available")
                 return False
                 break
         else:
            return True

#if __name__ == '__main__':
 #   import AddProduct
  #  AddProduct.vp_start_gui()


