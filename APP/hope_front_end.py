from functools import partial
from tkinter import *
from tkinter.ttk import Style, Frame, Button
import pyttsx3
import sys

it1 = 0
it2 = 0
it3 = 0
it4 = 0

l1 = False
l2 = False
l3 = False
l4 = False

runningLevel_1 = False
runningLevel_2 = False
runningLevel_3 = False
runningLevel_4 = False

level1Buttons = {}
level2Buttons = {}
level3Buttons = {}
level4Buttons = {}


def level1buttons(val):
    print(val)
    engine.say(val)
    engine.runAndWait()

def level1add(val):
    print("Adding....", val)
    engine.say("Adding....", val)
    engine.runAndWait()

def level2back():
    print("Doing level 2 back")
    engine.say("Doing level 2 back")
    engine.runAndWait()

def level2undo():
    print("Undoing Level 2")
    engine.say("Undoing level 2")
    engine.runAndWait()

def level2speak():
    print("Speaking at level 2")
    engine.say("Speaking at level 2")
    engine.runAndWait()

def level2buttons():
    print("Level 2 Button clicked")
    engine.say("Level 2 Button clicked")
    engine.runAndWait()

def level2erase():
    print("Erase after final speak")
    engine.say("Erase after final speak")
    engine.runAndWait()

def level3buttons():
    print("Level 3 Button clicked")
    engine.say("Level 3 Button clicked")
    engine.runAndWait()

def level3more():
    print("Level 3 More")
    engine.say("Level 3 More")
    engine.runAndWait()

def level3back():
    print("Level 3 Back")
    engine.say("Level 3 Back")
    engine.runAndWait()

def level4text():
    print("Level 4 Text")
    engine.say("Level 4 Text")
    engine.runAndWait()

def level4speak():
    print("Level 4 Speak")
    engine.say("Level 4 Speak")
    engine.runAndWait()

def level4back():
    print("Level 4 Back")
    engine.say("Level 4 Back")
    engine.runAndWait()

# -------------------------------------------------------------------------------------------#

def action(event):
    print("Action Successful")

    global runningLevel_1, runningLevel_2, runningLevel_3, runningLevel_4, Main_Window
    global level1Buttons, level2Buttons, level3Buttons, level4Buttons
    global it1, it2, it3, it4, l1, l2, l3, l4

    if l1:

        # Level 1 action
        print("Inside L1")
        runningLevel_1 = False
        l1 = False
        if it1 == 0:
            sys.exit()
        else:
            val = level1Buttons[(it1-1)%11]

        if it1 == 0:
            Main_Window._buttons1[level1Buttons[10]].config(style="b1.TButton")
        else:
            Main_Window._buttons1[level1Buttons[(it1 - 1) % 11]].config(style="b1.TButton")

        it1 = 0

        level2Buttons[1] = val[0]
        level2Buttons[2] = val[1]
        level2Buttons[3] = val[2]

        Main_Window._buttons2["1"].config(text = val[0])
        Main_Window._buttons2["2"].config(text=val[1])
        Main_Window._buttons2["3"].config(text=val[2])

        runningLevel_2 = True
        l2 = True
        it2 = 0

        root.after(1000, scanningLevel_2)

    elif l2:

        # Level 2 action
        pass

    elif l3:

        # Level 3 action
        pass

    elif l4:

        # Level 4 action
        pass


# -------------------------------------------------------------------------------------------#

def startScanning():

    global runningLevel_1
    runningLevel_1 = True

# -------------------------------------------------------------------------------------------#

