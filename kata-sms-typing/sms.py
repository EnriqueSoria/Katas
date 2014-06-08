# Developed in Python 2.7

__author__ = 'nRikee'

numpad = [ '-_:0', '.; 1', 'abc2', 'def3', 'ghi4', 'jkl5', 'mno6', 'pqrs7', 'tuv8', 'wxyz9' ]

def decode ( string ):
	simplified = '' + string[0]
	for n in string[1:]:
		if n.isdigit():
			if not n == simplified[-1]:
				simplified += ' '
			simplified += n
		else:
			simplified += ' '

	decoded = ''
	for token in simplified.split():
		pad = numpad [ int ( token [ 0 ] ) ]
		i = ( len(token) - 1 ) % len ( pad )
		decoded += pad [ i ]
	return decoded


def encode ( string ):
	coded = ''
	for char in string:
		for key in numpad:
			if char in key:
				number = str ( numpad.index ( key ) )
				times = key.index ( char ) + 1
				coded += number * times + ' '
				break;
	return coded

print decode( encode ( 'it simply works' ) )
