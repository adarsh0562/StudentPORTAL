#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.2
#  in conjunction with Tcl version 8.6
#    May 19, 2020 11:51:11 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Changepass_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Changepass_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Changepass_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Rockwell} -size 19 -weight bold -underline "  \
            "1"
        font11 = "-family {Rockwell} -size 13 -weight bold"
        font9 = "-family {News701 BT} -size 14 -weight bold"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("674x557+294+103")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#aeffd7")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.03, rely=0.036, relheight=0.878, relwidth=0.325)

        self.Frame1.configure(relief='sunken')
        self.Frame1.configure(borderwidth="5")
        self.Frame1.configure(relief="sunken")
        self.Frame1.configure(background="#3e56ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.027, rely=0.022, height=48, width=182)
        self.TLabel1.configure(background="#3e56ff")
        self.TLabel1.configure(foreground="#ffffff")
        self.TLabel1.configure(font="-family {MV Boli} -size 22 -weight bold")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''WELCOME''')

        self.TLabel2 = ttk.Label(self.Frame1)
        self.TLabel2.place(relx=0.046, rely=0.102, height=25, width=198)
        self.TLabel2.configure(background="#3e56ff")
        self.TLabel2.configure(foreground="#ffffff")
        self.TLabel2.configure(font="-family {MV Boli} -size 14 -weight bold")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''To Student Portal''')

        self.homebtn = ttk.Button(self.Frame1)
        self.homebtn.place(relx=0.027, rely=0.266, height=45, width=206)
        self.homebtn.configure(takefocus="")
        self.homebtn.configure(text='''DASHBOARD''')

        self.vprofilebtn = ttk.Button(self.Frame1)
        self.vprofilebtn.place(relx=0.027, rely=0.368, height=45, width=206)
        self.vprofilebtn.configure(takefocus="")
        self.vprofilebtn.configure(text='''VIEW PROFILE''')

        self.cpassword = ttk.Button(self.Frame1)
        self.cpassword.place(relx=0.027, rely=0.47, height=45, width=206)
        self.cpassword.configure(takefocus="")
        self.cpassword.configure(text='''CHANGE PASSWORD''')

        self.aboutbtn = ttk.Button(self.Frame1)
        self.aboutbtn.place(relx=0.027, rely=0.573, height=45, width=206)
        self.aboutbtn.configure(takefocus="")
        self.aboutbtn.configure(text='''ABOUT US''')

        self.logoutbtn = ttk.Button(self.Frame1)
        self.logoutbtn.place(relx=0.027, rely=0.675, height=45, width=206)
        self.logoutbtn.configure(takefocus="")
        self.logoutbtn.configure(text='''LOG OUT''')

        self.Frame1_1 = tk.Frame(top)
        self.Frame1_1.place(relx=0.401, rely=0.036, relheight=0.878
                , relwidth=0.561)
        self.Frame1_1.configure(relief='sunken')
        self.Frame1_1.configure(borderwidth="5")
        self.Frame1_1.configure(relief="sunken")
        self.Frame1_1.configure(background="#3e56ff")
        self.Frame1_1.configure(highlightbackground="#d9d9d9")
        self.Frame1_1.configure(highlightcolor="black")

        self.TLabel2_3 = ttk.Label(self.Frame1_1)
        self.TLabel2_3.place(relx=0.026, rely=0.041, height=36, width=365)
        self.TLabel2_3.configure(background="#3e56ff")
        self.TLabel2_3.configure(foreground="#ffffff")
        self.TLabel2_3.configure(font=font9)
        self.TLabel2_3.configure(relief="flat")
        self.TLabel2_3.configure(anchor='w')
        self.TLabel2_3.configure(justify='left')
        self.TLabel2_3.configure(text='''Welcome Mr/Mrs- ...............''')

        self.TLabel3_4 = ttk.Label(self.Frame1_1)
        self.TLabel3_4.place(relx=0.159, rely=0.143, height=34, width=275)
        self.TLabel3_4.configure(background="#3e56ff")
        self.TLabel3_4.configure(foreground="#ffffff")
        self.TLabel3_4.configure(font=font10)
        self.TLabel3_4.configure(relief="flat")
        self.TLabel3_4.configure(anchor='w')
        self.TLabel3_4.configure(justify='left')
        self.TLabel3_4.configure(text='''CHANGE PASSWORD''')

        self.TLabel3 = ttk.Label(self.Frame1_1)
        self.TLabel3.place(relx=0.053, rely=0.315, height=19, width=122)
        self.TLabel3.configure(background="#3e56ff")
        self.TLabel3.configure(foreground="#ffffff")
        self.TLabel3.configure(font=font11)
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''Old Password''')

        self.Entry1 = ttk.Entry(self.Frame1_1)
        self.Entry1.place(relx=0.529, rely=0.305, relheight=0.063
                , relwidth=0.413)
        self.Entry1.configure(takefocus="")
        self.Entry1.configure(cursor="ibeam")

        self.TLabel4 = ttk.Label(self.Frame1_1)
        self.TLabel4.place(relx=0.053, rely=0.397, height=19, width=135)
        self.TLabel4.configure(background="#3e56ff")
        self.TLabel4.configure(foreground="#ffffff")
        self.TLabel4.configure(font=font11)
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''New Password''')

        self.Entry2 = ttk.Entry(self.Frame1_1)
        self.Entry2.place(relx=0.529, rely=0.389, relheight=0.063
                , relwidth=0.413)
        self.Entry2.configure(takefocus="")
        self.Entry2.configure(cursor="ibeam")

        self.TLabel5 = ttk.Label(self.Frame1_1)
        self.TLabel5.place(relx=0.053, rely=0.483, height=19, width=165)
        self.TLabel5.configure(background="#3e56ff")
        self.TLabel5.configure(foreground="#ffffff")
        self.TLabel5.configure(font=font11)
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(anchor='w')
        self.TLabel5.configure(justify='left')
        self.TLabel5.configure(text='''Confirm Password''')

        self.Entry3 = ttk.Entry(self.Frame1_1)
        self.Entry3.place(relx=0.529, rely=0.47, relheight=0.063, relwidth=0.413)

        self.Entry3.configure(takefocus="")
        self.Entry3.configure(cursor="ibeam")

        self.savebtn = ttk.Button(self.Frame1_1)
        self.savebtn.place(relx=0.053, rely=0.716, height=35, width=336)
        self.savebtn.configure(takefocus="")
        self.savebtn.configure(text='''UPDATE''')

        self.TLabel6 = ttk.Label(self.Frame1_1)
        self.TLabel6.place(relx=0.053, rely=0.552, height=19, width=288)
        self.TLabel6.configure(background="#3e56ff")
        self.TLabel6.configure(foreground="#80ff00")
        self.TLabel6.configure(font="TkDefaultFont")
        self.TLabel6.configure(relief="flat")
        self.TLabel6.configure(anchor='w')
        self.TLabel6.configure(justify='left')
        self.TLabel6.configure(text='''Note - Password Must be Follow the Follwing creteria''')

        self.TLabel7 = ttk.Label(self.Frame1_1)
        self.TLabel7.place(relx=0.053, rely=0.593, height=19, width=307)
        self.TLabel7.configure(background="#3e56ff")
        self.TLabel7.configure(foreground="#80ff80")
        self.TLabel7.configure(font="TkDefaultFont")
        self.TLabel7.configure(relief="flat")
        self.TLabel7.configure(anchor='w')
        self.TLabel7.configure(justify='left')
        self.TLabel7.configure(text='''1. At Least One Upper case       2. At Least One Lower Case''')

        self.TLabel8 = ttk.Label(self.Frame1_1)
        self.TLabel8.place(relx=0.053, rely=0.634, height=19, width=299)
        self.TLabel8.configure(background="#3e56ff")
        self.TLabel8.configure(foreground="#80ff00")
        self.TLabel8.configure(font="TkDefaultFont")
        self.TLabel8.configure(relief="flat")
        self.TLabel8.configure(anchor='w')
        self.TLabel8.configure(justify='left')
        self.TLabel8.configure(text='''3. At Least One Special Character     4. At Least One Digit''')

if __name__ == '__main__':
    vp_start_gui()





