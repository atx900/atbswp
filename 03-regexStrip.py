'''
Practice Project 03: Regex Strip

Objective(s):
- Write a function that takes a string and does the same thing as the strip() string method.
	- If no other arguments are passed other than the string to strip, the whitespace characters will be removed from the
	  beginning and end of the string.
	- Otherwise, the characters specified in the second argument of the function will be removed.
'''
import re

def regexStrip(string, target):

	if string == '':														# terminates the program if no string entered
		print('regexStrip: No specified string, terminating program.')
		return 0

	if target == '':														# removes starting & ending whitespace if no target specified
		print()
		print('regexStrip: No target word specified, removing beginning & ending whitespace characters.')

		spaceBeginRegex = re.compile(r'^\s')
		try:
			matchObj = spaceBeginRegex.sub('', string)
			string = matchObj

			spaceEndRegex = re.compile(r'\s$')
			try:
				matchObj = spaceEndRegex.sub('', string)
				string = matchObj

				print('regexStrip: String\'s beginning & ending whitespaces removed. ')
				print('regexStrip: Updated string = "' + matchObj + '"')

			except AttributeError:
				print('regexStrip: No ending whitespace found.')

		except AttributeError:
			print('regexStrip: No beginning whitespace found.')

	else:

		replaceRegex = re.compile(target)									# removes target word from string
		try:
			matchObj = replaceRegex.search(string).group()
			matchObj = replaceRegex.sub('', string)
			print('regexStrip: Target word "' + target + '" removed from the string.')
			print('regexStrip: Updated string = "' + matchObj + '"')

		except AttributeError:
			print('regexStrip: The target word "' + target + '" is not found in the string.')


print('Enter a string: ')
userString = input()														# accepts user-defined string

print('Enter word to remove from string: ')
targetWord = input()														# accepts user-defined target word to be removed from string

regexStrip(userString, targetWord)
