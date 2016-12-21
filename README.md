# alfresco-admin-tools
Tools for Alfresco Administration

## Export and Import Group Members

Alfresco provides a REST API to handle group memberships. This API
can be used to export and import the members of groups to and from
JSON files.

Two Python scripts wrap this REST API:

* `export-group-memberships.py`
* `import-group-memberships.py`

## Installation

No installation is necessary.

The required library is [Requests](http://docs.python-requests.org/en/master/).

## Usage

### Export

    $ python3.5 export-group-memberships.py admin secret http://alfresco-host

This creates a JSON file for each group in the local directory.

    default.GROUP_NAME1.members.json
    default.GROUP_NAME2.members.json
    ...

If you want to export the groups of a tenant, add `@tenantname` to the username:

    $ python3.5 export-group-memberships.py admin@tenantname secret http://alfresco-host

The JSON files will include the tenant name.

    tenantname.GROUP_NAME1.members.json
    tenantname.GROUP_NAME2.members.json
    ...

### Import

    $ python3.5 import-group-memberships.py admin secret http://alfresco-host tenant.groupname.members.json

The REST API returns a HTTP status code `500` if the authority already was a member of the group. This is a little bit annoying.

Again, adding the `@tenantname` to the username will import into the selected tenant.
