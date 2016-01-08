import os

configState = None


def get():
    global configState

    if configState == None:
        configState = OlavaConfig()
    return configState


class OlavaConfig():

    def __init__(self):
        self.MandrillApiKey = os.environ.get("OLAVA_MANDRILL_API_KEY", "")
        self.GiantBombApiKey = os.environ.get("OLAVA_GIANTBOMB_API_KEY", "")
        self.MashapeApiKey = os.environ.get("OLAVA_MASHAPE_API_KEY", "")
        self.Recipients = os.environ.get("OLAVA_RECIPIENTS", "")
        self.FromEmailAddress = os.environ.get("OLAVA_FROM_EMAIL_ADDRESS", "")
        self.FromEmailName = os.environ.get("OLAVA_FROM_EMAIL_NAME", "")
        self.RequestCacheDirectory = os.environ.get("OLAVA_REQUEST_CACHE_DIRECTORY", "")
        self.BuildOutputRoot = os.environ.get("OLAVA_BUILD_OUTPUT_ROOT", "")
        self.GoogleAnalyticsId = os.environ.get("OLAVA_GOOGLE_ANALYTICS_ID", "")
        self.GoogleCalendarApiKey = os.environ.get("OLAVA_GOOGLE_CALENDAR_API_KEY", "")

    def listKeys(self):
        return [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
