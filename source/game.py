from datetime import datetime


class Game():

    def __init__(self, rawData):
        self.Title = rawData['game']['name']
        self.Platforms = [rawData['platform']['name']]
        self.PrettyReleaseDate = rawData['olavaSearchDate']
        self.ReleaseDate = datetime.strptime(self.PrettyReleaseDate, '%Y-%m-%d')
        self.Slug = self.Title + '-' + self.PrettyReleaseDate
        self.ReleaseDay = self.ReleaseDate.strftime('%A')
        self.ThumnailLink = ""
        if 'thumbnail' in rawData:
            self.ThumbnailLink = rawData['thumbnail']
        self.DetailLink = rawData['site_detail_url'].split('/releases/')[0]
        self.CalendarTitle = self.Title.replace(' ', '+')
        self.CalendarDate = self.PrettyReleaseDate.replace('-', '')
