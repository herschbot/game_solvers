from nltk.corpus import words
import sys

min_len = 5
all_words = words.words()

if len(sys.argv) > 1:
	letters = sys.argv[1]
# else, use the default letters
else:
	# required letter first
    letters = 'oafilrw'

for w in all_words:
    valid = True
    for l in w:
        if l not in letters:
            valid = False
            break
    if valid and letters[0] in w and len(w) >= min_len:
        print(w)
