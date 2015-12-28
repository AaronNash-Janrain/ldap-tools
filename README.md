User and group management tools for LDAP

Besides being used to represent entries in the ldap database, LDIF files are
also used to manipulate one or more entries in the database when they include
the changetype directive (this directive is recognized by the ldapmodify
command included in ldap-utils). The tree below provides a visual
representation of the operations that can be performed on ldap entries via the
generated ldif files created by this tool.

changetype
|
|__ add (entry)
|
|__ delete (entry)
|
|__ modify (entry)
|  |
|  |__ add (attribute)
|  |
|  |__ delete (attribute)
|  |
|  |__ replace (attribute)
|
|__ modrdn (entry)
   |
   |__ newrdn (rename entry)
   |
   |__ newrdn & newsuperior & deleterdn (rename/move/copy entry)

default rdn attrtibute when applicable: cn (common name)
