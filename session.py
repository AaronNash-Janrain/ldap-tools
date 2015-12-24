import ldap, defaults

# See http://www.python-ldap.org/doc/html/ldap.html

class Session:
    def __init__(self):
        self.url = defaults.PROTOCOL + '://' + defaults.FQDN + ':' + defaults.PORT
        self.connection = ldap.initialize(self.url)
        self.connection.protocol_version = ldap.VERSION3
        self.connection.set_option(ldap.OPT_X_TLS_CACERTFILE, defaults.CACERTFILE)


    def open(self, passwd, binddn = None):
        self.connection.simple_bind_s(
            defaults.BINDDN if binddn == None else binddn, passwd
        )

    def close(self):
        self.connection.unbind_s()

    def search(self, scope, filter):
        return self.connection.search_s(defaults.BASE, scope, filter)

    def add(self, dn, modlist):
        return self.connection.add_s(dn, modlist)

    def modify(self, dn, modlist):
        return self.connection.modify_s(dn, modlist)

    def delete(self, dn):
        return self.connection.delete_s(dn)

def add_list(entry):
    return ldap.modlist.addModlist(entry)

def modify_list(old_entry, new_entry):
    return ldap.modlist.modifyModlist(old_entry, new_entry)
