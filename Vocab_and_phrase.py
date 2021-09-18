"""
import lib
"""
import spacy
nlp = spacy.load('en_core_web_sm')



"""
Import PhraseMatcher
"""
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab, attr='LOWER')


terms = ["Swedish","girl","Tattoo","Millennium"]
patterns = [nlp(text) for text in terms]
matcher.add("Amazing ",None,*patterns)



text_doc = nlp("The Girl with the Dragon Tattoo (original title in Swedish: Män som hatar kvinnor, lit. 'Men Who Hate Women') is a psychological thriller novel by Swedish author and journalist Stieg Larsson (1954–2004), which was published posthumously in 2005 to become an international bestseller.[1] It is the first book of the Millennium series.")
matches = matcher(text_doc)
print(matches)
"""
OUTPUT : [(4703956757523288825, 1, 2), (4703956757523288825, 5, 6), (4703956757523288825, 10, 11), (4703956757523288825, 33, 34), (4703956757523288825, 62, 63)]
"""

match_id,start,end = matches[2]
print(nlp.vocab.strings[match_id], text_doc[start:end])

"""
OUTPUT : Amazing  Swedish
"""