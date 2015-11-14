import os

configState = None


def get():
    global configState

    if configState == None:
        configState = OlavaConfig()
    return configState


class OlavaConfig():

    def __init__(self):
        self.MailChimpApiKey = os.environ.get("OLAVA_MANDRILL_API_KEY", "")
        self.GiantBombApiKey = os.environ.get("OLAVA_GIANTBOMB_API_KEY", "")
        self.MashapeApiKey = os.environ.get("OLAVA_MASHAPE_API_KEY", "")
        self.Users = os.environ.get("OLAVA_USERS", "")
        self.Platforms = os.environ.get("OLAVA_PLATFORMS", "")

    def listKeys(self):
        return [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
