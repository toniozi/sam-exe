from tkinter import *
import os

root=Tk()
root.title("SAM")

can = Canvas(root)
can.pack()

###############

def sam():
    cmd = "sam" +" -speed " + speed_entry.get() + " -pitch " + pitch_entry.get() + " -throat " + throat_entry.get() + " -mouth " + mouth_entry.get() + " " + speech_entry.get()
    print(cmd)
    os.system(cmd)

for loop in range(1):
    can.grid_columnconfigure(loop, weight=1)
for moop in range(6):
    can.grid_rowconfigure(moop, weight=1)

speech_label=Label(can, text="Enter what SAM will say")
speech_label.grid(row=0, column=0)

speech_entry = Entry(can)
speech_entry.grid(row=0, column=1)
speech = speech_entry.get()

speed_label = Label(can, text="Speed")
speed_label.grid(row=1, column=0)

speed_entry = Entry(can)
speed_entry.grid(row=1, column=1)
speed_entry.insert(0, "72")


pitch_label = Label(can, text="Pitch")
pitch_label.grid(row=2, column=0)

pitch_entry = Entry(can)
pitch_entry.grid(row=2, column=1)
pitch_entry.insert(0, "64")


throat_label = Label(can, text="Throat")
throat_label.grid(row=3, column=0)

throat_entry = Entry(can)
throat_entry.grid(row=3, column=1)
throat_entry.insert(0, "128")


mouth_label = Label(can, text="Mouth")
mouth_label.grid(row=4, column=0)

mouth_entry = Entry(can)
mouth_entry.grid(row=4, column=1)
mouth_entry.insert(0, "128")


confirm = Button(can, text="Confirm text", command=sam)
confirm.grid(row=5, column=0)

Button(root, text="Quitter", command = root.quit).pack()


root.mainloop()
root.destroy()
