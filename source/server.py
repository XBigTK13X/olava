import os
import config

print("Reading in config for ENV: "+os.environ.get("OLAVA_ENV", "default"))
appConfig = config.get()
for key in appConfig.listKeys():
    print("Found "+key+" = "+getattr(appConfig, key))
