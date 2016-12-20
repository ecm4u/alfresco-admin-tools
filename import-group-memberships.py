#!/usr/bin/env python3.5

import argparse
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument("tenant", type=str, nargs="?", default="default")
parser.add_argument("membersFile", type=str)
parser.add_argument("username", type=str)
parser.add_argument("password", type=str)
parser.add_argument("url", type=str, default="http://alf-host")
args = parser.parse_args()

tenant = args.tenant
url_base = args.url + "/alfresco/service/api/groups"
if args.tenant != "default":
    username = args.username + "@" + args.tenant
else:
    username = args.username
auth = (username, args.password)

groupName = args.membersFile.split(".")[1]

with open(args.membersFile) as f:
    members = json.load(f)["data"]
    for member in members:
        if member["authorityType"] == "GROUP":
            name = member["fullName"]
        else:
            name = member["shortName"]
        url = url_base + "/" + groupName + "/children/" + name
        print(url)
        res = requests.post(url, json={}, auth=auth)
        print(res)
