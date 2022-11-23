import datasource as ds


def main():
    print("這裡是main function的執行點")
    all_data=ds.get_forcast_data(ds.tw_county_names["基隆"])
    for item in all_data:
        print(item['dt_txt'])

if __name__=="__main__":
    print("這裡是程式的執行點")
    main()