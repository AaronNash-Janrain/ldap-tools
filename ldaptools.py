#!/usr/bin/env python
#
# Author: Aaron Nash

import sys, json, argparse, entries, ldifutils, defaults

def num_entries(s):
    gathered = s.split(':', 1)
    if len(gathered) <= 1:
        gathered.append(1)
    try:
        gathered[1] = int(gathered[1])
        if gathered[0] in defaults.ENTRY_TYPES and gathered[1] >= 1:
            return gathered[0], gathered[1]
        else:
            raise Exception
    except Exception:
        raise argparse.ArgumentTypeError("Accepts input in the form of user|group|sudoer[:N>0]")

def make_interactive(entry_list, bill):
    entry_list = []
    print "Creating %s %s entries. Attributes left 'empty' will not be included in entry." % (str(bill[1]), bill[0])
    for i in range(0, bill[1]):
        updates = []
        name = raw_input("Name of new %s: " % bill[0])
        entry = entries.EntryFactory.create_entry(bill[0], name)
        entry.populate_defaults()
        print "Creating dn: %s" % entry['dn']
        print "Update values or press Enter to accept defaults\n"
        for key in entry['entry']:
            if key != 'objectClass':
                temp_value = raw_input("%s (%s): " % (key, entry['entry'][key][0]))
                if temp_value != '': updates.append((key, [temp_value]))
        print
        if len(updates) > 0: entry.update(updates)
        entry_list.append(entry)
    return entries.EntryCollection(entry_list = entry_list)

def init_add(args):
    # Do general setup tasks
    #init(args)
    new_entries = []
    collection = None
    # Read in existing entries from input file if -r
    # ...
    # Check the types/number of entries read and walk through prompt for each entry if -i
    if args.interactive != None:
        collection = make_interactive(new_entries, args.interactive)
    # Append to LDIF file if -d
    out = ldifutils.Unparser(
        sys.stdout
        if args.ldif_out_path == None
        else open(args.ldif_out_path, 'w')
    )
    if collection != None:
        for entry in collection['entries']:
            out.write(entry['dn'], ldifutils.get_add_mod_list(entry['entry']))
    if args.ldif_out_path != None: print "LDIF written to %s" % args.ldif_out_path
    # Overwrite JSON file if -j
    # ...

def init_delete(args):
    raise NotImplementedError
    # TODO

def init_modify(args):
    raise NotImplementedError
    # TODO

def init_move(args):
    raise NotImplementedError
    # TODO

option_n = {
    'action': 'store_true',
    'default': False,
    'help': "don't actually attempt server execution"
}

option_i = {
    'action': 'store',
    'dest': 'interactive',
    'type': num_entries,
    'metavar': "user|group|sudoer[:N>0]",
    'default': None,
    'help': "create/edit/validate one or more entries interactively"
}

option_d = {
    'action': 'store',
    'dest': 'ldif_out_path',
    'metavar': 'PATH',
    'default': None,
    'help': "write the resulting LDIFs to a file at PATH instead of stdout (if the file already exists any new entries will be appended to any existing entries)"
}

option_j = {
    'action': 'store',
    'dest': 'json_out_path',
    'metavar': 'PATH',
    'default': None,
    'help': "write a JSON representation of the resulting LDIFs to a file at PATH (if the file already exists any new entries will be appended to any existing entries)"
}

# Global parser and arguments
parser_ldap = argparse.ArgumentParser(
    prog = 'ldap', description = 'Manage LDAP users, groups and sudoers'
)

# Add parsers for subcommands
subparsers = parser_ldap.add_subparsers(dest = 'subparser_name', help = 'sub-command help')

# Sub parser and arguments for adding entries
parser_add = subparsers.add_parser('add-entries', help = 'add-entries help')
parser_add.add_argument('-n', **option_n)
parser_add.add_argument('-i', **option_i)
parser_add.add_argument('-d', **option_d)
parser_add.add_argument('-j', **option_j)
# add arguments here...
parser_add.set_defaults(func = init_add)

# Sub parser and arguments for deleting entries
parser_delete = subparsers.add_parser('delete-entries', help = 'delete-entries help')
parser_delete.add_argument('-n', **option_n)
parser_delete.add_argument('-i', **option_i)
parser_delete.add_argument('-d', **option_d)
parser_delete.add_argument('-j', **option_j)
# add arguments here...
parser_delete.set_defaults(func = init_delete)

# Sub parser and arguments for modifying entry attributes
parser_modify = subparsers.add_parser('modify-entries', help = 'modify-entries help')
parser_modify.add_argument('-n', **option_n)
parser_modify.add_argument('-i', **option_i)
parser_modify.add_argument('-d', **option_d)
parser_modify.add_argument('-j', **option_j)
# add arguments here...
parser_modify.set_defaults(func = init_modify)

# Sub parser and arguments for renaming/moving/copying entries
parser_move = subparsers.add_parser('move-entries', help = 'move-entries help')
parser_move.add_argument('-n', **option_n)
parser_move.add_argument('-i', **option_i)
parser_move.add_argument('-d', **option_d)
parser_move.add_argument('-j', **option_j)
# add arguments here...
parser_move.set_defaults(func = init_move)

args = parser_ldap.parse_args()
args.func(args)
