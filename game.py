import tkinter as tk

def klava(e):
    if e.keysym == "w":
        canvas.move(oval, 0, -10)
    if e.keysym == "s":
        canvas.move(oval, 0, 10)
    if e.keysym == "a":
        canvas.move(oval, -10, 0)
    if e.keysym == "d":
        canvas.move(oval, 10, 0)
    if e.keysym == "Up":
        canvas.move(ovalsec, 0, -10)
    if e.keysym == "Down":
        canvas.move(ovalsec, 0, 10)
    if e.keysym == "Left":
        canvas.move(ovalsec, -10, 0)
    if e.keysym == "Right":
        canvas.move(ovalsec, 10, 0)
win = tk.Tk()
canvas = tk.Canvas(win, bg='#0305B3', height = 400, width=400)
oval=canvas.create_oval((100, 150),(150, 200), fill = "#AAFF13")
ovalsec=canvas.create_oval((300, 150),(350, 200), fill = "#15C7FF")
canvas.pack()
win.bind("<KeyPress>", klava)
tk.mainloop()