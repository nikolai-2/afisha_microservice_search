from typing import List

from app.models.event import EventCard
from app.search.db_operations import load_db
from app.search.filter import analize
from app.search.index import Index


class Searcher:
    def __init__(self,
                 query: str,
                 sort_by: str = "popularity"):

        self._query = query
        self._sort = sort_by
        self._index = Index()

    def search(self) -> List[EventCard]:
        bd_data = load_db()

        self._index.index_data(bd_data)
        self.analize_query()
        frequence_list = self.get_frequence()
        success_list = self.get_success(frequence_list)

        print(print(frequence_list), len(frequence_list), len(success_list))

        return to_event_card(success_list)

    def analize_query(self):
        self._query = list(set(analize(self._query)))

    def get_frequence(self):
        index_list = []
        for token in self._query:
            elements_list = self._index.index.get(token, [])
            if not elements_list: continue

            for element in elements_list:
                analized_element_text = analize(element.element.get_full_text())
                koef = analized_element_text.count(token)
                element.rank = element.rank * koef/2
                index_list.append(element)

        return self._filter_frequence(index_list)

    @staticmethod
    def _get_frequence_keys(frequence_list):
        elements = []
        for element in frequence_list:
            print(type(element))
            if element not in elements:
                elements.append(element.element)
        print('elements', elements)
        return elements

    def _filter_frequence(self, frequence_list):
        db_elements = self._get_frequence_keys(frequence_list)

        filtered_frequence_list = []
        for k in db_elements:
            print(list(filter(lambda x: x.element == k, frequence_list)))
            v = sum(map(lambda x: x.rank, filter(lambda x: x.element == k, frequence_list)))
            filtered_frequence_list.append((k, v))

        return sorted(filtered_frequence_list, key=lambda x: x[1], reverse=True)

    def get_success(self, frequence_list):
        return [x[0] for x in frequence_list if x[1] > 1.5 * len(self._query)]


def to_event_card(bd_data) -> List[EventCard]:
    event_card_list = []

    for bd_row in bd_data:
        event_card_list.append(
            EventCard(id=bd_row.event_id,
                      image=bd_row.event_image,
                      channel=bd_row.channel_name,
                      name=bd_row.event_name,
                      startDate=bd_row.event_start_date,
                      endDate=bd_row.event_end_date,
                      period=bd_row.event_period)
        )

    return event_card_list

