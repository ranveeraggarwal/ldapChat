'''
Python 2.7.8
pip install python-ldap
'''

import ldap

conn = ldap.initialize('ldap://ldap.iitb.ac.in')
search_result = conn.search_s('dc=iitb,dc=ac,dc=in', ldap.SCOPE_SUBTREE, 'uid=d.s.rathor', ['uid','employeeNumber'])

'''
Search result will be like
search_result = [('uid=d.s.rathor,ou=UG,ou=CSE,ou=People,dc=iitb,dc=ac,dc=in',
  {'employeeNumber': ['120050033'], 'uid': ['d.s.rathor']})]
  
search_result[0][0] = 'uid=d.s.rathor',ou=UG,ou=CSE,ou=People,dc=iitb,dc=ac,dc=in'
'''

authenticated = False
rollNumber = ''
try:
    authenticate = conn.bind_s(search_result[0][0],'password')
    authenticated = True
    rollNumber = search_result[0][1]['employeeNumber'][0]
    print rollNumber
except ldap.INVALID_CREDENTIALS:
    print "your credentials are not correct"


    
