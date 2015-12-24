from ldif import LDIFWriter, LDIFParser

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

	def write(self, data):
		for entry in data['entries']:
			self.writer.unparse(entry['dn'], entry['entry'])
