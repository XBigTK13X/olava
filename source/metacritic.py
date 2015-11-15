import requests
import cache
import config


def get_all(query):
    entries = {}
    for platform in config.get().Platforms.split(','):
        entries[platform] = query(platform.strip())
    return entries


def coming_soon(platform):
    return lookup(platform, 'coming-soon')


def new_releases(platform):
    return lookup(platform, 'new-releases')


def lookup(platform, category):
    slug = 'metacritic-'+category+"-"+platform
    cacheContent = cache.read(slug)
    if cacheContent != None:
        return cacheContent
    print("Hitting the metacritic API for "+category+" -> "+platform)
    headers = {
        'Accept': 'application/json',
        'X-Mashape-Key': config.get().MashapeApiKey
    }
    response = requests.get(
        "https://metacritic-2.p.mashape.com/game-list/"+platform+"/"+category,
        headers=headers
    )
    entries = response.json()
    cache.write(slug, entries)
    return entries
