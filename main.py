Sinclaire Hoyt

import Tkinter
Tkinter._test()

import tkinter as tk
r = tk.Tk()
r.title('Entry Box Sample')
e1 = Entry(r)
e1.grid(row=0, column=1)
button = tk.Button(r, text='Enter Name', width=25, command=r.destroy)
button.pack()

r.mainloop()
