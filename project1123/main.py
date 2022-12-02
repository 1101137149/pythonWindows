import datasource as ds
from secrets import api_key
import tkinter as tk
from tkinter import ttk,messagebox

class Window(tk.Tk):
    def __init__(self,cities_dict):
        super().__init__()
        #建立Label pack是由上而下!
        tk.Label(self,text="各縣市4天天氣預測",font=('Arial',20)).pack(padx=30,pady=30) #類似CSS padding的設定 上下左右各推30

        #建立存放按鈕的容器
        buttons_frame=tk.Frame(self) #,background="#333333",width=200,height=300
        buttons_frame.pack(padx=115,pady=(0,30))


        #設定grid的row數量
        grid_row_nums = 3
        #enumerate 容器會建立一個索引 會傳回tuple型態 
        #cities_dict(index,key)  
        #cities_dict.items() (index,cities)  cities裡又包含(key,value)  command=self.button_click,

        for index,cities in enumerate(cities_dict.items()):
            cname, ename = cities
            btn=tk.Button(buttons_frame,text=f"{cname}\n{ename}",
            font=('arial',15),width=8,padx=20,pady=5)
            btn.grid(row=index % grid_row_nums,column=index // grid_row_nums)
            btn.bind('<Button>',self.button_click)
        
        


        #實體的方法 當按鈕按下去
    def button_click(self,event):
        #抓城市中文名、英文名
        btn_txt=event.widget['text']
        name_list=btn_txt.split("\n")
        cname=name_list[0]
        ename=name_list[1]
        
        #判斷是否是except
        errorLabel=False
        try:
            city_forcase=ds.get_forcast_data(ename,api_key)
        except Exception as e:
            print(e)
            city_forcase=None
            errorLabel=True
        finally:
            #LabelFrame
            if hasattr(self,"displayFrame") :
                self.displayFrame.destroy()
            self.displayFrame = DisplayFrame(self,data=city_forcase,text=cname,borderwidth=2,relief=tk.GROOVE)
            self.displayFrame.pack(fill=tk.BOTH,padx=50,pady=(0,30))



            #出現錯誤訊息 要補上錯誤對話框
            if  errorLabel:
                tk.Label(self.displayFrame, text="無資料!").pack(pady=10)
                messagebox.showwarning("無資料",f"{cname}沒有天氣資料")


class DisplayFrame(ttk.LabelFrame):
    def __init__(self,parent,data=None,**kwargs): #這裡的self是定義
        # print(kwargs) #kwargs被打包成dict
        super().__init__(parent,**kwargs)
        if data==None:
            return

        self.city_data=data

        #資料拆成3份
        total_rows=len(self.city_data)
        column_rows=total_rows//3+1

        leftData=self.city_data[:column_rows]
        centerData=self.city_data[column_rows:column_rows*2]
        rightData=self.city_data[column_rows*2:]


        leftFrame=CustomFrame(self,data=leftData)
        leftFrame.pack(side=tk.LEFT)

        centerFrame=CustomFrame(self,data=centerData)
        centerFrame.pack(side=tk.LEFT)

        rightFrame=CustomFrame(self,data=rightData)
        rightFrame.pack(side=tk.LEFT)





class CustomFrame(tk.Frame):
    def __init__(self,parent,data=None,**kwargs):#這裡的self是定義
        super().__init__(parent,**kwargs)


        self.list_data=data
        self.tree=ttk.Treeview(self,columns=['#1','#2','#3','#4'],show='headings',height=13)
        self.tree.pack(side=tk.LEFT,padx=10)

        scrollbar=tk.Scrollbar(self)
        scrollbar.pack(side=tk.LEFT,fill=tk.Y)
        self.tree.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tree.yview)

        self.tree.heading('#1',text="時間")
        self.tree.heading('#2',text="溫度")
        self.tree.heading('#3',text="狀態")
        self.tree.heading('#4',text="濕度")

        self.tree.column('#1',width=150,anchor="center")
        self.tree.column('#2',width=50,anchor="center")
        self.tree.column('#3',width=70,anchor="center")
        self.tree.column('#4',width=50,anchor="center")

        for item in self.list_data:
            self.tree.insert('',tk.END,values=item)





def main():
    window=Window(ds.tw_county_names)
    window.title("各縣市4天天氣預測")
    window.mainloop()



'''
    print("這裡是main function的執行點")
    try:
        list_data=ds.get_forcast_data(ds.tw_county_names["金門"],api_key)
    except Exception as e:
        print(e)
        return
    
    for item in list_data:
        print(item['dt_txt'])
'''
if __name__=="__main__":
    print("這裡是程式的執行點")
    main()