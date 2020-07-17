from collections import namedtuple
import tkinter as tk
from math import *



window = tk.Tk()
Rect = namedtuple('Rect', 'x0, y0, x1, y1')

class ImageMapper(object):
    def __init__(self, image, img_rects):
        self.width, self.height = image.width(), image.height()
        self.img_rects = img_rects

    def find_rect(self, x, y):
        for i, r in enumerate(self.img_rects):
            if (r.x0 <= x <= r.x1) and (r.y0 <= y <= r.y1):
                return i
        return None

class Demo(tk.Frame):


    

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

        ancho_boton=6
        active_round=False
        numero=("")
        blocked_ce=False
        comas=0
        reep=""
        alto_boton=2
        prev_sign=""
        input_text=tk.StringVar()
        #clear()#MUESTRA VALOR "0" AL INICIAR LA CALCULADORA
        bd=10


        def digit(n):
                global numero
                global l_numeros
                global blocked_ce
                blocked_ce=False
                long=len(l_numeros)
                if long<2 and numero!=str(pi):
                    if numero=="0":
                        numero=numero.replace("0",n)
                    else:
                        numero=numero+n
                    input_text.set(numero)

        def loga():
            global l_numeros
            global numero
            if len(l_numeros)==2:
                try:
                    numero=str(eval("log("+l_numeros[0]+")/log("+l_numeros[1]+")")) #l_numeros[0] es el numero y l_numeros[1] es la base
                    input_text.set(numero)
                    l_numeros[0]=numero
                    l_numeros.pop()
                except:
                    input_text.set("ERROR")
                    l_numeros=[]
                numero=""

        def image_click(self, event):
            hit = self.imagemapper.find_rect(event.x, event.y)

            display = None
            if hit is 0:
                display = '8'
            if hit is 1:
                display = '1'
            self.msg_text.set('{} clicked'.format(display))
            input_text.set(8)

        def eight():
            global numero
            global l_numeros
            global comas
            global blocked_ce
            if len(l_numeros)<2 and numero=="":
                numero=str(pi)
                input_text.set(numero)
                comas+=1
                blocked_ce=False

        def pee():
            global numero
            global l_numeros
            global comas
            global blocked_ce
            if len(l_numeros)<2 and numero=="":
                numero=str(pi)
                input_text.set(numero)
                comas+=1
                blocked_ce=False

        def coma():
            global numero
            global comas
            if numero!="" and comas==0:
                numero=numero+"."
                input_text.set(numero)
                comas+=1

        def enter():
            global numero
            global l_numeros
            global comas
            global blocked_ce
            global active_round
            if numero!="" and numero!="0.":
                if active_round==True:
                    numero=str(eval("round("+str(numero)+")"))
                    l_numeros.append(numero)
                    active_round=False
                else:
                    l_numeros.append(numero)
                input_text.set(numero)
                numero=""
                comas=0
                blocked_ce=True

        def operacion(s):
            global numero
            global l_numeros
            global prev_sign
            global reep
            if len(l_numeros)==2:
                try:
                    numero=str(eval(l_numeros[0]+s+l_numeros[1]))
                    input_text.set(numero)
                    l_numeros[0]=numero
                    reep=l_numeros[1]
                    l_numeros.pop()
                    prev_sign=s
                    print(l_numeros)
                except:
                    input_text.set("ERROR")
                    l_numeros=[]
                numero=""
            elif len(l_numeros)==1 and prev_sign==s: 
                numero=eval(l_numeros[0]+s+reep)
                input_text.set(numero)
                l_numeros[0]=str(numero)
                print(l_numeros)
                numero=""

        def funci(s):
            global numero
            global l_numeros
            if len(l_numeros)==1:
                try:
                    numero=str(eval(s+"("+l_numeros[0]+")"))#[0]
                    input_text.set(numero)
                    l_numeros[0]=numero
                    prev_sign=s
                except:
                    input_text.set("ERROR")
                    l_numeros=[]
                numero=""

        def rounded():
            global numero
            global active_round
            global l_numeros
            if not numero.endswith("."):
                active_round=True
                if numero!="":
                    numero=eval("round("+str(numero)+")")
                    input_text.set(numero)
                else:
                    l_numeros[-1]=str(eval("round("+l_numeros[-1]+")"))
                    input_text.set(l_numeros[-1])
            
        def cambia_signo(): 
            global numero
            global l_numeros
            if numero!="0" and numero!="":
                numero=str(eval(numero+"*(-1)"))
                input_text.set(numero)
            elif numero=="" and len(l_numeros)==1: #nuevo
                if l_numeros[0]!="0":
                    l_numeros[0]=str(eval(l_numeros[0]+"*(-1)"))
                    input_text.set(l_numeros[0])

        def clear():
            global numero
            global l_numeros
            global comas
            numero=""
            l_numeros=[]
            input_text.set("0")
            comas=0

        def clear_error():
            global numero
            global comas
            global blocked_ce
            if blocked_ce==False:
                numero=""
                input_text.set("0")
                comas=0
                blocked_ce=True


        tk.Entry(window, font=('Arial',20,"bold"),width=12,textvariable=input_text,bd=20,insertwidth=4,bg="#c5c7ba",justify="right").place(x=30,y=95)


    def create_widgets(self):
        self.msg_text = tk.StringVar()
        self.msg = tk.Message(self, textvariable=self.msg_text, width=100)
        self.msg.grid(row=0, column=0)

        self.picture = tk.PhotoImage(file='braunCalc35pct-2.gif')
        a = 34
        img_rects = [
                     #number buttons
                     #Rect(,,,), # btn 0
                     #Rect(,,,), # btn 1
                     #Rect(,,,), # btn 2
                     #Rect(,,,), # btn 3
                     #Rect(,,,), # btn 4
                     #Rect(,,,), # btn 5                    
                     #Rect(,,,), # btn 6
                     #Rect(77, 280, 77+a, 280+a),    # btn 7
                     #Rect(123, 279, 157, 313),      # btn 8
                     #Rect(169, 280, 169 +a, 280+a), # btn 9

                     #green buttons
                     #Rect(,,,), # btn m+
                     #Rect(,,,), # btn m-
                     #Rect(,,,), # btn mr
                     #Rect(,,,), # btn mc
                     #Rect(,,,), # btn plmin
                     #Rect(,,,), # btn eq


                     #on and off buttons
                     #Rect(,,,), # btn on
                     #Rect(,,,), # btn off

                     #brown buttons
                     #Rect(,,,), # btn dec
                     #Rect(,,,), # btn del pct
                     #Rect(,,,), # btn sqrt
                     #Rect(,,,), # btn pct
                     #Rect(,,,), # btn ce c
                     #Rect(,,,), # btn div
                     #Rect(,,,), # btn mul
                     #Rect(,,,), # btn sub
                     #Rect(,,,), # btn add
                     ]

        #self.picture2 = tk.PhotoImage(file='braunCalc35pct-2.gif')
        #input_text = 8
        #window.configure(background="gray20")


        self.imagemapper = ImageMapper(self.picture, img_rects)
        # use Label widget to display image
        self.image = tk.Label(self, image=self.picture, borderwidth=0)
        self.image.bind('<Button-1>', self.image_click)
        self.image.grid(row=1, column=0)

    number = ""

    def image_click(self, event):
        input_text=tk.StringVar()
        tk.Entry(window, font=('Helvetica',20),width=12,textvariable=input_text,bd=20,insertwidth=4,bg="#c5c7ba",justify="right").place(x=30,y=95)

        hit = self.imagemapper.find_rect(event.x, event.y)
        display = None
        if hit is 0:
            display = '8'
            self.number = self.number + "8"
        if hit is 1:
            display = '7'
        self.msg_text.set('{} clicked'.format(display))
        input_text.set(self.number)


            

app = Demo()
app.master.title('Braun ET66 Tribute')
app.mainloop()