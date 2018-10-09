import pickle
from collections import Counter


class Query:

    def __init__(self):
        self.index = None
        try:
            with open('DISK/BLOCKINDEX.pickle', 'rb') as pickle_file:
                self.index = pickle.load(pickle_file)
        except FileNotFoundError:
            print('cant find it.')

    def search_term(self, term):
        try:
            return sorted(self.index[term])
        except KeyError:
            return []

    def search_AND(self, query):
        query_term_list = query.split(',')
        posting_lists = []
        for term in query_term_list:
            posting_lists.append(self.search_term(term))
        result = set(posting_lists[0])
        for posting in posting_lists[1:]:
            result.intersection_update(posting)
        return sorted(list(result))

    def search_OR(self, query):
        query_term_list = query.split(',')
        result = []
        for term in query_term_list:
            result = result + self.search_term(term)
        return [item[0] for item in Counter(result).most_common()]

    def is_built(self):
        return self.index is not None


