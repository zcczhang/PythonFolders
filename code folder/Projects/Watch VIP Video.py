# Author: CZ
# Time: 2019-07-21 22:03

import re
import webbrowser
from urllib import parse
import tkinter as tk
import tkinter.messagebox as msgbox


class App(object):
    def __init__(self, width=500, height=300):
        self.width = width
        self.height = height
        self.title = ' VIP Video Play Helper '
        self.root = tk.Tk(className=self.title)
        # VIP video's url
        self.url = tk.StringVar()
        # video source
        self.source = tk.IntVar()
        # default selection
        self.source.set(1)

        # arrangement
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        group = tk.Label(frame_1, text='Video Chanel', padx=10, pady=10)
        tb = tk.Radiobutton(frame_1, text='Chanel ONE', variable=self.source, value=1, width=10, height=3)
        label = tk.Label(frame_2, text='Video Link: ')
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        play = tk.Button(frame_2, text='Play', fg='purple', width=2, height=1, command=self.video_play)
        frame_1.pack()
        frame_2.pack()
        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        play.grid(row=0, column=3, ipadx=10, ipady=10)

    def video_play(self):
        # url for parsing the video
        port = 'http://www.wmxz.wang/video.php?url='
        # prevent inputing illegal urls
        if re.match(r'^https?:/{2}\w.+$', self.url.get()):
            ip = self.url.get()
            ip = parse.quote_plus(ip)
            # open in the webpage
            webbrowser.open(port + ip)
        else:
            msgbox.showerror(title='Wrong', message='Invalid Video Link')

    def loop(self):
        self.root.resizable(True, True)
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.loop()
