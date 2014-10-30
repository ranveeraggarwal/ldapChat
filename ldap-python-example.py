'''
Python 2.7.8
pip install python-ldap
'''

import ldap

conn = ldap.initialize('ldap://ldap.iitb.ac.in')
search_result = ldap.search_s('dc=iitb,dc=ac,dc=in', ldap.SCOPE_SUBTREE, 'uid=d.s.rathor', ['uid','employeeNumber'])

'''
Search result will be like
search_result = [('uid=d.s.rathor,ou=UG,ou=CSE,ou=People,dc=iitb,dc=ac,dc=in',
  {'employeeNumber': ['120050033'], 'uid': ['d.s.rathor']})]
  
search_result[0][0] = 'uid=d.s.rathor',ou=UG,ou=CSE,ou=People,dc=iitb,dc=ac,dc=in'
'''

authenticated = False
try:
    authenticate = ldap.bind_s('search_result[0][0],'password')
    authenticated = True
except ldap.INVALID_CREDENTIALS:
    print "your credentials are not correct"


    
