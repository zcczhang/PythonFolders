# Author: CZ
# Time: 2019-07-06 14:31 
"""
    Program for:
    Currency Converter
    BMR Calculator
    Find a Day
    Save Money
    Setting Password Tool

"""
import re
import json
import urllib.request
import math
from easygui import*
import sys
from datetime import*
from PasswordTool import PasswordTool

alllist = ['Currency Converter', 'BMR Calculator', 'Find a Day', 'Save Money', 'Setting Password Tool']


# Currency Converter
def usdcny():
    url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXUSDCNY&column=Code,Price"
    req = urllib.request.Request(url)
    f = urllib.request.urlopen(req)
    html = f.read().decode("utf-8")
    s = re.findall("{.*}", str(html))[0]
    sjson = json.loads(s)
    r = sjson["Data"][0][0][1]/10000
    return r
# def convc1():
#     val_str = input('value（$/￥): ')
#     while val_str[1:].isdigit():
#         out = lambda x, y: x * y
#         if val_str.startswith('$'):
#             print('￥', out(eval(val_str[1:]), USD_vs_CNY))
#         elif val_str.startswith('￥'):
#             print('$', out(eval(val_str[1:]), 1/USD_vs_CNY))
#         else:
#             break
#         print('——————————————————————————')
#         val_str = input('value（$/￥): ')
#     print('already quit')


# def convc2(val_str):
#     def rate(r):
#         nonlocal val_str
#         while val_str[1:].isdigit():
#             if val_str.startswith('$'):
#                 print('￥', eval(val_str[1:]) * r)
#             elif val_str.startswith('￥'):
#                 print('$', eval(val_str[1:]) / r)
#             else:
#                 break
#             print('——————————————————————————')
#             val_str = input('value（$/￥): ')
#     return rate
def convc():
    try:
        val_list = multenterbox(msg='Fill the Value',
                                title='Currency Converter', fields=['value（$/￥): '])
        val_str = val_list[0]
        r = usdcny()
        while val_str[1:].isdigit():
            if val_str.startswith('$'):
                msgbox('Real Time Exchange Result: ￥ {}'.format(eval(val_str[1:]) * r), datetime.now())
                break
            elif val_str.startswith('￥'):
                msgbox('Real Time Exchange Result: $ {}'.format(eval(val_str[1:]) / r), datetime.now())
                break
            else:
                redo(1)
    except:
        main()
    redo(1)


# BMR Calculator
def bmrc():
    list2 = ['Gender(M/F)', 'Weight(kg)', 'Height(cm)', 'Age']
    str_list = multenterbox(msg='Fill in values for the fields.',
                            title='Calculate the BMr', fields=list2)
    try:
        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])

        if gender == 'M':
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == 'F':
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            msgbox('Gender：{}，Weight：{}kg，Height：{}cm，Age：{}'.format(gender, weight, height, age)+
                   '\n'+'Basal Metabolic Rate(BMR)：{} kilocalorie'.format(bmr), 'Result')
        else:
            msgbox('wrong gender')
    except ValueError as rsn1:
        msgbox('wrong info\nBecause: ' + str(rsn1))
    except IndexError as rsn2:
        msgbox('less info\nBecause: ' + str(rsn2))
    except:
        main()
    redo(2)


# Find a Day
def is_leap_year(year):

    is_leap = False

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True

    return is_leap


def daysinayr():
    try:
        list0 = ['Date']
        input_date_list = multenterbox(msg='Fill the Date in a year(Y.M.D.): ',
                                       title='How many days past in a year', fields=list0)
        input_date_str = input_date_list[0]
        input_date = datetime.strptime(input_date_str, '%Y.%m.%d')

        year = input_date.year
        month = input_date.month
        day = input_date.day

        day_month_dict = {30: {4, 6, 9, 11},
                          31: {1, 3, 5, 7, 8, 10, 12}}

        days = 0

        for i in range(1, month):
            if i in day_month_dict[30]:
                days += 30
            else:
                days += 31

        if is_leap_year(year) and month > 2:
            days -= 2
        else:
            days -= 3

        days += day

        msgbox('This is No.{} day in year {}.'.format(days, year))
        redo(3)
    except TypeError:
        main()
    except ValueError:
        msgbox('Wrong info')
        redo(3)


# Save Money
def save_accountlist(money_1_week, increase_money, total_week):
    moneylist = []
    account = []
    for i in range(total_week):
        moneylist.append(money_1_week)
        money_1_week += increase_money
        saving = math.fsum(moneylist)
        account.append(saving)
    return account


def savemoney():
    try:
        list0 = ['Saving End Date(yyyy.mm.dd): ', 'The first week saving: ',
                 'Increment of savnig per week: ']
        input_date_list = multenterbox(msg='Fill the Date in a year(Y.M.D.): ',
                                       title='Save Money', fields=list0)
        input_date_str = input_date_list[0]
        money_1_week = eval(input_date_list[1])
        increase_money = eval(input_date_list[1])

        input_date = datetime.strptime(input_date_str, '%Y.%m.%d')
        # 'date.isocalendar()' return: (year, nth week, day of the week)
        week_num = input_date.isocalendar()[1]

        account = save_accountlist(money_1_week, increase_money, week_num)

        msgbox('You will have savig {1} in {0} weeks'.format(week_num, account[week_num - 1]))
        redo(4)
    except TypeError:
        main()
    except:
        redo(4)


def pwt():
    try_times = 5
    try:
        while try_times > 0:
            password = passwordbox('Password: ', 'Setting the Password')
            password_tool = PasswordTool(password)
            password_tool.process_password()

            if password_tool.strength_level == 3:
                msgbox('Successfully Setting!')
                break
            else:
                msgbox('Fail to Set!')
                try_times -= 1
                continue
        if try_times <= 0:
            msgbox('You reached the maximum attempts')
    except TypeError:
        main()


def redo(num):
    while 1:
        cc = buttonbox('Redo this program?', str(datetime.now()),
                       ['Redo', 'No', 'Quit all'])
        if cc == 'Redo':
            if num == 1:
                convc()
            if num == 2:
                bmrc()
            if num == 3:
                daysinayr()
            if num == 4:
                savemoney()
        elif cc == 'No':
            break
        else:
            sys.exit(0)


# main function
def main():
    call_str = choicebox('Choose a program to run: ', title='Selection page', choices=alllist)
    if call_str == alllist[0]:
        convc()
    elif call_str == alllist[1]:
        bmrc()
    elif call_str == alllist[2]:
        daysinayr()
    elif call_str == alllist[3]:
        savemoney()
    elif call_str == alllist[4]:
        pwt()
    while 1:
        if ccbox('Change to another program?', str(datetime.now()), choices=['Yes', 'No']):
            main()
        else:
            sys.exit(0)


if __name__ == '__main__':
    main()
