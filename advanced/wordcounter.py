from collections import Counter

text = "The genre has also been described as possessing \"a continuous and comprehensive history of about two thousand years\"." \
       "[1] This view sees the novel's origins in Classical Greece and Rome, medieval, early modern romance, " \
       "and the tradition of the novella. The latter, an Italian word used to describe short stories, " \
       "supplied the present generic English term in the 18th century. Ian Watt, however, " \
       "in The Rise of the Novel (1957) suggests that the novel first came into being in the early 18th century,"

words = text.split()
counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)