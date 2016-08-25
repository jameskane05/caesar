from helpers import rotate_character, alphabet_position
from sys import argv, exit

def encrypt(text,rot):
	#if not user_input_is_valid(argv):
	#	exit("usage: python3 caesar.py n")
	#else:
		#text = input("Type a message:\n")
	encrypted_text = ""
	for char in text:
		if char == " ":
			encrypted_text += char
		else: encrypted_text += rotate_character(char,int(rot))
	return encrypted_text

def user_input_is_valid(cl_args):
	if not len(cl_args) == 2:
		return False
	if not cl_args[1].isdigit():
		return False
	else: return True
