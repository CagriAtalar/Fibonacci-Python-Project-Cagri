from tkinter import *
from ay_ci import *
from oran_graph import *
from spiral import *
from PIL import ImageTk,Image

def ayc():
    fib_g = Fibonacci()

    fib_g.create_gui()
def spi():
    Spiral()

def oran():
    show_graph()



pencere = Tk()
pencere.title("Fibonacci //Cagri Atalar")
pencere.resizable(width=False, height=False)

arka_res = ImageTk.PhotoImage(Image.open("arkaplan.jpg"))

arka = Label(image=arka_res)

arka.pack()

gen = pencere.winfo_reqwidth()
yuk = pencere.winfo_reqheight()
sagPoz = int(pencere.winfo_screenwidth()/3 - gen/2)
solPoz = int(pencere.winfo_screenheight()/3 - yuk/2)
pencere.geometry("900x450+{}+{}".format(sagPoz, solPoz))

class Uygulama():
    def __init__(self,master):
        self.master = master
        self.create_button()

    def create_button(self):
        ay= Button(self.master,text="Ayçiçeği",bg="black",fg="white",width = 10,height=1,command=ayc)
        ay.configure(font=("Calibri", 12, "bold"))
        ay.place(relx=0.15,rely=0.45)
        alt = Button(self.master,text="Altın Spiral",bg="black",fg="white",width = 10,height=1,command=spi)
        alt.configure(font=("Calibri", 12, "bold"))
        alt.place(relx=0.45,rely=0.45)
        gra = Button(self.master,text="Oran Grafiği",bg="black",fg="white",width = 10,height=1,command=oran)
        gra.configure(font=("Calibri", 12, "bold"))
        gra.place(relx=0.75,rely=0.45)

    def run(self):
        self.master.mainloop()
        
uyg = Uygulama(pencere)
uyg.run()
    
