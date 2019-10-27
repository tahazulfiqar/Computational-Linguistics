import nltk
import helper

g = helper.merge(["Grammar", "Lexicon"])

grammar = nltk.grammar.CFG.fromstring(g)


#print(grammar)
print('Test Positives')
helper.autotest('Positive', grammar)
print('Test Negatives')
helper.autotest('Negative', grammar)

#helper.manutest(grammar)