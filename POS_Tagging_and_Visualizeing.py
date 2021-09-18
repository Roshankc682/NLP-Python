import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Nepal is amazing place with greate people")

for token in doc:
  print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
"""
OUTPUT :  Nepal Nepal PROPN NNP nsubj Xxxxx True False
is be AUX VBZ ROOT xx True True
amazing amazing ADJ JJ amod xxxx True False
place place NOUN NN attr xxxx True False
with with ADP IN prep xxxx True True
greate greate ADJ JJ amod xxxx True False
people people NOUN NNS pobj xxxx True False
"""





"""
Create a simple Doc object
"""
doc = nlp(u"Nepal is amazing place with greate people")

print(doc.text)
"""
OUTPUT : Nepal is amazing place with greate people
"""
"""
Print the fourth word and associated tags
"""
print(doc[4].text, doc[4].pos_, doc[4].tag, spacy.explain(doc[4].tag_))
"""
OUTPUT: with ADP 1292078113972184607 conjunction, subordinating or preposition
"""



doc = nlp(u"I have Gone Through different Phase !")
r = doc[2]

print(f'{r.text} {r.pos_} {r.tag_} {spacy.explain(r.tag_)}')
"""
OUTPUT : Gone VERB VBN verb, past participle
"""



doc = nlp(u"I have Gone Through different Phase !")
POS_counts = doc.count_by(spacy.attrs.POS)
for k,v in sorted(POS_counts.items()):
  print(f'{k}. {doc.vocab[k].text} {v}')




import spacy
nlp = spacy.load('en_core_web_sm')
from spacy import displacy

doc = nlp(u"I have Gone Through different Phase !")
displacy.render(doc,style='dep',jupyter=True,options={'distance':100})


