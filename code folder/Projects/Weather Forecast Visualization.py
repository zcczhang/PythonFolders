# Author: CZ
# Time: 2019-07-06 12:14 
"""
    visualization of weather forecast
"""

from tkinter import *
import urllib.request
import gzip
import json
from tkinter import messagebox
root = Tk()


def main():
    # 输入窗口
    root.title('天气查询')  # 窗口标题
    Label(root, text='请输入城市').grid(row=0, column=0)  # 设置标签并调整位置
    enter = Entry(root)  # 输入框
    enter.grid(row=0, column=1, padx=20, pady=20)  # 调整位置

    running = 1

    def get_weather_data():  # 获取网站数据
        city_name = enter.get()  # 获取输入框的内容
        url1 = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city_name)
        weather_data = urllib.request.urlopen(url1).read()
        # 读取网页数据
        weather_data = gzip.decompress(weather_data).decode('utf-8')
        # 解压网页数据
        weather_dict = json.loads(weather_data)
        # 将json数据转换为dict数据

        if weather_dict.get('desc') == 'invilad-citykey':
            messagebox.askokcancel("提示", "你输入的城市名有误，或者天气中心未收录你所在城市")
        else:
            show_data(weather_dict, city_name)

    def show_data(weather_dict, city_name):  # 显示数据
        forecast = weather_dict.get('data').get('forecast')  # 获取数据块
        root1 = Tk()  # 副窗口
        root1.geometry('920x280')  # 修改窗口大小
        root1.title(city_name + '天气状况')  # 副窗口标题
        # 设置日期列表
        for i in range(5):  # 将每一天的数据放入列表中
            lans = [(forecast[i].get('date'), '日期'),
                    (forecast[i].get('fengxiang'), '风向'),
                    (str(forecast[i].get('fengli')), '风级'),
                    (forecast[i].get('high'), '最高温'),
                    (forecast[i].get('low'), '最低温'),
                    (forecast[i].get('type'), '天气')]
            group = LabelFrame(root1, text='天气状况', padx=0, pady=0, fg='red')  # 框架
            group.pack(padx=11, pady=0, side=LEFT)  # 放置框架
            for lang, value in lans:  # 将数据放入框架中
                c = Label(group, text=value + ': ' + lang)
                c.pack(anchor=W)
        Label(root1, text='今日' + weather_dict.get('data').get('ganmao'), fg='green')\
            .place(x=245, y=10, height=40)  # 温馨提示
        Label(root1, text="Author: CZ")\
            .place(x=0, y=240, width=125, height=20)
        Label(root1, text='实时温度: '+weather_dict.get('data').get('wendu')+'℃ ', fg='blue') \
            .place(x=10, y=20, width=125, height=20)
        Button(root1, text='确认并退出', width=10, command=root1.quit)\
            .place(x=820, y=230, width=80, height=40)  # 退出按钮
        root1.mainloop()
    # 布置按键
    Button(root, text="确认", width=10, command=get_weather_data)\
        .grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Button(root, text='退出', width=10, command=root.quit)\
        .grid(row=3, column=1, sticky=E, padx=10, pady=5)
    if running == 1:
        root.mainloop()


if __name__ == '__main__':
    main()