def stopScanning():

    global runningLevel_1, runningLevel_2, runningLevel_3, runningLevel_4, Main_Window
    global level1Buttons, level2Buttons, level3Buttons, level4Buttons
    global it1, it2, it3, it4, l1, l2, l3, l4

    runningLevel_1 = False
    runningLevel_2 = False
    runningLevel_3 = False
    runningLevel_4 = False

    l1 = False
    l2 = False
    l3 = False
    l4 = False

    if it1 == 0:
        Main_Window._buttons1[level1Buttons[10]].config(style="b1.TButton")
    else:
        Main_Window._buttons1[level1Buttons[(it1-1)%11]].config(style="b1.TButton")

    if it2 == 0:
        Main_Window._buttons3[level2Buttons[6]].config(style="b1.TButton")
    elif it2<=4:
        if it2-1==0:
            Main_Window._buttons2[level2Buttons[0]].config(style="b1.TButton")
        else:
            Main_Window._buttons2[str((it2-1)%7)].config(style="b1.TButton")
    elif it2>4:
        Main_Window._buttons3[level2Buttons[(it2-1)%7]].config(style="b1.TButton")

    Main_Window._buttons2["1"].config(text="")
    Main_Window._buttons2["2"].config(text="")
    Main_Window._buttons2["3"].config(text="")
    #print(it1)

    it1 = 0
    it2 = 0
    it3 = 0
    it4 = 0

    pass

# -------------------------------------------------------------------------------------------#

def changeVoice():

    # Voice changing function
    pass

# -------------------------------------------------------------------------------------------#

# SCANNING LEVEL 1 FUNCTION

def scanningLevel_1():

    global runningLevel_1, Main_Window, it1, l1

    if runningLevel_1:

        # Scans over level 1 buttons
        #print(level1Buttons[0])
        l1 = True

        if it1 == 0:
            Main_Window._buttons1[level1Buttons[10]].config(style="b1.TButton")
            Main_Window._buttons1[level1Buttons[0]].config(style = "b11.TButton")

        else:
            Main_Window._buttons1[level1Buttons[(it1-1)%11]].config(style="b1.TButton")
            Main_Window._buttons1[level1Buttons[it1]].config(style="b11.TButton")

        it1 = (it1+1)%11

        #print("Hello Scanning Level 1")

    root.after(2000, scanningLevel_1)

# -------------------------------------------------------------------------------------------#

# SCANNING LEVEL 2 FUNCTION

def scanningLevel_2():

    global runningLevel_2, Main_Window, it2, l2

    if runningLevel_2:

        l2 = True
        # Scans over level 2 buttons
        if it2 == 0:
            Main_Window._buttons3[level2Buttons[6]].config(style="b1.TButton")
            Main_Window._buttons2[level2Buttons[0]].config(style = "b11.TButton")
        elif it2 < 4:
            if (it2-1)%7 == 0:
                Main_Window._buttons2[level2Buttons[0]].config(style="b1.TButton")
                Main_Window._buttons2[str(it2)].config(style="b11.TButton")
            else:
                Main_Window._buttons2[str((it2 - 1) % 7)].config(style="b1.TButton")
                Main_Window._buttons2[str(it2)].config(style="b11.TButton")
        elif it2 == 4:
            Main_Window._buttons2["3"].config(style="b1.TButton")
            Main_Window._buttons3[level2Buttons[4]].config(style="b11.TButton")
        elif it2 > 4:
            Main_Window._buttons3[level2Buttons[(it2-1)%7]].config(style="b1.TButton")
            Main_Window._buttons3[level2Buttons[it2]].config(style="b11.TButton")

        it2 = (it2 + 1)%7

    root.after(2000, scanningLevel_2)

# -------------------------------------------------------------------------------------------#

# SCANNING LEVEL 3 FUNCTION

def scanningLevel_3():

    global runningLevel_3, Main_Window, it3, l3

    if runningLevel_3:

        # Scans over level 2 buttons
        pass


# -------------------------------------------------------------------------------------------#

# SCANNING LEVEL 4 FUNCTION

def scanningLevel_4():

    global runningLevel_4, Main_Window, it4, l4

    if runningLevel_4:

        # Scans over level 2 buttons
        pass


# -------------------------------------------------------------------------------------------#


# Class declaration to Initialize all necessary buttons

