"""
Write a function to display basic entity info
"""
import spacy
nlp = spacy.load('en_core_web_sm')
def show_ent(doc):
  if doc.ents:
    for ent in doc.ents:
      print(ent.text + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))
  else:
    print("Blank Doc")


doc = nlp(u'Hey this is Roshan and i am very good in programming python !')
show_ent(doc)

"""
OUTPUT : Roshan - PERSON - People, including fictional
"""