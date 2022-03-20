import re
import string
from typing import List
from .stemmer import Porter

PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))


def tokenize(query: str) -> List[str]:
    return query.split()


def to_lower_case(query: List[str]) -> List[str]:
    return [el.lower() for el in query]


def stem_filter(query: List[str]) -> List[str]:
    return [Porter.stem(word) for word in query]


def punctuation_filter(query: List[str]) -> List[str]:
    return [PUNCTUATION.sub('', token) for token in query]


def check_stopwords(query: List[str]) -> List[str]:
    return [w for w in query if len(w) > 3]


def analize(query):
    query = tokenize(query)
    query = to_lower_case(query)
    query = check_stopwords(query)
    query = stem_filter(query)
    query = punctuation_filter(query)

    return [t for t in query if t]