class InitializeWindow:

    def __init__(self, master):


        self._master = master
        self._level1 = ["ADD", "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ#", "QUIT"]

        self._buttons0 = {}
        self._buttons1 = {}
        self._buttons2 = {}
        self._buttons3 = {}
        self._buttons4 = {}
        self._buttons5 = {}

        self._frame0 = Frame(master, padding = (11,10,0,0))
        self._frame1 = Frame(master, padding = (0,10,0,0))
        self._topframe234 = Frame(master, padding = (32, 16, 32, 0))
        self._frame2 = Frame(self._topframe234)
        self._frame3 = Frame(self._topframe234)
        self._frame4 = Frame(self._topframe234, width = 200)
        self._frame5 = Frame(master, relief = "ridge", width = 100, height = 50)

        self.initUI()

    # -------------------------------------------------------------------------------------------#

    def initUI(self):

        # Packing Frames in Root window
        global level1Buttons, level2Buttons, level3Buttons, level4Buttons

        self._master.title("HOPE")
        self._master.bind('<Button-1>', action)

        self._frame0.pack(anchor = NW)
        self._frame1.pack(anchor = N)
        self._topframe234.pack(anchor = W, fill = X)
        self._frame2.pack(side = LEFT)
        self._frame3.pack(side = RIGHT)
        self._frame4.pack(anchor = CENTER, pady = 5)
        self._frame5.pack(anchor = CENTER)

        # Style configuration for Buttons

        s1 = Style()
        s1.configure("b1.TButton", font=("Helvetica", 14, "bold"), foreground="black",
                     background="lightblue", padding=4)

        s2 = Style()
        s2.configure("b2.TButton", font=("Helvetica", 14, "bold"), foreground="black",
                     background="white", padding=4, borderwidth=0)

        s3 = Style()
        s3.configure("b3.TButton", font=("Helvetica", 14, "bold"), foreground="black",
                     background="lightyellow", padding=4)


        # Level 0 Button Initialization


        self._buttons0["StartScan"] = (Button(self._frame0, text="Start Scan", style="b3.TButton"))
        self._buttons0["StartScan"].configure(command=startScanning)
        self._buttons0["StartScan"].pack(side = LEFT, padx = 2)

        self._buttons0["StopScan"] = (Button(self._frame0, text="Stop Scan", style="b3.TButton"))
        self._buttons0["StopScan"].configure(command=stopScanning)
        self._buttons0["StopScan"].pack(side = LEFT, padx=2)

        self._buttons0["VoiceChange"] = (Button(self._frame0, text="Change Voice", style="b3.TButton"))
        self._buttons0["VoiceChange"].configure(command=changeVoice)
        self._buttons0["VoiceChange"].pack(side = LEFT, padx=2)


        # Level 1 Button Initialization

        for i, val in enumerate(self._level1):

            self._buttons1[val] = (Button(self._frame1, text = val, style = "b1.TButton"))
            level1Buttons[i] = val

            if val=="ADD":
                self._buttons1[val].configure(command = partial(level1add, val))
            elif val=="QUIT":
                self._buttons1[val].configure(command = quit)
            else:
                self._buttons1[val].configure(command=partial(level1buttons, val))

            self._buttons1[val].pack(side = LEFT, padx = 2)



        # Level 2 Button Initialization

        self._buttons2["Back"] = (Button(self._frame2, text = "Back", style = "b1.TButton"))
        self._buttons2["Back"].configure(command = level2back)
        self._buttons2["Back"].pack(pady = 2)
        level2Buttons[0] = "Back"

        self._buttons2["1"] = (Button(self._frame2, style="b1.TButton"))
        self._buttons2["1"].configure(command=partial(level2buttons))
        self._buttons2["1"].pack(pady = 2)
        level2Buttons[1] = ""

        self._buttons2["2"] = (Button(self._frame2, style="b1.TButton"))
        self._buttons2["2"].configure(command=level2buttons)
        self._buttons2["2"].pack(pady = 2)
        level2Buttons[2] = ""

        self._buttons2["3"] = (Button(self._frame2, style="b1.TButton"))
        self._buttons2["3"].configure(command=level2buttons)
        self._buttons2["3"].pack(pady = 2)
        level2Buttons[3] = ""

        self._buttons3["Undo"] = (Button(self._frame3, text = "Undo", style="b1.TButton"))
        self._buttons3["Undo"].configure(command=level2undo)
        self._buttons3["Undo"].pack(pady = 2)
        level2Buttons[4] = "Undo"

        self._buttons3["Speak"] = (Button(self._frame3, text = "Speak", style="b1.TButton"))
        self._buttons3["Speak"].configure(command=level2speak)
        self._buttons3["Speak"].pack(pady = 2)
        level2Buttons[5] = "Speak"

        self._buttons3["Erase"] = (Button(self._frame3, text = "Erase", style="b1.TButton"))
        self._buttons3["Erase"].configure(command=level2erase)
        self._buttons3["Erase"].pack(pady = 2)
        level2Buttons[6] = "Erase"


        # Level 3 Button Initialization

        self._buttons4["Main"] = (Button(self._frame4, style="b2.TButton", width = 80))
        self._buttons4["Main"].configure(command=level3buttons)
        self._buttons4["Main"].pack(pady = 2)
        level3Buttons[0] = "Main"

        self._buttons4["1"] = (Button(self._frame4, style="b2.TButton", width = 80))
        self._buttons4["1"].configure(command=level3buttons)
        self._buttons4["1"].pack(pady = 2)
        level3Buttons[1] = ""

        self._buttons4["2"] = (Button(self._frame4, style="b2.TButton", width = 80))
        self._buttons4["2"].configure(command=level3buttons)
        self._buttons4["2"].pack(pady = 2)
        level3Buttons[2] = ""

        self._buttons4["3"] = (Button(self._frame4, style="b2.TButton", width = 80))
        self._buttons4["3"].configure(command=level3buttons)
        self._buttons4["3"].pack(pady = 2)
        level3Buttons[3] = ""

        self._buttons4["4"] = (Button(self._frame4, style="b2.TButton", width = 80))
        self._buttons4["4"].configure(command=level3buttons)
        self._buttons4["4"].pack(pady = 2)
        level3Buttons[4] = ""

        self._buttons4["More"] = (Button(self._frame4, text = "More", style="b2.TButton", width=40))
        self._buttons4["More"].configure(command=level3more)
        self._buttons4["More"].pack(side = LEFT, pady = 6, padx = 2)
        level3Buttons[5] = "More"

        self._buttons4["Back"] = (Button(self._frame4, text = "Back", style="b2.TButton", width=40))
        self._buttons4["Back"].configure(command=level3back)
        self._buttons4["Back"].pack(side = LEFT, pady = 6, padx = 2)
        level3Buttons[6] = "Back"


        # Level 4 Button Initialization

        self._buttons5["Text"] = (Button(self._frame5, width = 60, style = "b3.TButton"))
        self._buttons5["Text"].configure(command = level4text)
        self._buttons5["Text"].pack(side = LEFT)
        level4Buttons[0] = "Text"

        self._buttons5["Speak"] = (Button(self._frame5, text = "Speak", width=10, style="b3.TButton"))
        self._buttons5["Speak"].configure(command=level4speak)
        self._buttons5["Speak"].pack(side=LEFT)
        level4Buttons[1] = "Speak"

        self._buttons5["Back"] = (Button(self._frame5, text = "Back", width=10, style="b3.TButton"))
        self._buttons5["Back"].configure(command=level4back)
        self._buttons5["Back"].pack(side=LEFT)
        level4Buttons[2] = "Back"

        return self


# -------------------------------------------------------------------------------------------#


if __name__ == "__main__":

    root = Tk()
    root.geometry("1200x500+100+100")
    engine = pyttsx3.init()

    # -------------------------------------------------------------------------------------------#

    s1 = Style()
    s1.configure("b1.TButton", font=("Helvetica", 14, "bold"), foreground="black",
                 background="lightblue", padding=4)
    s11 = Style()
    s11.configure("b11.TButton", font=("Helvetica", 15, "bold"), foreground="white",
                  background="darkblue", padding=4)

    s2 = Style()
    s2.configure("b2.TButton", font=("Helvetica", 14, "bold"), foreground="black",
                 background="white", padding=4, borderwidth=0)

    s3 = Style()
    s3.configure("b3.TButton", font=("Helvetica", 14, "bold"), foreground="black",
                 background="lightyellow", padding=4)

    # -------------------------------------------------------------------------------------------#

    Main_Window = InitializeWindow(root)
    root.after(2000, scanningLevel_1)
    root.mainloop()
