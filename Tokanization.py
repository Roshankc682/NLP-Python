import string
import re
text = "I\'m a man of who love python from Nepal! wow.This is amazing i loved it yes.it\'s is indeed"
words = re.split(r'\W+',text)
print(words[:100])

"""
OUTPUT : ['I', 'm', 'a', 'man', 'of', 'who', 'love', 'python', 'from', 'Nepal', 'wow', 'This', 'is', 'amazing', 'i', 'loved', 'it', 'yes', 'it', 's', 'is', 'indeed', '']

"""


words = text.split()
re_punc = re.compile('[%s]'% re.escape(string.punctuation))
stripped = [re_punc.sub('',w) for w in words]
print(stripped[:100])

"""
OUTPUT : ['Im', 'a', 'man', 'of', 'who', 'love', 'python', 'from', 'Nepal', 'wowThis', 'is', 'amazing', 'i', 'loved', 'it', 'yesits', 'is', 'indeed']

"""


re_print = re.compile('[^%s]' % re.escape(string.printable))
result = [re_print.sub('', w) for w in words]
print(result)

"""
OUTPUT :["I'm", 'a', 'man', 'of', 'who', 'love', 'python', 'from', 'Nepal!', 'wow.This', 'is', 'amazing', 'i', 'loved', 'it', "yes.it's", 'is', 'indeed!']


"""


import spacy
nlp = spacy.load('en_core_web_sm')
string = "I\'m a man of who love python from Nepal! wow.This is amazing i loved it yes.it\'s is indeed!"
doc = nlp(string)
for token in doc:
  print(token.text,end=' | ')

"""
OUTPUT : I | 'm | a | man | of | who | love | python | from | Nepal | ! | wow | . | This | is | amazing | i | loved | it | yes.it | 's | is | indeed | ! |

"""

doc3 = nlp(u"we're the one from other world! don\'t be afraid we willn\'t eat instead \
will conduct experiment how those complex life formed in first place.If you have any question then mail me test@gmail.com")
for t in doc3:
  print(t)
# print(len(doc3))
# print(doc3.vocab)

"""
OUTPUT :  Character in new line

"""

string8 = nlp(u'Nepal is beautiful country located in Himalayes sides.')
for  token in string8:
  print(token.text, end=' | ')
for ent in string8.ents:
  print(ent.text+' - '+ent.label_+' - '+ str(spacy.explain(ent.label_)))


"""
OUTPUT : Nepal | is | beautiful | country | located | in | Himalayes | sides | . | Himalayes - ORG - Companies, agencies, institutions, etc.

"""

string8 = nlp(u'Nepal is beautiful country located in Himalayes sides.')
for  token in string8.noun_chunks:
  print(token.text, end=' | ')



"""
OUTPUT : Nepal | beautiful country | Himalayes sides | 


"""

from spacy import displacy

doc = nlp(u'Nepal is beautiful country located in Himalayes sides.')
displacy.render(doc,style='dep',jupyter=True,options={'distance':100})


"""
OUTPUT : Design in Graph

"""

from spacy import displacy

doc = nlp(u'Nepal is beautiful country located in Himalayes sides.')
displacy.render(doc,style='ent',jupyter=True)


"""
OUTPUT : Nepal is beautiful country located in Himalayes ORG sides.

"""

from spacy import displacy
doc = nlp(u'Nepal is beautiful country located in Himalayes sides.')
displacy.serve(doc,style='ent')


"""
OUTPUT : Host in local address

"""
