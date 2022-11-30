import datasource as ds
from secrets import api_key
import tkinter as tk

class Window(tk.Tk):
    def __init__(self,cities_dict):
        super().__init__()
        #建立Label pack是由上而下!
        tk.Label(self,text="各縣市4天天氣預測",font=('Arial',20)).pack(padx=30,pady=30) #類似CSS padding的設定 上下左右各推30

        #建立存放按鈕的容器
        buttons_frame=tk.Frame(self) #,background="#333333",width=200,height=300
        buttons_frame.pack(padx=50,pady=(0,30))


        #設定grid的row數量
        grid_row_nums = 3
        #enumerate 容器會建立一個索引 會傳回tuple型態 
        #cities_dict(index,key)  
        #cities_dict.items() (index,cities)  cities裡又包含(key,value)  

        for index,cities in enumerate(cities_dict.items()):
            cname, ename = cities
            btn=tk.Button(buttons_frame,text=f"{cname}\n{ename}",command=self.button_click,
            font=('arial',15),width=8,padx=20,pady=5)
            btn.grid(row=index % grid_row_nums,column=index // grid_row_nums)



        #實體的方法
    def button_click(self):
        print("User Click")



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