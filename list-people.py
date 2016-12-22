#!/usr/bin/env python3

# Export of all Alfresco people as JSON files.
#
# Copyright 2016 ecm4u GmbH
#
# Apache License, Version 2.0, January 2004, http://www.apache.org/licenses/

import argparse
import json
import requests
import sys

parser = argparse.ArgumentParser()
parser.add_argument("username", type=str)
parser.add_argument("password", type=str)
parser.add_argument("url", type=str, default="http://alf-host")
args = parser.parse_args()

url_base = args.url + "/alfresco/service/api/people"
auth = (args.username, args.password)

if "@" in args.username:
    tenant = args.username.split("@")[1]
else:
    tenant = "default"

res_people = requests.get(url_base, auth=auth, verify=False)
if res_people.status_code == 200:
    people = res_people.json()["people"]
    for person in people:
        userName = person["userName"]
        print(",".join([tenant, userName]))
else:
    print(res_people)
    sys.exit(1)
