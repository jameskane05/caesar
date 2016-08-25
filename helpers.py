def alphabet_position(char):
	if char.isupper():
		return ord(char) - 65
	if char.islower():
		return ord(char) - 97

def rotate_character(char, rot):
	if not char.isalpha():
		return char
	if char.isupper():
		return chr(((alphabet_position(char) + rot) % 26) + 65)
	if char.islower():
		return chr(((alphabet_position(char) + rot) % 26) + 97)
