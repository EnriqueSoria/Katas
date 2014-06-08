__author__ = 'nRikee'

import random
import sys

# Variables
lang_input = [ 'R', 'A', 'M', 'V', 'N', 'I' ]
lang_OK_POS = 'X'
lang_NO_POS = '*'

seq_size = 4    # Size of the passord
max_times = 12

# Verbose
system_var = 'guest@secretlab:~$ sudo rm -rf /'
system_win = 'Correct password! Logged as drevil\ndrevil@secretlab:~$ rm -rf /\n\tSucces!'
system_fail = 'Incorrect password. Shutting down the system and calling Mr.Evil... Wait there!\n' \
			  'guest@secretlab:~$ exit\nProcess finished with exit code 1'

# Choose a new random password
def new_pass ( ):
	aux = lang_input
	password = ''

	for i in range ( seq_size ):
		chosen = random.choice ( aux )
		password += chosen
		aux.remove ( chosen )
	return password


# Check passowrd
def check_pass ( user, password ):
	aux = ''
	for tpla in zip ( user, password ):
		if tpla [ 0 ] == tpla [ 1 ]:
			aux += lang_OK_POS
		elif tpla [ 0 ] in password:
			aux += lang_NO_POS
	return ''.join ( sorted ( [ r for r in aux ], reverse=True ) )

# Main code
passwd = new_pass ( )
print 'Welcome to Mr. Evil super secret lab.'
for i in range ( max_times ):
	# Input
	user = raw_input ( system_var + '\n\tIntroduce security code.\n' )
	user.capitalize ( )

	ret = check_pass ( user, passwd )

	if ret == 'XXXX':
		print system_win
		sys.exit ( 0 )
	else:
		print ret
		
print system_fail
