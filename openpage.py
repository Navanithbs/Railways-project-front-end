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

import openpage_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    openpage_support.init(root, top)
    root.overrideredirect(1)
    root.mainloop()


w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    openpage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
def next():
            import proj
            root.after(10,root.destroy())
            proj.vp_start_gui()

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Noto Serif Tamil} -size 18 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"

        top.geometry("600x450+386+188")
        top.title("New Toplevel")
        top.configure(background="#3d393c")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.2, rely=0.289, relheight=0.456, relwidth=0.575)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#dbdbdb")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.0, rely=0.049, height=151, width=339)
        photo_location = os.path.join(prog_location,"/home/navanith/Downloads/123.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(text='''Label''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.522, rely=0.829, height=31, width=151)
        self.Button1.configure(background="#7a7a7a")
        self.Button1.configure(text='''Click to continue''')
        self.Button1.configure(command=next)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.067, rely=0.067, height=51, width=499)
        self.Label2.configure(background="#e5e5e5")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(font=font9)
        self.Label2.configure(text='''Railway Reservation System''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

if __name__ == '__main__':
    vp_start_gui()





