import os
import config
import metacritic
import cache

# cache.destroy()

print("Reading in config for ENV: "+os.environ.get("OLAVA_ENV", "default"))
soon = metacritic.get_all(metacritic.coming_soon)
for key in soon.keys():
    print("Found " + str(len(soon[key]['results'])) + " " + key + " games coming soon")

releases = metacritic.get_all(metacritic.new_releases)
for key in releases.keys():
    print("Found " + str(len(releases[key]['results'])) + " " + key + " games newly released")
