import tkinter
from tkinter import font, messagebox
from tkinter import *
def hola():
    messagebox.showinfo(message="HOLA MUNDO", title="🎉🎉🎉🎉🎉")
def Calcular():
  global precioVh
  precioVh = texbox1.get
  print(precioVh)
root = Tk()
root.geometry("960x620")
root.title("Consecionario")
root.configure(background='#FFC7FA')
root.resizable(True, False)
texbox1 = Entry(root, text=" ", bg='white',fg='black', width=13, font=("BubbleGum", 30 ))
texbox1.place(x=610, y= 60)
label1 = Label(root, text="precio del vehiculo", bg='#FFC7FA',fg='black', width=0, font=("BubbleGum", 30))
label1.place(x= 600, y= 10)
label2 = Label(root, text="Tipo de vehiculo", bg='#FFC7FA',fg='black', width=0, font=("BubbleGum", 30))
label2.place(x= 600, y= 120)
Tipo = IntVar()
rbutton1 = Radiobutton(root, text="Familiar", bg='#FFC7FA',fg='black', width=0, font=("BubbleGum", 30), variable= Tipo, value=0)
rbutton1.place(x= 600, y= 180)

rbutton1 = Radiobutton(root, text="4x4", bg='#FFC7FA',fg='black', width=0, font=("BubbleGum", 30), variable= Tipo, value=1)
rbutton1.place(x= 600, y= 230)

rbutton1 = Radiobutton(root, text="Carga", bg='#FFC7FA',fg='black', width=0, font=("BubbleGum", 30), variable= Tipo, value=2)
rbutton1.place(x= 600, y= 275)

label3 = Label(root, text="Inicial", bg='#FFC7FA',fg='black', width=0, font=("BubbleGum", 30))
label3.place(x= 600, y= 350)
texboxdos = Entry(root, text=" ", bg='white',fg='black', width=8, font=("BubbleGum", 30 ))
texboxdos.place(x=720, y= 350)
label4 = Label(root, text="Saldo", bg='#FFC7FA',fg='black', width=0, font=("BubbleGum", 30))
label4.place(x= 600, y= 420)
texboxtres = Entry(root, text=" ", bg='white',fg='black', width=8, font=("BubbleGum", 30 ))
texboxtres.place(x=720, y= 420)
imagen = PhotoImage(file="consecionario.png")
Labelimagen = Label(root, image= imagen)
Labelimagen.pack()
Labelimagen.config(width="300", height="300")
Labelimagen.place(x=50, y=20)
button1 = Button(root, text='Calcular', width=10, height=1, font=('BubbleGum', 30), bg='#FF4131', fg='white', command= Calcular)
button1.place(x=50, y=330)
button2 = Button(root, text='Limpiar', width=10, height=1, font=('BubbleGum', 30), bg='#FF4131', fg='white', command= hola)
button2.place(x=50, y=420)
button3 = Button(root, text='Salir', width=10, height=1, font=('BubbleGum', 30), bg='#FF4131', fg='white', command= hola)
button3.place(x=50, y=510)
root.mainloop()