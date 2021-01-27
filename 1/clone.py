#!/usr/bin/env python
import sys
from os import environ
import json
import requests
from requests.auth import HTTPBasicAuth

NEW_NAME = "BuildMyApp"


## this could be implemented more cleanly, but it's clear enough and separates
## configuration from code, and allows users to specify security-sensitive
## information either at runtime or in the environment
try:
  server = environ['TFS_URL']
except KeyError:
  server = input("TFS/Devops Server root URL.  Include organization (eg, \"http://172.16.84.2/DefaultCollection\") This can be set in the TFS_URL environment variable.:")

try:
  auth = HTTPBasicAuth('user', environ['TFS_TOKEN'])
except KeyError:
  token = input("personal access token. This can be set in the TFS_TOKEN environment variable.:")
  auth = HTTPBasicAuth('user', token)
  


def dumpjson(relurl, debug=False):
  """helper function to get json from the server"""
  r = requests.get(server + relurl, auth=auth)
  j = json.loads(r.content)
  debug and print(json.dumps(j, indent=2))
  return j

def selectmenu(relurl, debug=False):
  """helper function to either return the only item or ask the user for a selection"""
  json = dumpjson(relurl, debug=debug)
  if json["count"] < 1:
    print("sorry, no items, quitting")
    sys.exit()

  if json["count"] == 1:
    return json["value"][0]["id"]

  for i, item in enumerate(json["value"]):
    print(i + 1, item["name"])
  selectedid = int(input("which item would you like (first column)? "))

  try:
     return json["value"][selectedid - 1]["id"]
  except KeyError:
     print("sorry, no such item- exiting")
     sys.exit()



if __name__=="__main__":
  # list projects
  # if only one project, proceed; otherwise ask
  print("PROJECTS")
  projid = selectmenu("/_apis/projects", debug=False)
  print("using project id %s" % (projid))

  # list build definitions
  # if only one def, proceed; otherwise ask
  print("BUILD DEFINITIONS")
  defid = selectmenu("/%s/_apis/build/definitions/" % (projid))

  d = dumpjson("/%s/_apis/build/definitions/%d" % (projid, defid))  # i would like to call this variable "def", but that's a keyword in python
  rev = d['revision']
  # https://www.danielemaggio.eu/devops/ado-rest-api-clone-build-release-def/
  # drop unnecessary keys
  for i in ["_links", "authoredBy", "queue._links", "queue.url", "queue.id", "url", "uri", "revision", "createdDate", "id"]:
    d.pop(i, None)
  # rename our new project
  d['name'] = NEW_NAME

  # fire away: generate our new build definition
  r = requests.post(server + "/%s/_apis/build/definitions/?definitionToCloneId=%d&definitionToCloneRevision=%d&api-version=6.0-preview" % (projid, defid, rev), auth=auth, json=d)
  print(r.content)
