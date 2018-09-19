'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", 
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", 
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

dictionary = ['the', 'quick', 'brown', 'fox', 'bed', 'bedbath', 'and', 'beyond', 'bath']

def search_dict(string):
	global dictionary
	words = []

	for i in range(0, len(string)):
		for j in range(i + 1, len(string) + 1):
			word = string[i : j]
			if word in dictionary and word not in words:
				words.append(word)
				i = j + 1

	if words:
		return words
	else:
		return 

print(search_dict('thequickbrownfox'))
print(search_dict('bedbathandbeyond'))
print(search_dict('permanaharianja'))