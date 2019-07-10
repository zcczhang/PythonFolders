# Author: CZ
# Time: 2019-07-07 00:17
"""
    EASYGUI
"""
from easygui import*
from datetime import datetime

login = multpasswordbox('Enter the Username and Passward: ',
                        'Log in to Read', ['Username: ', 'Password'])
if login[0] == '1' and login[1] == '1':
    msgbox('choose the file under the directory')
    path = fileopenbox(default='*.txt')
    textbox(msg='THE TRAGEDY OF ROMEO AND JULIET', title=str(datetime.now()),
            text=open(path))
else:
    msgbox('Wrong Username or Password')

