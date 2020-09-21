from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from json_settings import json_settings
from kivy.config import ConfigParser
from connector import *

config = ConfigParser('app')


class PopupWindow(Popup):
	def __init__(self, title, **kwargs):
		self.title = title
		super(PopupWindow, self).__init__(**kwargs)

class Interface(FloatLayout):

	def __init__(self, **kwargs):
		super(Interface, self).__init__(**kwargs)
		self.name = config.get('general', 'name') or None
		self.url = config.get('general', 'url') or None
		self.worksheet = config.get('general', 'worksheet') or None
		

	def checkIn(self):
		if (self.checkSettings()):
			try:
				c = Connector(self.name, self.url, self.worksheet)
			except Exception as e:
				self.showAlert('Error', str(e))
			else:
				checkedInAt = c.getCheckIn()
				if not checkedInAt:
					c.checkIn()
					self.showAlert('Success', 'You have successfully checked in.')
				else:
					self.showAlert('Warning', f'You have already checked in today at {checkedInAt}')


	def checkOut(self):
		if (self.checkSettings()):
			try:
				c = Connector(self.name, self.url, self.worksheet)
			except Exception as e:
				self.showAlert('Error', str(e))
			else:
				checkedOutAt = c.getCheckOut()
				if not checkedOutAt:
					c.checkOut()
					self.showAlert('Success', 'You have successfully checked out.')
				else:
					self.showAlert('Warning', f'You have already checked out today at {checkedOutAt}')

	def showAlert(self, status, message):
		popup = PopupWindow(title=status)
		popup.message.text = message
		popup.open()

	def checkSettings(self):
		if self.name is None or self.url is None or self.worksheet is None:
			self.showAlert('Warning', 'Please set the required settings first.')
			return False
		return True



class AttendanceApp(App):

	def __init__(self, **kwargs):
		super(AttendanceApp, self).__init__(**kwargs)
		self.use_kivy_settings = False



	def build_config(self, config):
		config.setdefaults('general',
		{
			'url': '',
			'name': '',
			'worksheet':''
		})

	def build_settings(self,settings):
		settings.add_json_panel('Attendance', self.config, data=json_settings)
		settings.font_size = .01, None


	def build(self):
		config = self.config
		return Interface()

	def on_config_change(self, config, section, key, value):
		if key == 'name':
			self.root.name = value

		if key == 'url':
			self.root.url = value

		if key == 'worksheet':
			self.root.worksheet = value



if __name__ == '__main__':
	AttendanceApp().run()

	