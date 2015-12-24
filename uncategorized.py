#!/usr/bin/env python

import sys, ldap, json, argparse, getpass, string
from ldif import LDIFParser, LDIFWriter

class LDIFOperator(LDIFParser):
    def __init__(self, input):
        LDIFParser.__init__(self, input)

    def write(self, dn, entry):
        LDIFWriter(sys.stdout).unparse(dn, entry)

class FileOperator:
    def file_open(path):
        return open(path, 'r')

    def file_read(file):
        try:
            data = json.load(file)
        except ValueError:
            try:
                data = LDIFOperator(file).parse()
            except ValueError as e:
                print "Input file must be in JSON or LDIF format: " + e
        return data

class LDAPAgent():
    def __init__(self):
        self.server = ldap.initialize(URL + ':' + PORT)

parser = argparse.ArgumentParser(description = "Manage LDAP users and groups")

parser.add_argument('entity type', choices = ['group', 'user', 'sudoer'])
parser.add_argument('action', choices = ['add', 'remove', 'modify'])
parser.add_argument('-r', '--read', action = 'store', dest = 'file')
parser.add_argument('-o', '--output', choices = ['ldif', 'json'],
    action = 'store', dest = 'output')
parser.add_argument('-d', '--dry-run', action = 'store_true', dest = 'dry_run',
    default = False)

args = parser.parse_args()
