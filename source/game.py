from datetime import datetime
import giantbomb


class Game():

    def __init__(self, rawData):
        self.Title = rawData['game']['name']
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
            self.Info = self.Info['results']
            self.Description = self.Info['deck']
            self.Image = self.Info['image']['small_url']
