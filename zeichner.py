import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Zugleitsystem")

canvas = tk.Canvas(root, height=300, width=300)

points = [100, 100, 200, 300, 300, 100, 50, 50]
canvas.create_line(points, smooth=True, fill='red', width=2, splinesteps=20)
canvas.create_

canvas.pack()

root.mainloop()