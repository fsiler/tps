#!/usr/bin/env python3
from os import environ
import json
import logging
import coloredlogs
import requests
from requests.auth import HTTPBasicAuth

try:
  server = environ['TFS_URL']
except:
  server = input("TFS/Devops Server root URL (can be set in TFS_URL environment variable):")

try:
  auth = HTTPBasicAuth('user', environ['TFS_TOKEN'])
except KeyError:
  token = input("personal access token (can be set in TFS_TOKEN environment variable):")
  auth = HTTPBasicAuth('user', token)
  

def dumpjson(relurl):
  r = requests.get(server + relurl, auth=auth)
  j = json.loads(r.content)
  print(json.dumps(j, indent=2))
  return r


if __name__=="__main__":
#  dumpjson("/DefaultCollection/_apis/projects")
#  dumpjson("/DefaultCollection/_apis/projects/883dd4ef-7e52-4e5a-9a8f-06a4c17d4a49/properties")
#  dumpjson("/DefaultCollection/883dd4ef-7e52-4e5a-9a8f-06a4c17d4a49/_apis/build/definitions")
  dumpjson("/DefaultCollection/883dd4ef-7e52-4e5a-9a8f-06a4c17d4a49/_apis/build/definitions/1")
