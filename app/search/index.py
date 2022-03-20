from app.search.db_operations import load_db
from app.search.filter import analize


class IndexElement:
    def __init__(self, element, rank):
        self.element = element
        self.rank = rank

    def __repr__(self):
        return f'<{self.element} {self.rank}>'


class Index:

    def __init__(self):
        self.index = {}

    def index_subelement(self, subelement, element, rank: int):

        for token in analize(subelement):
            if token not in self.index:
                self.index[token] = list()
            self.index[token].append(IndexElement(element, rank))

    def index_element(self, element):

        self.index_subelement(element.channel_name, element, 20)
        for tag in element.tags:
            self.index_subelement(tag, element, 18)
        self.index_subelement(element.event_name, element, 15)
        self.index_subelement(element.event_text, element, 4)
        self.index_subelement(element.event_place, element, 7)

    def index_data(self, bd_data: load_db):
        for element in bd_data:
            self.index_element(element)