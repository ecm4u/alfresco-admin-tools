#!/usr/bin/env python3

# Export of all Alfresco groups as JSON files.
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

url_base = args.url + "/alfresco/service/api/groups"
auth = (args.username, args.password)

if "@" in args.username:
    tenant = args.username.split("@")[1]
else:
    tenant = "default"

res_groups = requests.get(url_base, params={"shortNameFilter": "*"}, auth=auth)
if res_groups.status_code == 200:
    groups = res_groups.json()["data"]
    for group in groups:
        groupShortName = group["shortName"]
        res_members = requests.get("{}/{}/children".format(url_base, groupShortName), auth=auth)
        if res_members.status_code == 200:
            members = res_members.json()
            with open("{}.{}.members.json".format(tenant, groupShortName), "w") as w:
                w.write(json.dumps(members))
else:
    print(res_groups)
    sys.exit(1)
