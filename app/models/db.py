from dataclasses import dataclass


@dataclass
class DBData:
    event_id: int
    event_name: str
    event_text: str
    event_place: str
    event_start_date: int
    event_image: str
    channel_name: str
    tags: list
    counter: int
    event_end_date: int = None
    event_period: int = None

    def get_full_text(self):
        return '\n'.join([self.event_name,
                          self.event_text,
                          self.event_place,
                          ','.join(self.tags),
                          self.channel_name])