import datetime
from datetime import date
import requests
import cache
import config
import time


def get_all(daysFromNow, startDate):
    results = []
    for ii in range(0, daysFromNow):
        targetDate = startDate + datetime.timedelta(days=ii)
        queryFormattedDate = str(targetDate)
        entries = lookup(queryFormattedDate)
        if 'results' in entries and len(entries['results']) > 0:
            for result in entries['results']:
                result['olavaSearchDate'] = targetDate.strftime("%Y-%m-%d")
            results.extend(entries['results'])
    return results


def lookup(searchDate):
    slug = 'giantbomb-'+searchDate+'-v11'
    cacheContent = cache.read(slug)
    if cacheContent != None:
        return cacheContent
    print("Hitting the GiantBomb API for "+searchDate)
    query = "http://www.giantbomb.com/api/releases/?api_key={}&format=json&filter=release_date:{},region:1".format(
        config.get().GiantBombApiKey,
        searchDate)
    headers = {
        'User-Agent': 'Olava Data Grabber',
        'From': 'info@olava.xyz'
    }
    # rate limit to 1 query per second
    time.sleep(1)
    response = requests.get(
        query,
        headers=headers
    )
    if response == None:
        print("Response wasn't populated for [{}].", query)
        import pprint
        pprint.pprint(vars(response))
        return {}
    try:
        entries = response.json()
    except ValueError as e:
        print("An error occurred while grabbing JSON.")
        import pprint
        pprint.pprint(vars(response))
        return {}
    cache.write(slug, entries)
    return entries
