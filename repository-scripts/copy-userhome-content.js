var ps = people.getPeople("");
for each (var n in ps) {
	print("---");
	var p = search.findNode(n);
	var username = p.properties.userName;
	print("username: " + username);
	var userhome = p.properties.homeFolder;
	print("userhome: " + userhome.nodeRef);
	for each (var uh in userhome.parent.children) {
		var r = RegExp("^" + username + "-\\d+$");
		if (uh.name.match(r) && "" + uh.nodeRef != "" + userhome.nodeRef) {
			print("matching userhome: " + uh.name);
			for each (var c in uh.children) {
				print("copy " + c.name);
				// var cp = c.copy(userhome);
				// cp.setOwner(username);
			}
		}
	}
}
