from ex48.parser import Sentence as Sen

mySen = Sen()
mySen.parse_sentence([('verb', 'run'), ('direction', 'north')])

print(mySen.subject)
print(mySen.verb)
print(mySen.object)

