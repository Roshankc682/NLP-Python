
"""
To see the word is a stop word or not
"""

import spacy
nlp = spacy.load('en_core_web_sm')
import nltk
nltk.download('stopwords')

print(nlp.Defaults.stop_words)
len(nlp.Defaults.stop_words)
"""
326
"""

nlp.vocab["hey"].is_stop
"""
False
"""

nlp.vocab["is"].is_stop
"""
True
"""

nlp.Defaults.stop_words.add("is")
nlp.vocab["hey"].is_stop
"""
False
"""

len(nlp.Defaults.stop_words)
"""
327
"""

nlp.vocab['is'].is_stop = False
