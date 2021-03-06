#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.2
#  in conjunction with Tcl version 8.6
#    May 18, 2020 10:44:55 PM IST  platform: Windows NT

import sys
import sm_registration
import sm_forgetpass
import sm_dashboard
from tkinter.messagebox import *
import mysql.connector

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

import sm_homepage_support



def login_page():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    sm_homepage_support.init(root, top)
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
    sm_homepage_support.init(w, top, *args, **kwargs)
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
        font12 = "-family {MV Boli} -size 14 -weight bold"
        font13 = "-family {MV Boli} -size 22 -weight bold"
        font15 = "-family {Rockwell} -size 19 -weight bold"
        font16 = "-family {Rockwell} -size 13 -weight bold"
        font17 = "-family {Segoe UI Historic} -size 12 -weight bold"
        font18 = "-family {Segoe UI Light} -size 15 -weight bold"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("661x518+316+109")
        top.minsize(661, 518)
        top.maxsize(661, 518)
        #top.resizable(316, 109)
        top.title("Student Portal")
        top.configure(background="#aeffd7")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.212, rely=0.058, relheight=0.878
                , relwidth=0.598)
        self.Frame1.configure(relief='sunken')
        self.Frame1.configure(borderwidth="5")
        self.Frame1.configure(relief="sunken")
        self.Frame1.configure(background="#3e56ff")

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.028, rely=0.022, height=45, width=238)
        self.TLabel1.configure(background="#3e56ff")
        self.TLabel1.configure(foreground="#ffffff")
        self.TLabel1.configure(font=font13)
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''WELCOME''')

        self.TLabel2 = ttk.Label(self.Frame1)
        self.TLabel2.place(relx=0.028, rely=0.11, height=33, width=266)
        self.TLabel2.configure(background="#3e56ff")
        self.TLabel2.configure(foreground="#ffffff")
        self.TLabel2.configure(font=font12)
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''To Student Portal''')

        self.TLabel3 = ttk.Label(self.Frame1)
        self.TLabel3.place(relx=0.367, rely=0.264, height=32, width=99)
        self.TLabel3.configure(background="#3e56ff")
        self.TLabel3.configure(foreground="#ffffff")
        self.TLabel3.configure(font=font15)
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''LOGIN''')

        self.TLabel4 = ttk.Label(self.Frame1)
        self.TLabel4.place(relx=0.025, rely=0.462, height=22, width=179)
        self.TLabel4.configure(background="#3e56ff")
        self.TLabel4.configure(foreground="#ffffff")
        self.TLabel4.configure(font=font16)
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''Enter User Name''')

        self.Entry1 = ttk.Entry(self.Frame1)
        self.Entry1.place(relx=0.506, rely=0.44, relheight=0.075, relwidth=0.446)

        self.Entry1.configure(font=font17)
        self.Entry1.configure(takefocus="")
        self.Entry1.configure(cursor="ibeam")
        self.tooltip_font = "TkDefaultFont"
        self.Entry1_tooltip = \
        ToolTip(self.Entry1, self.tooltip_font, '''Enter Your User Name''')

        self.TLabel5 = ttk.Label(self.Frame1)
        self.TLabel5.place(relx=0.028, rely=0.549, height=22, width=202)
        self.TLabel5.configure(background="#3e56ff")
        self.TLabel5.configure(foreground="#ffffff")
        self.TLabel5.configure(font=font16)
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(anchor='w')
        self.TLabel5.configure(justify='left')
        self.TLabel5.configure(text='''Enter  Password''')

        self.Entry2 = ttk.Entry(self.Frame1)
        self.Entry2.place(relx=0.506, rely=0.549, relheight=0.075
                , relwidth=0.446)
        self.Entry2.configure(font=font18)
        self.Entry2.configure(takefocus="")
        self.Entry2.configure(cursor="ibeam",show="*")
        self.tooltip_font = "TkDefaultFont"
        self.Entry2_tooltip = \
        ToolTip(self.Entry2, self.tooltip_font, '''Enter Your Password''')

        self.loginbtn = ttk.Button(self.Frame1)
        self.loginbtn.place(relx=0.051, rely=0.681, height=25, width=346)
        self.loginbtn.configure(takefocus="")
        self.loginbtn.configure(text='''LOGIN''',command=self.login)

        self.regbtn = ttk.Button(self.Frame1)
        self.regbtn.place(relx=0.051, rely=0.769, height=25, width=346)
        self.regbtn.configure(takefocus="")
        self.regbtn.configure(text='''NEW USER'S''',command=self.open_registration)

        self.forgetbtn = ttk.Button(self.Frame1)
        self.forgetbtn.place(relx=0.051, rely=0.857, height=25, width=346)
        self.forgetbtn.configure(takefocus="")
        self.forgetbtn.configure(text='''FORGET  PASSWORD''',command=self.open_forgetpass)

    def open_registration(self):
        a = sm_homepage_support.destroy_window()
        a = sm_registration.registration_page()

    def open_forgetpass(self):
        a = sm_homepage_support.destroy_window()
        a = sm_forgetpass.forget_password()

    def connection(self):
        try:
            self.con = mysql.connector.connect(host='localhost',user='root',passwd='',database='student_portal')
            self.cursor = self.con.cursor()
        except Exception as e:
            showerror("Connection Error",e)

    def conection_close(self):
        self.con.close()
        self.cursor.close()

    def login_password(self):

        self.connection()
        password = self.Entry2.get()
        qry2 = ''
        try:
            qry2 = "select password from studentrecord where rollno=%s"
            self.cursor.execute(qry2,(self.Entry1.get(),))
            qry2 = self.cursor.fetchone()[0]
            #print(qry2)
        except Exception as e:
            print("ERROR",e)
        if qry2 == password:
            session = self.Entry1.get()
            a = sm_homepage_support.destroy_window()
            a = sm_dashboard.dashboard_page(session)
        else:
            showwarning("Warning", "please enter valid password !!")

    def login(self):
        self.connection()
        username = self.Entry1.get()

        #print(password)
        qry = ''
        try:
            qry = "select rollno from studentrecord having rollno=%s"%username
            self.cursor.execute(qry)
            qry = self.cursor.fetchone()[0]
        except:
            print("ERROR")

        if qry == username:
            self.conection_close()
            self.login_password()

        else:
            showwarning("Warning","please enter valid user name !!")

# ======================================================
# Support code for Balloon Help (also called tooltips).
# Found the original code at:
# http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
# Modified by Rozen to remove Tkinter import statements and to receive
# the font as an argument.
# ======================================================

from time import time, localtime, strftime

class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=0.5, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          tooltip_font: Font to be used
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in milliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()

    def update(self, msg):
        """
        Updates the Tooltip with a new message. Added by Rozen
        """
        self.msgVar.set(msg)

# ===========================================================
#                   End of Class ToolTip
# ===========================================================

if __name__ == '__main__':
    login_page()





