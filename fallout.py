# list of candidate passwords
words = [
    'waltz',
    'educe',
    # 'laces',
    'louma',
    'agree',
    'lycea',
    'paeon',
    'pacer',
    'daces',
    'gager',
    'lyres',
    'halma',
    'pixel',
    'lycee',
    'laced',
    'lutea']

# guesses made
# (word, ltrs matched)
match_words = [
    # ('premen',4),
    # ('lancing',5),
    ('lycee',4)
    ]

# return # of letters that match between 2 words (a,b)
def word_match(a,b):
    c = 0
    for l in range(len(a)):
        if a[l] == b[l]:
            c+=1
    return c

def print_row(cols,colwidth=-1):
    if colwidth == -1:
        colwidth=[len(str(c)) for c in cols]
    row = '|'
    divider = '\n+'
    for i in range(len(cols)):
        row += ' '
        row += str(cols[i]).ljust(colwidth[i])
        row += ' |'
        divider +=  '-'*(colwidth[i]+2) + '+'
    return row+divider

# drop words that don't match
# ERROR: Dropping elements mid-loop is breaking it
new_words = []
for i in words:
    flag = 1
    for w in match_words:
        if word_match(i,w[0]) != w[1]:
            flag = 0
            break
    if flag:
        new_words.append(i)

words = new_words

# create dict of {word: [matches to other words]}
counts = {}
for i in words:
    counts[i] = []
    for j in words:
        if i == j:
            counts[i].append(-1)
        else:
            c = word_match(i,j)
            counts[i].append(c)
    # print('{0}: {1}'.format(i,counts[i]))

# freq is a dict of {word: {# of matches: how many words have this #}}
# e.g. if 5 words each match 'word' with 2 letters {'word': {2: 5}}
# max_freq is the largest number in freq (e.g. 5) for each word
# i.e. the "worst case scenario" if you choose that word and are wrong
freq = {}
max_freq = []
for i in counts:
    freq[i] = {}
    for j in counts[i]:
        freq[i].update({j: counts[i].count(j)})
    max_freq.append([ i, freq[i][max(freq[i],key=freq[i].get)] ])

for m in max_freq:
    print(print_row(m))
