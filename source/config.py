import os

configState = None


def get():
    global configState

    if configState == None:
        configState = OlavaConfig()
    return configState


class OlavaConfig():

    def __init__(self):
        self.BuildOutputRoot = os.environ.get("OLAVA_BUILD_OUTPUT_ROOT", "")
        self.GiantBombApiKey = os.environ.get("OLAVA_GIANTBOMB_API_KEY", "")
        self.GoogleAnalyticsId = os.environ.get("OLAVA_GOOGLE_ANALYTICS_ID", "")
        self.MailChimpApiKey = os.environ.get("OLAVA_MAILCHIMP_API", "")
        self.MailChimpListId = os.environ.get("OLAVA_MAILCHIMP_LIST_ID", "")
        self.OlavaEnv = os.environ.get("OLAVA_ENV", 'default')
        self.RequestCacheDirectory = os.environ.get("OLAVA_REQUEST_CACHE_DIRECTORY", "")

    def debug(self):
        keys = [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
        import pprint
        pprint.pprint(vars(self))
