import os
import config
import metacritic
import cache
import game
import datetime
import builder
import reporter
import sys

# cache.destroy()

lowerBound = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

if len(sys.argv) > 1:
    print("Detected date argument, using that as the bound pivot: "+sys.argv[1])
    lowerBound = datetime.datetime.strptime(sys.argv[1], '%Y-%m-%d')

upperBound = lowerBound + datetime.timedelta(days=7)

games = {}
platforms = {}
gamesInScope = []
gamesByDay = {}
dayOrder = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
platformOrder = config.get().Platforms.split(',')
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
soon = metacritic.get_all(metacritic.coming_soon)
for key in soon.keys():
    for entry in soon[key]['results']:
        addGame(game.Game(entry, key))

releases = metacritic.get_all(metacritic.new_releases)
for key in releases.keys():
    for release in releases[key]['results']:
        addGame(game.Game(release, key))

gamesInScope = [games[x] for x in games.keys()
                if games[x].ReleaseDate >= lowerBound
                and games[x].ReleaseDate < upperBound
                and (not 'pc' in games[x].Platforms or len(games[x].Platforms) > 1)]

for info in gamesInScope:
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
releaseCount = len(gamesInScope)
print("Found "+str(releaseCount)+" unique game/release date combos within the next week")
builder.createIndex(gamesByDay,
                    platforms,
                    dayOrder,
                    releaseCount,
                    platformOrder,
                    config.get().GoogleAnalyticsId,
                    config.get().GoogleCalendarApiKey)

if len(config.get().Recipients) > 0:
    reporter.send(releaseCount)
    print("All finished emailing all users a link to the latest news")
else:
    print("No recipients defined. Skipping email send.")
