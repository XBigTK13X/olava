import os
import config
import metacritic
import cache
import game
import datetime

# cache.destroy()

games = {}


def addGame(game):
    global games
    if not game.Slug in games:
        games[game.Slug] = game
    else:
        games[game.Slug].Platforms = games[game.Slug].Platforms + game.Platforms

print("Reading in config for ENV: "+os.environ.get("OLAVA_ENV", "default"))
soon = metacritic.get_all(metacritic.coming_soon)
for key in soon.keys():
    print("Found " + str(len(soon[key]['results'])) + " " + key + " games coming soon")
    for entry in soon[key]['results']:
        addGame(game.Game(entry, key))

releases = metacritic.get_all(metacritic.new_releases)
for key in releases.keys():
    print("Found " + str(len(releases[key]['results'])) + " " + key + " games newly released")
    for release in releases[key]['results']:
        addGame(game.Game(release, key))

lowerBound = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
upperBound = (datetime.datetime.today() + datetime.timedelta(days=7)).replace(hour=0, minute=0, second=0, microsecond=0)
gamesInScope = [games[x] for x in games.keys()
                if games[x].ReleaseDate >= lowerBound
                and games[x].ReleaseDate < upperBound
                and (not 'pc' in games[x].Platforms or len(games[x].Platforms) > 1)]

for info in gamesInScope:
    print(info.Title+" is coming out "+info.PrettyReleaseDate+" for "+str(info.Platforms))
print("Found "+str(len(gamesInScope))+" unique game/release date combos within the next week")
