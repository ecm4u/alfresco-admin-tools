#!/usr/bin/env python3.5

import argparse
import json
import requests
import sys

parser = argparse.ArgumentParser()
parser.add_argument("tenant", type=str, nargs="?", default="default")
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

res_groups = requests.get(url_base, params={"shortNameFilter": "*"}, auth=auth)
if res_groups.status_code == 200:
    groups = res_groups.json()["data"]
    for group in groups:
        groupShortName = group["shortName"]
        res_members = requests.get(url_base + "/" + groupShortName + "/children", auth=auth)
        if res_members.status_code == 200:
            members = res_members.json()
            with open("{}.{}.members.json".format(tenant, groupShortName), "w") as w:
                w.write(json.dumps(members))
else:
    print(res_groups)
    sys.exit(1)
