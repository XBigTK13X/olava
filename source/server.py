import os
import config
import reporter

print("Reading in config for ENV: "+os.environ.get("OLAVA_ENV", "default"))
