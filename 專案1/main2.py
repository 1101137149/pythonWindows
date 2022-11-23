from email.mime import image
import tkinter as tk
from PIL import Image,ImageTk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        
        bgimage=Image.open('bg.jpg')
        self.tkImage=ImageTk.PhotoImage(bgimage) #如果沒有賦予self.會被消滅導致圖片出不來
        mainCanvas=tk.Canvas(self,width=600,height=427)
        mainCanvas.create_image(0,0,anchor=tk.NW,image=self.tkImage)

        #圖片處理
        btnbgimage=Image.open('downloadbg.jpg').resize((150,50), Image.ANTIALIAS) #resize設定大小
        self.tkbtnbgImage=ImageTk.PhotoImage(btnbgimage)
        btn=tk.Button(mainCanvas,text="click",image=self.tkbtnbgImage,compound=tk.LEFT,).pack()
        mainCanvas.pack(fill=tk.BOTH,expand=True) #一定要設定括號裡的東西 不然寫東西進去時原先設定的寬高就會消失 會出不來

def main():
    window=Window()
    window.title("Frame框架")
    window.geometry("640x427")

    # bgimage=Image.open('bg.jpg')
    # tkImage=ImageTk.PhotoImage(bgimage)
    # mainCanvas=tk.Canvas(window,width=640,height=427)
    # mainCanvas.pack()

    # mainCanvas.create_image(0,0,anchor=tk.NW,image=tkImage)

    window.mainloop()


if __name__ =="__main__":
    main()

