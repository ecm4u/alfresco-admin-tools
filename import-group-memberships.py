#!/usr/bin/env python3

# Import group members from a JSON file into Alfresco.
#
# Copyright 2016 ecm4u GmbH
#
# Apache License, Version 2.0, January 2004, http://www.apache.org/licenses/
#

import argparse
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument("username", type=str)
parser.add_argument("password", type=str)
parser.add_argument("url", type=str, default="http://alf-host")
parser.add_argument("membersFile", type=str)
args = parser.parse_args()

url_base = args.url + "/alfresco/service/api/groups"

tenant = args.membersFile.split(".")[0]
auth = (args.username, args.password)

groupName = args.membersFile.split(".")[1]

with open(args.membersFile) as f:
    members = json.load(f)["data"]
    for member in members:
        if member["authorityType"] == "GROUP":
            name = member["fullName"]
        else:
            name = member["shortName"]
        url = url_base + "/" + groupName + "/children/" + name
        res = requests.post(url, headers={"Content-Type": "application/json"}, auth=auth)
        print(url, res)
