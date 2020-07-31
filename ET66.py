#__author__ = "Nicholas Schmidt"
#__license__ = "GPL"
#__maintainer__ = "Nicholas Schmidt"
#__email__ = "nchlsschmidt@gmail.com"
#__status__ = "Beta"


from math import *


from collections import namedtuple
import tkinter as tk

window = tk.Tk()
window.resizable(False, False)

Rect = namedtuple('Rect', 'x0, y0, x1, y1')

#the following class creates the rectangle for the gui
class ImageMapper(object):
    def __init__(self, image, img_rects):
        self.width, self.height = image.width(), image.height()
        self.img_rects = img_rects

    def find_rect(self, x, y):
        for i, r in enumerate(self.img_rects):
            if (r.x0 <= x <= r.x1) and (r.y0 <= y <= r.y1):
                return i
        return None

#the following class contains all the core functionality for the program
#It maps all the buttons in the calculator image to virtual buttons
#It listens for clicks and displays an output on the calculator screen accordingly
class ET66(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        input_text=tk.StringVar()

        tk.Entry(window, font=('Arial',20,"bold"),width=12,textvariable=input_text,bd=20,insertwidth=4,bg="#c5c7ba",justify="right").place(x=30,y=95)


    def create_widgets(self):
        self.msg_text = tk.StringVar()
        self.msg = tk.Message(self, textvariable=self.msg_text, width=100)
        self.msg.grid(row=0, column=0)

        self.picture = tk.PhotoImage(file='braunCalc35pct-2.gif')
        a = 34 #width of big buttons
        b = 20 #width of on/off buttons

# credit to martineau for starter code on representing "button areas" :
#https://stackoverflow.com/questions/37471878/hide-a-button-under-an-image-tkinter
######################################################################################
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
######################################################################################
    number = ""
    firstNum = None
    secondNum = None
    result = None
    operator = None
    mem = 0


    def calc_reset(): #currently not using this... didn't work when I tried to call it. I think it will work if I use "super()"
        self.result = None
        self.firstNum = None
        self.secondNum = None
        self.operator = None

    def evaluate():
        """
    	#debugging
        print ("num stored in firstNum:", self.firstNum)
        print ("num stored in secondNum:", self.secondNum)

        self.msg_text.set('eq clicked')
        if self.firstNum == None:
            self.result = self.number  
        else:
            self.secondNum = self.number
        print ("num stored in firstNum:", self.firstNum)
        print ("num stored in secondNum:", self.secondNum)
        if self.firstNum != None and self.secondNum == None:
            input_text.set(self.number)
            self.number = ''

            #handle the result of the operation based on the operator used
        if self.firstNum != None and self.secondNum != None:
            if self.operator == "+":
                self.result = str(float(self.firstNum) + float(self.secondNum))
                self.number = self. result
            elif self.operator == "-":
                self.result = str(float(self.firstNum) - float(self.secondNum))
                self.number = self.result
            elif self.operator == "*":
                self.result = str(float(self.firstNum) * float(self.secondNum))
                self.number = self.result
            elif self.operator == "/":
                self.result = str(float(self.firstNum) / float(self.secondNum))
                self.number = self.result
            elif self.operator == "del pct":
                	#https://sciencing.com/calculate-delta-percentage-8475192.html
                self.result = str((float(self.secondNum) - float(self.firstNum))/float(self.firstNum)*100)
                self.number = self.result
                print("result: ", self.result)

            #don't display trailing 0
        if self.result[-1] == "0" and self.result[-2] == ".":
            self.result = self.result[:-2]
        input_text.set(self.result)
        self.result = None
        self.firstNum = self.result
        self.secondNum = None
        self.operator = None

    	pass
    	"""

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
            self.mem += float(self.number)
            #self.mem = str(self.mem)
            #debugging
            print("mem: ", self.mem)
            self.number = ""


        elif hit == 11:
            self.msg_text.set('m- clicked')
            self.mem -= float(self.number)
            self.mem = str(self.mem)
            #debugging
            print("mem: ", self.mem)
            self.number = ""


        elif hit == 12:
            self.msg_text.set('mr clicked')
            #debugging
            print("str(mem): ", str(self.mem))
            print("mem: ", self.mem)
            self.display = ""
            #don't display trailing 0
            #if self.mem[-1] == "0" and self.mem[-2] == ".":
            #    self.mem = self.mem[:-2]

            input_text.set(str(self.mem))     
            
        elif hit == 13:
            self.msg_text.set('mc clicked')
            self.mem = 0

        elif hit == 14:
            self.msg_text.set('plmin clicked')

            if self.number != None:

	            if self.number[0] != "-" and len(self.number) > 1:
	            	self.number  = "-" + self.number

	            elif self.number[0] == "-" and len(self.number) > 1:
	            	self.number = self.number[1:]
	            	

            input_text.set(self.number)

        #most important case!
        elif hit == 15:

            #debugging
            print ("num stored in firstNum:", self.firstNum)
            print ("num stored in secondNum:", self.secondNum)

            self.msg_text.set('eq clicked')
            if self.firstNum == None:
                self.result = self.number  
            else:
                self.secondNum = self.number
            print ("num stored in firstNum:", self.firstNum)
            print ("num stored in secondNum:", self.secondNum)
            if self.firstNum != None and self.secondNum == None:
                input_text.set(self.number)
                self.number = ''

            #handle the result of the operation based on the operator used
            if self.firstNum != None and self.secondNum != None:
                if self.operator == "+":
                    self.result = str(float(self.firstNum) + float(self.secondNum))
                    self.number = self. result
                elif self.operator == "-":
                    self.result = str(float(self.firstNum) - float(self.secondNum))
                    self.number = self.result
                elif self.operator == "*":
                    if self.number == None or self.number == "":
                        self.number = "0"
                    self.result = str(float(self.firstNum) * float(self.secondNum))
                    self.number = self.result
                elif self.operator == "/":
                    #debugging
                    print("number: ", self.number)
                    if self.number == None or self.number == "":
                    	self.number = "0"
                    print("number: ", self.number)

                    if self.number != "0":
                        self.result = str(float(self.firstNum) / float(self.secondNum))
                        self.number = self.result
                    else:
                        self.result = "ERROR"
                elif self.operator == "del pct":
                    #https://sciencing.com/calculate-delta-percentage-8475192.html
                    self.result = str((float(self.secondNum) - float(self.firstNum))/float(self.firstNum)*100)
                    self.number = self.result
                    print("result: ", self.result)


            #don't display trailing 0
            if self.result[-1] == "0" and self.result[-2] == ".":
                self.result = self.result[:-2]
            input_text.set(self.result)
            self.result = None
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
            self.operator = "del pct"

            if self.firstNum == None:
                self.firstNum = self.number
            if self.firstNum != None and self.secondNum == None:
                pass
            else:
                self.secondNum = self.number
            self.number = ""

            #if self.firstNum != None and self.secondNum != None:
            #    self.result = str((float(self.secondNum) - float(self.secondNum))/float(self.secondNum)*100)
            #    self.firstNum = self.result
            #    input_text.set(self.result)


        elif hit == 20:
            self.msg_text.set('sqrt clicked')
            #debugging
            print ("num stored in firstNum:", self.firstNum)
            print ("num stored in secondNum:", self.secondNum)

            #if self.firstNum == None:
            #    self.firstNum = self.number
            #    self.firstNum = self.result
            #if self.firstNum != None and self.secondNum == None:
            #    pass

            self.result = sqrt(float(self.number))

            #don't display trailing 0
            self.result = str(self.result)
            if self.result[-1] == "0" and self.result[-2] == ".":
                self.result = self.result[:-2]
            input_text.set(self.result)

            #self.result = None
            self.number = self.result
            self.firstNum = self.result
            self.secondNum = None
            self.operator = None

            print ("num stored in firstNum:", self.firstNum)
            print ("num stored in secondNum:", self.secondNum)

        elif hit == 21:
            self.msg_text.set('pct clicked')
            #https://sciencing.com/divide-percent-using-calculator-7588458.html

			#debugging
            print ("num stored in firstNum:", self.firstNum)
            print ("num stored in secondNum:", self.secondNum)

            if self.firstNum == None:
                self.result = str(float(self.number) / 100)
            else:
                self.secondNum = self.number
            if self.firstNum != None and self.secondNum == None:
                input_text.set(self.number)
                self.number = ''

            if self.firstNum != None and self.secondNum != None:
                if self.operator == "+":
                    self.result = str(float(self.firstNum) + float(self.secondNum)/float(self.firstNum)*100)
                    self.number = self. result
                elif self.operator == "-":
                    self.result = str(float(self.firstNum) - float(self.secondNum)/float(self.firstNum)*100)
                    self.number = self.result
                elif self.operator == "*":
                    self.result = str(float(self.firstNum) * float(self.secondNum) / 100)
                    self.number = self.result
                elif self.operator == "/":
                    self.result = str(float(self.firstNum) / float(self.secondNum))
                    self.number = self.result

            #don't display trailing 0
            if self.result[-1] == "0" and self.result[-2] == ".":
                self.result = self.result[:-2]
            input_text.set(self.result)
            #self.result = None
            #self.firstNum = self.result
            #self.secondNum = None
            #self.operator = None


        elif hit == 22:
            self.msg_text.set('ce c clicked')
            self.number = "0"
            input_text.set(self.number)
            self.result = None
            self.firstNum = self.result
            self.secondNum = None
            self.operator = None


        elif hit == 23:
            self.msg_text.set('div clicked')
            input_text.set(self.number)

            self.operator = "/"
            if self.firstNum == None:
                self.firstNum = self.number
            if self.firstNum != None and self.secondNum == None:
                pass
            else:
                self.secondNum = self.number
            self.number = ""

        elif hit == 24:
            self.msg_text.set('mul clicked')
            input_text.set(self.number)

            self.operator = "*"
            if self.firstNum == None:
                self.firstNum = self.number
            if self.firstNum != None and self.secondNum == None:
                pass
            else:
                self.secondNum = self.number
            self.number = ""

            if self.firstNum != None and self.secondNum != None:
                self.result = str(float(self.firstNum) * float(self.secondNum))
                self.firstNum = self.result
                input_text.set(self.result)

        elif hit == 25:
            self.msg_text.set('sub clicked')
            #input_text.set(self.number)

            self.operator = "-"
            if self.firstNum == None:
                self.firstNum = self.number
            if self.firstNum != None and self.secondNum == None:
                pass
            else:
                #self.secondNum = self.number
                pass
            self.number = ""

            if self.firstNum != None and self.secondNum != None:
                self.result = str(float(self.firstNum) - float(self.secondNum))
                self.firstNum = self.result
                input_text.set(self.result)

        elif hit == 26:
            self.msg_text.set('add clicked')
            input_text.set(self.number)

            self.operator = "+"
            if self.firstNum == None:
                self.firstNum = self.number
            if self.firstNum != None and self.secondNum == None:
                pass
            else:
                self.secondNum = self.number
            self.number = ""

            if self.firstNum != None and self.secondNum != None:
                self.result = str(float(self.firstNum) + float(self.secondNum))
                self.firstNum = self.result
                input_text.set(self.result)

            #debugging
            print ("num stored in firstNum:", self.firstNum)
            print ("num stored in secondNum:", self.secondNum)

        else:
            #debugging
            #print ("num stored in firstNum:", self.firstNum)
            #print ("num stored in secondNum:", self.secondNum)
            display = str(hit)
            #trailing zeros (issue #4)
            #if self.number   == '0':
            #    display = ''
            self.number = self.number + display

            self.msg_text.set('{} clicked'.format(display))
            input_text.set(self.number)
app = ET66()
app.master.title('Braun ET66 Tribute')
app.mainloop()