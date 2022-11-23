import tkinter as tk #GUI圖型介面工具包 as命名小名可簡化名稱

'''
#函數寫法
def createWindow():
    window=tk.Tk() #建立一個視窗實體
    window.title("這是我的第一個視窗") #視窗的title名稱
    btn=tk.Button(window,text="請按我",padx=20,pady=20,font=('arial',16)) #放在window變數裡，按鈕顯示請按我 按鈕內行距長寬20px
    btn.pack(padx=50,pady=30) #視窗大小 寬50 高30
    window.mainloop()
'''

#class寫法
class Window(tk.Tk):
    def __init__(self):
        super().__init__() #去繼承副類別的所有屬性
        self.title("這是我的第一個視窗")
        btn=tk.Button(self,text="請按我",padx=20,pady=20,font=('arial',16),command=self.userClick).pack(padx=50,pady=30) 

    def userClick(self):
        print("userClick")

def main():
    #函數呼叫寫法
    #createWindow()

    #Class呼叫寫法
    window=Window()
    window.mainloop()

if __name__ =="__main__":
    main()