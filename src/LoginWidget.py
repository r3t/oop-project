#! /usr/bin/env python
# -*- coding: utf-8 -*

import sys
import urlparse

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import uic

class LoginWidget(QtGui.QWidget):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self, parent)
		uic.loadUi(("./ui/loginwidget.ui"), self)
		# connect widgets
		self.webView.urlChanged.connect(self.webView_urlChanged)
		self.load_login_page()
	
	# widgets handlers
	
	def webView_urlChanged(self, url):
		new_url = str(url.toString())
		parsed_url = urlparse.urlparse(new_url)
		print urlparse.parse_qs(parsed_url.fragment)
		# Example:
		"""{'access_token': ['41441b294cd949d82918c8ce811bdf73d25b98158ab71efbf6d71c323b98a28798b169b5249b4c5f8361b'], 
		'user_id': ['4643070'], 'expires_in': ['0']}"""
		# TODO: Write data to config file or db
		
	# other methods
	
	def load_login_page(self):
		#TODO: Set login url parametrs
 		login_url = "http://api.vkontakte.ru/oauth/authorize?client_id=3989945" \
		"&scope=offline&redirect_uri=http://oauth.vk.com/blank.html&response_type=token"
		self.webView.load(QtCore.QUrl(login_url))

def main():
	app = QtGui.QApplication(sys.argv)
	w = LoginWidget()
	w.show()
	w.raise_()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()