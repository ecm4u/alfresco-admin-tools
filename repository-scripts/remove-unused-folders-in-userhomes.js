var realUserhomes = [];
for each (var n in people.getPeople("")) {
	var p = search.findNode(n);
	var userhome = p.properties.homeFolder;
	realUserhomes.push("" + userhome.nodeRef);
}
print("real userhomes: " + realUserhomes.length);

print("---");

for each (var userhome in search.luceneSearch('PATH:"/app:company_home/app:user_homes"')[0].children) {
	if (realUserhomes.indexOf("" + userhome.nodeRef) < 0) {
		print("" + userhome.name + " is no real userhome, removing it");
		// userhome.remove();
	}
}
