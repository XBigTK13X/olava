import os
import datetime
import config
import pickle

from jinja2 import Environment, FileSystemLoader
pwd = os.path.dirname(os.path.abspath(__file__))
templates = Environment(loader=FileSystemLoader(os.path.join(pwd, 'templates')))


def createIndex(games,
                platforms,
                platformsOrder,
                dayOrder,
                releaseCount,
                googleAnalyticsId):
    global templates
    rawData = {
        'games': games,
        'platforms': platforms,
        'dayOrder': dayOrder,
        'releaseCount': releaseCount,
        'googleAnalyticsId': googleAnalyticsId
    }
    template = templates.get_template('index.html')
    indexContent = template.render(games=games,
                                   platforms=platforms,
                                   platformsOrder=platformsOrder,
                                   dayOrder=dayOrder,
                                   releaseCount=releaseCount,
                                   googleAnalyticsId=googleAnalyticsId)
    if not os.path.exists(config.get().BuildOutputRoot):
        os.makedirs(config.get().BuildOutputRoot)
    indexPath = os.path.join(config.get().BuildOutputRoot, 'index.html')
    with open(indexPath, 'w') as indexFile:
        indexFile.write(indexContent)
    print("Index file written to "+indexPath)
    archiveRoot = os.path.join(config.get().BuildOutputRoot, 'archive')
    if not os.path.exists(archiveRoot):
        os.makedirs(archiveRoot)
    dateToday = datetime.date.today()
    archivePath = os.path.join(archiveRoot, str(dateToday))+".html"
    with open(archivePath, 'w') as archiveFile:
        archiveFile.write(indexContent)
    rawPath = archivePath.replace('.html', '.pickle')
    print("Archive file written to "+archivePath)
    with open(rawPath, 'wb') as fp:
        pickle.dump(rawData, fp)
    print("Pickled raw data file written to "+rawPath)
