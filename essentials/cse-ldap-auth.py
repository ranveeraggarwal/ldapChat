'''
Python 2.7.8
pip install python-ldap
'''

import sys,ldap

CACERTFILE='/home/nitin/ldapChat/cse-cacert.pem'

ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_DEMAND)
ldap.set_option(ldap.OPT_X_TLS_CACERTFILE, CACERTFILE)

#{1,2,3,4}.ldap.cse.iitb.ac.in
conn = ldap.initialize('ldap://2.ldap.cse.iitb.ac.in')

conn.protocol_version= ldap.VERSION3

#if connection is not present this will throw error
#if error try connecting with some other server (1/2/3/4)
conn.start_tls_s()

#First search for username and bindDN through conn.search_s
result = conn.search_s('dc=cse,dc=iitb,dc=ac,dc=in', ldap.SCOPE_SUBTREE, 'uid=ntnchandrol', ['uid','employeeNumber', 'cn'])
password = 'ntnchandrol'

if(len(result) < 1):
    print "No username found"
else:
	print result
#stop code here and return un-authorized user

'''
result should be:
[('uid=dheerendra,ou=ug12,ou=UG,ou=Students,ou=People,dc=cse,dc=iitb,dc=ac,dc=in',
  {'cn': ['Dheerendra Singh Rathor'],
   'employeeNumber': ['120050033'],
   'uid': ['dheerendra']})]
'''

bindDN = result[0][0]
name = result[0][1]['cn'][0]
rollNumber = result[0][1]['employeeNumber'][0]
username = result[0][1]['uid'][0]

'''
Binding (authenticating) in try catch
If invalid credentials then it will throw ldap.INVALID_CREDENTIALS error
'''
authenticated = False
try:
    bind = conn.bind_s(result[0][0],password,ldap.AUTH_SIMPLE)
    authenticated=True
except ldap.INVALID_CREDENTIALS:
    print "you are not a valid user here"

