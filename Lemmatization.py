import spacy
nlp = spacy.load('en_core_web_sm')

string8 = nlp(u'Nepal is beautiful country located in Himalayes sides.!.is that show ?')
for token in string8:
  print(token.text, '\t', token.pos_,'\t', token.lemma_, '\t', token.lemma_)

"""
OUTPUT : Nepal 	 PROPN 	 Nepal 	 Nepal
		is 	 AUX 	 be 	 be
		beautiful 	 ADJ 	 beautiful 	 beautiful
		country 	 NOUN 	 country 	 country
		located 	 VERB 	 locate 	 locate
		in 	 ADP 	 in 	 in
		Himalayes 	 PROPN 	 Himalayes 	 Himalayes
		sides.!.is 	 VERB 	 sides.!.i 	 sides.!.i
		that 	 DET 	 that 	 that
		show 	 NOUN 	 show 	 show
		? 	 PUNCT 	 ? 	 ?
"""


def show_lemmatization(text):
  for token in text:
    print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_}')

string8 = nlp(u'Nepal is beautiful country located in Himalayes sides.!.is that show ?')
show_lemmatization(string8)
show_lemmatization(nlp(u"hey hey i love you anish"))