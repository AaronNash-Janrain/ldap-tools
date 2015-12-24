class Entry(object):
    def __init__(self, cn, ou):
        if len(cn) < 1:
            raise ValueError("Zero-length entry name")
        self.dn = "cn=%s,ou=%s,%s" % (cn,ou,DOMAIN)

class UserEntry(Entry):
    def __init__(self, cn):
        Entry.__init__(self, cn, 'Users')
        name = cn.split(' ')
        self.entry = {
            'cn' = [cn],
            'givenName' = [name[0]],
            'sn' = [name[1] if len(name) >= 2 else name[0]],
            'uid' = [string.lower(self.entry['givenName'][0][0]) +
                string.lower('sn'][0])
                if self.entry['givenName'] != self.entry['sn']
                else string.lower(self.entry['givenName'][0])],
            'gidNumber' = [GID],
            'homeDirectory' = [HOME + self.entry['uid'][0]],
            'loginShell' = [SHELL],
            'objectClass' = U_OBJECTS
        }

class GroupEntry(Entry):
    def __init__(self, cn):
        Entry.__init__(self, cn, 'Groups')
        self.entry = {
            'cn' = [cn]
            'objectClass' = G_OBJECTS
        }

class SudoEntry(Entry):
    def __init__(self, cn):
        Entry.__init__(self, cn, 'SUDOers')
        self.entry = {
            'cn' = [cn]
            'sudoUser' = [cn]
            'sudoCommand' = COMMANDS
            'sudoHost' = HOSTS
            'objectClass' = S_OBJECTS
        }

class EntryFactory:
