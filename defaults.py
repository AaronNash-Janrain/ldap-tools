# Connection defaults
PROTOCOL = 'ldaps'
FQDN = 'ldapmanager-prod-va.janrain.com'
PORT = '636'
CACERTFILE = '/etc/openldap/DigiCert_Global_Root_CA.crt'
BINDDN = 'cn=admin,dc=janrain,dc=com'

# Database defaults
BASE = 'dc=janrain,dc=com'

# Acceptable cli/file input to the correct entry (object) types
ENTRY_TYPES = ['user', 'group', 'sudoer']

# New user defaults
UOU = 'Users'
GID = '500'
HOME = '/home/'
SHELL = '/bin/bash'
U_OBJECTS = ['inetOrgPerson', 'posixAccount', 'ldapPublicKey', 'top']

# New group defaults
GOU = "Groups"
G_OBJECTS = ['posixGroup', 'top']

# New suoder defaults
SOU = 'SUDOers'
COMMANDS = 'ALL'
HOSTS = 'ALL'
S_OBJECTS = ['sudoRole', 'top']
