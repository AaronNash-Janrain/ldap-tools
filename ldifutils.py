from ldif import LDIFWriter, LDIFParser
from ldap import modlist

class Parser(LDIFParser):
	def __init__(self, input):
		LDIFParser.__init__(self, input)
		self.data = {}
		self.data['entries'] = []

	def read(self):
		self.parse()
		return self.data

	def handle(self, dn, entry):
		self.data['entries'].append({
			'dn': dn,
			'entry': entry
		})

class Unparser():
	def __init__(self, output):
		self.writer = LDIFWriter(output)

	def write(self, dn, entry_or_modlist):
		self.writer.unparse(dn, entry_or_modlist)

def get_add_mod_list(entry):
	return modlist.addModlist(entry)

def get_modify_mod_list(old_entry, new_entry):
	return modlist.modifyModList(old_entry, new_entry)
