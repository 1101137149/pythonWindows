#視窗要跟背景圖一樣大小(以背景圖大小為主) 背景圖不要太花
#視窗不可以任意調整大小
#用Class 建立Label


#(進虛擬環境) 把將套件的資訊存到requirements.txt
#pip freeze > requirements.txt
#(進虛擬環境) 將requirements.txt 裡的套件直接安裝環境
#pip install -r requirements.txt

import tkinter as tk
from turtle import bgcolor
from PIL import Image,ImageTk
import tkinter.font as tkFont

class TKLable(tk.Label):
    def __init__(self,parents,**kwargs):
        super().__init__(parents,**kwargs)
        helv26=tkFont.Font(family='Helvetica',size=26,weight='bold') #先設定字體格式
        self.config(font=helv26,bg= '#FCE9E9',foreground="#E9B3B2")


#建立視窗
class Window(tk.Tk):
    def __init__(self):
        super().__init__() 

        #建立背景
        bgimage=Image.open('homeworkbg.jpg')
        self.tkImage=ImageTk.PhotoImage(bgimage) #如果沒有賦予self.會被消滅導致圖片出不來
        mainCanvas=tk.Canvas(self,width=600,height=427)
        mainCanvas.create_image(0,0,anchor=tk.NW,image=self.tkImage)
        mainCanvas.pack(fill=tk.BOTH,expand=True) #一定要設定括號裡的東西 不然寫東西進去時原先設定的寬高就會消失 會出不來

        #建立Lable
        TKLable(mainCanvas,text="Python視窗作業").place(x=150,y=450)

        TKLable(mainCanvas,text="Lable Class應用").place(x=150,y=500)

def main():
    window=Window()
    window.title("homework")
    window.resizable(0,0) #禁止拖拉視窗調整視窗大小
    window.geometry("564x1002+500+0") #設定windows的大小和位置


    window.mainloop()


if __name__ =="__main__":
    main()

