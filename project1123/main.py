import datasource as ds
from secrets import api_key
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()


def main():
    window=Window()
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