import os
import config
import datetime
import json
import shutil


def destroy():
    shutil.rmtree(config.get().RequestCacheDirectory)


def read(slug):
    cacheDir = os.path.join(config.get().RequestCacheDirectory, slug)
    if not os.path.exists(cacheDir):
        os.makedirs(cacheDir)
    signature = datetime.datetime.now().date()
    cachePath = os.path.join(cacheDir+"/", str(signature)+".json")
    if not os.path.exists(cachePath):
        return None
    with open(cachePath) as cacheData:
        return json.load(cacheData)


def write(slug, data):
    cacheDir = os.path.join(config.get().RequestCacheDirectory, slug)
    if not os.path.exists(cacheDir):
        os.makedirs(cacheDir)
    signature = datetime.datetime.now().date()
    cachePath = os.path.join(cacheDir+"/", str(signature)+".json")
    if os.path.exists(cachePath):
        print("Overwriting cache "+cachePath)
    with open(cachePath, 'w') as cacheData:
        return json.dump(data, cacheData)
