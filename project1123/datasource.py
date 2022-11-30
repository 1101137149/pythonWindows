#datasource 主要是下載資料和處理資料用 
import requests


tw_county_names = {"台北":"Taipei",
                   "台中":"Taichung",
                   "基隆":"Keelung",
                   "台南":"Tainan",
                   "高雄":"Kaohsiung",
                   "新北":"New Taipei",
                   "宜蘭":"Yilan",
                   "桃園":"Taoyuan",
                   "嘉義":"Chiayi",
                   "新竹":"Hsinchu",
                   "苗栗":"Miaoli",
                   "南投":"Nantou",
                   "彰化":"Changhua",
                   "雲林":"Yunlin",
                   "屏東":"Pingtung",
                   "花蓮":"Hualien",
                   "台東":"Taitung",
                   "金門":"Kinmen",
                   "澎湖":"Penghu",
                   "連江":"Lienchiang"
                   }


def get_forcast_data(cityName,api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={cityName},tw&APPID={api_key}&lang=zh_tw&units=metric"
    response=requests.get(url=url)
    county_forcase=[]  #list

    if response.ok:
        print(cityName+"下載成功")
        source_data= response.json()['list']
        for item in source_data:
            #建立list資料丟到county_forcase裡
            county_forcase.append([item["dt_txt"],item["main"]["temp"],item["weather"][0]["description"],item["main"]["humidity"]]) 

        return(county_forcase)

    else:
        raise Exception(cityName+"下載失敗") #自己定義raise 拋出自定義的錯誤訊息
