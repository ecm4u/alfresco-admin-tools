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

tenant = args.membersFile.split(".")[0]
auth = (args.username, args.password)

res_groups = requests.get(url_base, params={"shortNameFilter": "*"}, auth=auth)
if res_groups.status_code == 200:
    groups = res_groups.json()["data"]
    for group in groups:
        groupShortName = group["shortName"]
        res_members = requests.get("{}/{}/children".format(url_base, groupShortName), auth=auth)
        if res_members.status_code == 200:
            totalItems = res_members.json()["paging"]["totalItems"]
            if totalItems == 0:
                print(",".join([args.tenant, groupShortName]))
else:
    print(res_groups)
    sys.exit(1)
