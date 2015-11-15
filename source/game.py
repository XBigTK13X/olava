from datetime import datetime


class Game():

    def __init__(self, rawData, platform):
        self.Title = rawData['name']
        self.Platforms = [platform]
        self.PrettyReleaseDate = rawData['rlsdate']
        self.ReleaseDate = datetime.strptime(rawData['rlsdate'], '%Y-%m-%d')
        self.Slug = self.Title + '-' + self.PrettyReleaseDate
