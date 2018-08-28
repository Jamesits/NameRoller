# Config
namedb_filename = "namedb.csv"

# =============================================================
import tkinter as tk
from tkinter import ttk
import random

# Database logic
people = []

def load_people(filename):
    with open(filename, encoding="utf-8") as f:
        for line in f.readlines():
            # minimum CSV reader
            try:
                name, org = line.strip().strip("\n").split(",", 2)
                people.append({"name": name, "org": org})
            except:
                # ignore all lines with unreadable content
                pass

def random_select():
    return random.choice(people)

def random_select_multiple(count):
    # warning: undefined behavior when count > len(people)
    return random.sample(people, count)

# GUI logic
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.rotating = False

    def create_widgets(self):
        # fake label to expand others
        self.lblFake = tk.Label(self)
        self.lblFake["width"] = 1000
        self.lblFake["height"] = 0
        self.lblFake.pack(side="top", fill="x", expand=True)

        self.lblCurrent = tk.Label(self)
        self.lblCurrent["font"] = ('Microsoft Yahei', 36)
        self.lblCurrent.pack(side="top", fill="both", expand=True)

        self.btnStart = tk.Button(self)
        self.btnStart["text"] = "开始"
        self.btnStart["command"] = self.enable_rotation
        self.btnStart.pack(side="left", fill="x", expand=True)

        self.btnStop = tk.Button(self)
        self.btnStop["text"] = "停止"
        self.btnStop["command"] = self.disable_rotation
        self.btnStop.pack(side="left", fill="x", expand=True)

    def rotate(self):
        chosen_person = random_select()
        self.lblCurrent.configure(text="{1} {0}".format(chosen_person["name"], chosen_person["org"]))
        if self.rotating:
            root.after(50, self.rotate)

    def enable_rotation(self):
        self.rotating = True
        self.rotate()

    def disable_rotation(self):
        self.rotating = False
    

if __name__ == "__main__":
    # initialize random seed
    random.seed()

    # initialize database
    load_people(namedb_filename)

    # start GUI
    root = tk.Tk()
    root.title("点名系统")
    root.style = ttk.Style()
    try:
        root.style.theme_use('winnative')
    except tk.TclError:
        pass
    root.resizable(width=False, height=False)
    root.geometry('720x130')
    app = Application(master=root)
    app.mainloop()