# Connection defaults
PROTOCOL = 'ldaps'
FQDN = 'ldapmanager-prod-va.janrain.com'
PORT = '636'
CACERTFILE = '/etc/openldap/DigiCert_Global_Root_CA.crt'
BINDDN = 'cn=admin,dc=janrain,dc=com'

# Database defaults
BASE = 'dc=janrain,dc=com'

ORGANIZATIONAL_UNITS = {
    'users': 'Users',
    'groups': 'Groups',
    'sudoers': 'SUDOers'
}

# New user defaults
GID = '500'
HOME = '/home/'
SHELL = '/bin/bash'
U_OBJECTS = ['inetOrgPerson', 'posixAccount', 'ldapPublicKey', 'top']

# New group defaults
G_OBJECTS = ['posixGroup', 'top']

# New suoder defaults
S_OBJECTS = ['sudoRole', 'top']
COMMANDS = 'ALL'
HOSTS = 'ALL'
