#from email.mime import image
import tkinter as tk
from PIL import Image,ImageTk
import tkinter.font as tkFont

class ImageButton(tk.Button):
    def __init__(self,parents,**kwargs): #**kwargs 打包
        super().__init__(parents,**kwargs) #**kwargs 打開
        btnimage1=Image.open('btn1.png')
        self.tkbtnImage1=ImageTk.PhotoImage(btnimage1)
        self.config(image=self.tkbtnImage1,borderwidth=0)


class Window(tk.Tk):
    def __init__(self):
        super().__init__() 
        
        #建立背景
        bgimage=Image.open('bg.jpg')
        self.tkImage=ImageTk.PhotoImage(bgimage) #如果沒有賦予self.會被消滅導致圖片出不來
        mainCanvas=tk.Canvas(self,width=600,height=427)
        mainCanvas.create_image(0,0,anchor=tk.NW,image=self.tkImage)
        mainCanvas.pack(fill=tk.BOTH,expand=True) #一定要設定括號裡的東西 不然寫東西進去時原先設定的寬高就會消失 會出不來
        
        #建立Lable
        helv26=tkFont.Font(family='Helvetica',size=26,weight='bold') #先設定字體格式
        tk.Label(mainCanvas,text="職能發展學院",font=helv26,bg="#C9C8CD",foreground="#888888").place(x=380,y=50)

        #建立ButtonsFrame
        buttonFrame=tk.Frame(mainCanvas,width=130,height=300,background="#FFFFFF")
        buttonFrame.place(x=100,y=50)

        #建立Button
        # btnimage1=Image.open('btn1.png')
        # self.tkbtnImage1=ImageTk.PhotoImage(btnimage1)
        btn1=ImageButton(buttonFrame,command=self.btn1Click)
        btn1.pack()

        btn2=ImageButton(buttonFrame,command=self.btn1Click)
        btn2.pack()
        
        

    def btn1Click(self):
        print("userClick")



        # btn1=tk.Button(buttonFrame,text="美麗花園",bd=0)
        # btn1.pack(padx=10,pady=10)


        #圖片處理
        # btnbgimage=Image.open('downloadbg.jpg').resize((150,50), Image.ANTIALIAS) #resize設定大小
        # self.tkbtnbgImage=ImageTk.PhotoImage(btnbgimage)
        # btn=tk.Button(mainCanvas,text="click",image=self.tkbtnbgImage,compound=tk.LEFT).pack()
        

def main():
    window=Window()
    window.title("Frame框架")
    window.resizable(0,0) #禁止拖拉視窗調整視窗大小
    window.geometry("640x427+300+200") #設定windows的大小和位置

    # bgimage=Image.open('bg.jpg')
    # tkImage=ImageTk.PhotoImage(bgimage)
    # mainCanvas=tk.Canvas(window,width=640,height=427)
    # mainCanvas.pack()
    # mainCanvas.create_image(0,0,anchor=tk.NW,image=tkImage)

    window.mainloop()


if __name__ =="__main__":
    main()

