# -----------------------------------------------------------------------------
# pparse.py
#
# Simple parser for ANSI C.  Based on the grammar in K&R, 2nd Ed.
# ----------------------------------------------------------------------------

import sys
import os
import plex
import ply.yacc as yacc

# Get the token map
tokens = plex.tokens

# enum-specifier:

def p_enum_specifier(t):
	'enum_specifier : ENUM ID LBRACE enumerator_list RBRACE SEMI'
	pass

# enumerator_list:
def p_enumerator_list_1(t):
    'enumerator_list : enumerator'
    pass

def p_enumerator_list_2(t):
    'enumerator_list : enumerator_list COMMA enumerator'
    pass

# enumerator:
def p_enumerator_1(t):
    'enumerator : ID'
    pass

def p_enumerator_2(t):
    'enumerator : ID EQUALS ICONST'
    pass
	


def p_error(t):
    print("Whoa. We're hosed",t)

import profile
# Build the grammar

yacc.yacc()
#yacc.yacc(method='LALR',write_tables=False,debug=True)

#profile.run("yacc.yacc(method='LALR')")

filename = "com.p"

yacc.parse(open(filename).read())
