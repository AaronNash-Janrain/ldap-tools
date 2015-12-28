import string, defaults

class Entry(dict):
    def __init__(self, cn = None, ou = None, **kwargs):
        super(Entry, self).__init__()
        if cn == None or ou == None:
            raise TypeError("New entries require at minimum cn= and ou=")
        entry = {}
        entry['cn'] = [cn]
        for key in kwargs:
            entry[key] = [str(kwargs[key])]
        self.update(
            dn = "cn=%s,ou=%s,%s" % (cn, ou, defaults.BASE),
            entry = entry
        )

    def populate_defaults(self):
        raise NotImplementedError

class UserEntry(Entry):
    def __init__(self, name, **kwargs):
        super(Entry, self).__init__(cn = name, ou = defaults.ORGANIZATIONAL_UNITS['users'], **kwargs)

    def populate_defaults(self):
        name = self['entry']['cn'][0].split(' ')
        self['entry']['givenName'] = [name[0]]
        self['entry']['sn'] = [name[1] if len(name) >= 2 else name[0]]
        self['entry']['uid'] = [
            string.lower(self['entry']['givenName'][0][0]) + string.lower(self['entry']['sn'][0])
            if self['entry']['givenName'] != self['entry']['sn']
            else string.lower(self['entry']['givenName'][0])
        ]
        self['entry']['gidNumber'] = [defaults.GID]
        self['entry']['homeDirectory'] = [defaults.HOME + self['entry']['uid'][0]]
        self['entry']['loginShell'] = [defaults.SHELL]
        self['entry']['objectClass'] = defaults.U_OBJECTS

class GroupEntry(Entry):
    def __init__(self, name, **kwargs):
        super(Entry, self).__init__(cn = Name, ou = defaults.ORGANIZATIONAL_UNITS['groups'], **kwargs)

    def populate_defaults(self):
        self['entry']['objectClass'] = defaults.G_OBJECTS

class SudoEntry(Entry):
    def __init__(self, name, **kwargs):
        super(Entry, self).__init__(cn = name, ou = defaults.ORGANIZATIONAL_UNITS['sudoers'], **kwargs)

    def populate_defaults(self):
        self['entry']['sudoUser'] = [self['entry']['cn'][0]]
        self['entry']['sudoCommand'] = [defaults.COMMANDS]
        self['entry']['sudoHost'] = [defaults.HOSTS]
        self['entry']['objectClass'] = defaults.S_OBJECTS

class EntryFactory():
    entry_types = {'user': UserEntry, 'group': GroupEntry, 'sudoer': SudoEntry}
    @staticmethod
    def create_entry(type_string, name, **kwargs):
        return entry_types[type_string](name, **kwargs)

class EntryCollection(dict):
    def __init__(self, *args, **kwargs):
        super(EntryCollection, self).__init__()
        collection = []
        input_list = kwargs.pop('entry_list', None)
        try:
            combined = (input_list + list(args)) if input_list != None else args
            for entry in combined:
                if isinstance(entry, Entry):
                    collection.append(entry)
                else:
                    raise TypeError
        except TypeError:
            raise TypeError("Expected dictionaries (or list of dictionaries) of type Entry")
        self.update(entries = collection)
