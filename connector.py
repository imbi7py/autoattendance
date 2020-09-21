import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
from datetime import datetime, timedelta

class Connector:

	def __init__(self, name, url, worksheet):
		self.name = name
		self.url = url
		self.worksheet = worksheet
		self.today = datetime.now().strftime('%A')
		self.current_time = datetime.now().strftime('%I:%M:%S %p')
		self.scope = ['https://www.googleapis.com/auth/spreadsheets']
		self.reg = re.compile(rf'{self.today}')
		self.processData()

	def checkIn(self):
		self.sheet.update_cell(self.row, self.inCol, self.current_time)

	def checkOut(self):
		self.sheet.update_cell(self.row, self.outCol, self.current_time)

	def getCheckIn(self):
		return self.sheet.cell(self.row, self.inCol).value

	def getCheckOut(self):
		return self.sheet.cell(self.row, self.outCol).value


	def processData(self):
		try:
			self.creds = ServiceAccountCredentials.from_json_keyfile_name('client.json', self.scope)
			self.client = gspread.authorize(self.creds)
		except:
			raise Exception('Check your json key file.')
		try:
			self.sheetKey = self.url.split('/')[5]
		except:
			raise Exception('Check your url. Must be google sheet url.')
		try:
			self.sheet = self.client.open_by_key(self.sheetKey).worksheet(self.worksheet)
		except:
			raise Exception('Couldn\'t find the sheet.')
		try:
			cell = self.sheet.find(self.reg)
			self.inCol = cell.col
			self.outCol = cell.col + 1
		except:
			raise Exception('Ah crap! must be weekend.')
		try:
			cell = self.sheet.find(self.name)
			self.row = cell.row
		except:
			raise Exception('Couldn\'t find your name.')




