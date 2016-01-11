from datetime import datetime


class Game():

    def __init__(self, rawData):
        self.Title = rawData['game']['name']
        self.Platforms = [rawData['platform']['name']]
        self.PrettyReleaseDate = rawData['release_date']
        if self.PrettyReleaseDate is None or self.PrettyReleaseDate == 'None':
            paddedMonth = str(rawData['expected_release_month'])
            if len(paddedMonth) == 1:
                paddedMonth = '0'+paddedMonth
            paddedDay = str(rawData['expected_release_day'])
            if len(paddedDay) == 1:
                paddedDay = '0'+rawData['expected_release_day']
            self.PrettyReleaseDate = '{}-{}-{}'.format(
                rawData['expected_release_year'],
                paddedMonth,
                paddedDay)
        else:
            self.PrettyReleaseDate = self.PrettyReleaseDate.split(' ')[0]

        self.ReleaseDate = datetime.strptime(self.PrettyReleaseDate, '%Y-%m-%d')
        self.Slug = self.Title + '-' + self.PrettyReleaseDate
        self.ReleaseDay = self.ReleaseDate.strftime('%A')
        self.ThumnailLink = ""
        if 'thumbnail' in rawData:
            self.ThumbnailLink = rawData['thumbnail']
        self.DetailLink = rawData['site_detail_url'].split('/releases/')[0]
        self.CalendarTitle = self.Title.replace(' ', '+')
        self.CalendarDate = self.PrettyReleaseDate.replace('-', '')
