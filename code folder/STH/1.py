
import sys
import time
import random
import hashlib
import requests
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QPushButton


class Youdao:
	"""
		youdao translator
	"""
	def __init__(self):
		self.headers = {
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
						'Referer': 'http://fanyi.youdao.com/',
						'Cookie': 'OUTFOX_SEARCH_USER_ID=-481680322@10.169.0.83;'
					}
		self.data = {
						'i': None,
						'from': 'AUTO',
						'to': 'AUTO',
						'smartresult': 'dict',
						'client': 'fanyideskweb',
						'salt': None,
						'sign': None,
						'ts': None,
						'bv': None,
						'doctype': 'json',
						'version': '2.1',
						'keyfrom': 'fanyi.web',
						'action': 'FY_BY_REALTlME'
					}
		self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

	def translate(self, word):
		ts = str(int(time.time()*10000))
		salt = str(int(time.time()*10000) + random.random()*10 + 10)
		sign = 'fanyideskweb' + word + salt + '97_3(jkMYg@T[KZQmqjTK'
		sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
		bv = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
		bv = hashlib.md5(bv.encode('utf-8')).hexdigest()
		self.data['i'] = word
		self.data['salt'] = salt
		self.data['sign'] = sign
		self.data['ts'] = ts
		self.data['bv'] = bv
		res = requests.post(self.url, headers=self.headers, data=self.data)
		return [res.json()['translateResult'][0][0].get('tgt')]


class Demo(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('YouDao Translator')
		self.setWindowIcon(QIcon('data/icon.jpg'))
		self.Label1 = QLabel('Words(Chinese/Engl)')
		self.Label2 = QLabel('Translation')
		self.LineEdit1 = QLineEdit()
		self.LineEdit2 = QLineEdit()
		self.translateButton2 = QPushButton()
		self.translateButton2.setText('Translate')
		self.grid = QGridLayout()
		self.grid.setSpacing(12)
		self.grid.addWidget(self.Label1, 1, 0)
		self.grid.addWidget(self.LineEdit1, 1, 2)
		self.grid.addWidget(self.Label2, 2, 0)
		self.grid.addWidget(self.LineEdit2, 2, 2)
		self.grid.addWidget(self.translateButton2, 3, 1)
		self.setLayout(self.grid)
		self.resize(400, 150)
		self.translateButton2.clicked.connect(lambda: self.translate())
		self.yd_translate = Youdao()

	def translate(self):
		word = self.LineEdit1.text()
		if not word:
			return
		else:
			results = self.yd_translate.translate(word)
		self.LineEdit2.setText(';'.join(results))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())
