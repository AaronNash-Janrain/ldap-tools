#!/usr/bin/env python
#
# Author: Aaron Nash

import argparse

entry_types = ['user', 'group', 'sudoer']

def num_entries(s):
    gathered = s.split(':', 1)
    if len(gathered) <= 1:
        gathered.append(1)
    try:
        gathered[1] = int(gathered[1])
        if gathered[0] in entry_types and gathered[1] >= 1:
            return gathered[0], gathered[1]
        else:
            raise Exception
    except Exception:
        raise argparse.ArgumentTypeError("Accepts 'ENTRY-TYPE' | 'ENTRY-TYPE:N(>0)'")

def init(args):
    # TODO

def init_add(args):
    # Do general setup tasks
    init(args)
    new_entry_list = []
    if args.interactive != None:


def init_delete(args):
    # Do general setup tasks
    init(args)
    # TODO

def init_modify(args):
    # Do general setup tasks
    init(args)
    # TODO

def init_move(args):
    # Do general setup tasks
    init(args)
    # TODO

def add_interactive

# Global parser and arguments
parser_ldap = argparse.ArgumentParser(
    prog = 'ldap', description = 'Manage LDAP users, groups and sudoers'
)
parser_ldap.add_argument(
    '-n', action = 'store_true', default = False,
    help = "don't actually attempt server execution"
)
parser_ldap.add_argument(
    '-d', action = 'store', dest = 'ldif_out_path', metavar = 'PATH',
    help = """write the resulting LDIF to a file at PATH
            (if the file already exists any new entries will be appended to any existing entries)"""
)
parser_ldap.add_argument(
    '-j', action = 'store', dest = 'json_out_path', metavar = 'PATH',
    help = """write a JSON representation of the resulting LDIF to a file at PATH
            (if the file already exists any new entries will be appended to any existing entries)"""
)

# Add parsers for subcommands
subparsers = parser_ldap.add_subparsers(dest = 'subparser_name', help = 'sub-command help')

# Sub parser and arguments for adding entries
parser_add = subparsers.add_parser('add-entries', help = 'add-entries help')
parser_add.add_argument(
    '-i', action = 'store', dest = 'interactive', type = num_entries,
    metavar = 'ENTRY-TYPE:N(>0)', default = None,
    help = "create or edit one or more entries interactively"
)
parser_add.set_defaults(func = init_add)

# Sub parser and arguments for deleting entries
parser_delete = subparsers.add_parser('delete-entries', help = 'delete-entries help')
# add arguments here...
parser_delete.set_defaults(func = init_delete)

# Sub parser and arguments for modifying entry attributes
parser_modify = subparsers.add_parser('modify-entries', help = 'modify-entries help')
# add arguments here...
parser_modify.set_defaults(func = init_modify)

# Sub parser and arguments for renaming/moving/copying entries
parser_move = subparsers.add_parser('move-entries', help = 'move-entries help')
# add arguments here...
parser_move.set_defaults(func = init_move)

args = parser_ldap.parse_args()
args.func(args)
