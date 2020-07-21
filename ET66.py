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
        a = 34 #width of big buttons
        b = 20 #width of on/off buttons

        img_rects = [#number buttons
                     Rect(77,418,77+a,418+a), # btn 0
                     Rect(77,372,77+a,372+a), # btn 1
                     Rect(124,372,124+a,372+a), # btn 2
                     Rect(170,373,170+a,373+a), # btn 3
                     Rect(77,326,77+a,326+a), # btn 4
                     Rect(123,326,123+a,326+a), # btn 5                    
                     Rect(170,326,170+a,326+a), # btn 6
                     Rect(77, 280, 77+a, 280+a),    # btn 7
                     Rect(123, 279, 157, 313),      # btn 8
                     Rect(169, 280, 169 +a, 280+a), # btn 9

                     #green buttons
                     Rect(31,233,31+a,233+a), # btn m+
                     Rect(76,233,76+a,233+a), # btn m-
                     Rect(123,233,123+a,233+a), # btn mr
                     Rect(170,233,170+a,233+a), # btn mc
                     Rect(216,233,216+a,233+a), # btn plmin
                     Rect(170,418,170+a,418+a), # btn eq

                     #on and off buttons
                     Rect(37,170,37+b,170+b), # btn on
                     Rect(83,170,83+b,170+b), # btn off

                     #brown buttons
                     Rect(123,418,123+a,418+a), # btn dec
                     Rect(31,279,31+a,279+a), # btn del pct
                     Rect(31,326,31+a,326+a), # btn sqrt
                     Rect(31,372,31+a,372+a), # btn pct
                     Rect(31,418,31+a,418+a), # btn ce c
                     Rect(216,280,216+a,280+a), # btn div
                     Rect(216,326,216+a,326+a), # btn mul
                     Rect(216,373,216+a,373+a), # btn sub
                     Rect(216,418,216+a,418+a), # btn add
                     ]

        self.imagemapper = ImageMapper(self.picture, img_rects)
        # use Label widget to display image
        self.image = tk.Label(self, image=self.picture, borderwidth=0)
        self.image.bind('<Button-1>', self.image_click)
        self.image.grid(row=1, column=0)

    number = ""
    firstNum = None
    secondNum = None
    result = None
    operator = None
    mem = 0

    def calc_reset():
    	self.result = None
    	self.firstNum = None
    	self.secondNum = None
    	self.operator = None

    def image_click(self, event):
        input_text=tk.StringVar()
        tk.Entry(window, font=('Helvetica',20),width=12,textvariable=input_text,bd=20,insertwidth=4,bg="#c5c7ba",justify="right").place(x=30,y=95)

        hit = self.imagemapper.find_rect(event.x, event.y)
        
        if self.number == "0":
        	self.number = ""
        	self.result = '0'

        #display = None
        if hit is None:
            input_text.set(self.result)


        #could do a switch case here
        elif hit == 10:
            self.msg_text.set('m+ clicked')
            self.mem = self.number
            #debugging
            print("mem: ", self.mem)

        elif hit == 11:
            self.msg_text.set('m- clicked')

        elif hit == 12:
            self.msg_text.set('mr clicked')
            #debugging
            print("str(mem): ", str(self.mem))
            print("mem: ", self.mem)
            self.display = ""

            input_text.set(str(self.mem))     

        elif hit == 13:
            self.msg_text.set('mc clicked')

        elif hit == 14:
            self.msg_text.set('plmin clicked')

        #most important case!
        elif hit == 15:
            self.msg_text.set('eq clicked')
            if self.firstNum == None:
                self.result = self.number  
            else:
            	self.secondNum = self.number
            if self.firstNum != None and self.secondNum == None:
                input_text.set(self.number)
                self.number = ''

            if self.firstNum != None and self.secondNum != None:
            	if self.operator == "+":
            		self.result = str(int(self.firstNum) + int(self.secondNum))

            self.operator = None

            input_text.set(self.result)
            #self.result = None
            self.firstNum = self.result
            self.secondNum = None
            #self.operator = None

        elif hit == 16:
            self.msg_text.set('on clicked')
            self.number = "0"
            input_text.set(self.number)

        elif hit == 17:
            self.msg_text.set('off clicked')
            self.number = ""

            self.result = None
            self.firstNum = None
            self.secondNum = None
            self.operator = None

           
        elif hit == 18:
            self.msg_text.set('dec clicked')

            #not letting the user enter "." if there is already a "."
            #alternative option 
            if "." not in self.number and self.number != "":
                self.number += "."
            input_text.set(self.number)

        elif hit == 19:
            self.msg_text.set('del pct clicked')

        elif hit == 20:
            self.msg_text.set('sqrt clicked')

        elif hit == 21:
            self.msg_text.set('pct clicked')

        elif hit == 22:
            self.msg_text.set('ce c clicked')

        elif hit == 23:
            self.msg_text.set('div clicked')

        elif hit == 24:
            self.msg_text.set('mul clicked')

        elif hit == 25:
            self.msg_text.set('sub clicked')

        elif hit == 26:
            self.msg_text.set('add clicked')
            input_text.set(self.number)

            self.operator = "+"
            if self.firstNum == None:
                self.firstNum = self.number
            else:
            	self.secondNum = self.number
            self.number = ""

            if self.firstNum != None and self.secondNum != None:
            	self.result = str(int(self.firstNum) + int(self.secondNum))
            	self.firstNum = self.result
            	input_text.set(self.result)

            #debugging
            print ("num stored in firstNum:", self.firstNum)
            print ("num stored in secondNum:", self.secondNum)




        else:
            display = str(hit)
            #trailing zeros (issue #4)
            #if self.number   == '0':
            #    display = ''
            self.number = self.number + display

            self.msg_text.set('{} clicked'.format(display))
            input_text.set(self.number)


            

app = Demo()
app.master.title('Braun ET66 Tribute')
app.mainloop()