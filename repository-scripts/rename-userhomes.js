/*
 * Rename userhome folders to match the username.
 * the real userhomes.
 *
 * Copyright 2016 ecm4u GmbH
 *
 * Apache License, Version 2.0, January 2004, http://www.apache.org/licenses/
 */
var ps = people.getPeople("");
for each (var n in ps) {
	var p = search.findNode(n);
	var username = p.properties.userName;
	if ("admin" == username || "guest" == username) {
		continue;
	}
	var userhome = p.properties.homeFolder;
	if ("" + userhome.properties.name != username) {
		print("---");
		print("reanming '" + userhome.properties.name + "' to '" + username + "' (" + userhome.nodeRef + ")");
		var existing = userhome.parent.childByNamePath(username)
		if (existing) {
			print("a folder named '" + username + "' already exists, can't rename");
		} else {
			userhome.name = username;
			userhome.save();
		}
	}
}
