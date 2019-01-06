import math
from tkinter import *

class Fibonacci():
    def s5(self, n, r): # works better for first direction
        spirals = []
        for i in range(n+1):
            spirals.append(((r*(i**0.5),((i*(360)/(((5**0.5)+1)/2))%360))))
        return spirals

    def pol2cart(self, r, theta):
        x = r * math.cos(math.radians(theta))
        y = r * math.sin(math.radians(theta))
        return x,y

    def calculate_coordinates(self, num_points = 100, distance = 3):
        # do the cartesian conversion
        self.coordinates = [self.pol2cart(r, t) for r, t in self.s5(num_points, distance)]

        # center for the canvas
        self.coordinates = [(x+700,y+500) for x, y in self.coordinates]

    def plot_numbers(self, canvas,point,distance1):
        h = 1
        self.calculate_coordinates(num_points = point,distance = distance1)
        for x, y in self.coordinates:
            canvas.create_oval(x+8, y+8, x-8, y-8)
            canvas.create_text(x, y, text = h)
            h += 1

    def plot_lines(self, canvas):
        for delta in [21, 34]:
            for start in range(34):
                x0, y0 = self.coordinates[0]
                i = start
                while i < len(self.coordinates):
                    x1, y1 = self.coordinates[i]
                    canvas.create_line(x0, y0, x1, y1)
                    x0 = x1; y0 = y1
                    i += delta

    def create_gui(self):
        master = Tk()
        master.attributes("-fullscreen", True)
        master.configure(background="purple")
        canvas = Canvas(master, width =1600, height = 900)
        canvas.configure(bg="red")
        canvas.pack()

        self.plot_numbers(canvas,7000,5)
        self.plot_lines(canvas)

        mainloop()

def main():
    f = Fibonacci()
    f.create_gui()
    return 0

if __name__ == '__main__':
    main()
