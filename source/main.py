import os
import config
import giantbomb
import cache
import game
import datetime
import builder
import reporter
import sys

# cache.destroy()

startDate = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

if len(sys.argv) > 1:
    print("Detected date argument, using that as the bound pivot: "+sys.argv[1])
    startDate = datetime.datetime.strptime(sys.argv[1], '%Y-%m-%d')

games = {}
platforms = {}
gamesByDay = {}
dayOrder = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
releaseCount = 0


def addGame(game):
    global games
    if not game.Slug in games:
        games[game.Slug] = game
    for platform in game.Platforms:
        if not platform in games[game.Slug].Platforms:
            games[game.Slug].Platforms.append(platform)
    games[game.Slug].Platforms.sort()


print("Reading in config for ENV: "+os.environ.get("OLAVA_ENV", "default"))
releases = giantbomb.get_all(daysFromNow=7, startDate=startDate)
for release in releases:
    addGame(game.Game(release))

for key in games.keys():
    info = games[key]
    for platform in info.Platforms:
        if not platform in platforms:
            platforms[platform] = 0
        platforms[platform] = platforms[platform] + 1
    if not info.ReleaseDay in gamesByDay:
        gamesByDay[info.ReleaseDay] = []
    gamesByDay[info.ReleaseDay].append(info)
noReleases = []
for day in dayOrder:
    if not day in gamesByDay:
        noReleases.append(day)
dayOrder = [x for x in dayOrder if not x in noReleases]
for day in dayOrder:
    gamesByDay[day].sort(key=lambda x: x.Title)

print("There are "+str(len(noReleases))+" days this week with no releases")
releaseCount = len(games)
print("Found "+str(releaseCount)+" unique game/release date combos within the next week")

platformsOrder = [k for k in sorted(platforms)]

builder.createIndex(gamesByDay,
                    platforms,
                    platformsOrder,
                    dayOrder,
                    releaseCount,
                    config.get().GoogleAnalyticsId)

if len(config.get().Recipients) > 0:
    reporter.send(releaseCount)
    print("All finished emailing all users a link to the latest news")
else:
    print("No recipients defined. Skipping email send.")
