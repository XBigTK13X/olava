from datetime import datetime
import giantbomb
import urllib.parse

class Game():

	def __init__(self, rawData):
		self.Title = rawData['game']['name']
		self.SearchSlug = urllib.parse.quote_plus('video game ' + self.Title.lower())
		self.Platforms = [rawData['platform']['name']]
		self.PrettyReleaseDate = rawData['olavaSearchDate']
		self.ReleaseDate = datetime.strptime(self.PrettyReleaseDate, '%Y-%m-%d')
		self.Slug = self.Title + '-' + self.PrettyReleaseDate
		self.ReleaseDay = self.ReleaseDate.strftime('%A')
		self.DetailLink = rawData['site_detail_url'].split('/releases/')[0]
		self.CalendarTitle = self.Title.replace(' ', '+')
		self.CalendarDate = self.PrettyReleaseDate.replace('-', '')
		self.Info = giantbomb.game_info(rawData['game']['api_detail_url'])
		if 'results' in self.Info:
			if 'results' in self.Info:
				self.Info = self.Info['results']
				if 'deck' in self.Info:
					self.Description = self.Info['deck']
				if 'image' in self.Info and self.Info['image'] != None and 'small_url' in self.Info['image']:
					self.Image = self.Info['image']['small_url']
