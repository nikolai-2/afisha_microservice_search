from dataclasses import dataclass


@dataclass
class EventCard:
    id: int
    image: str
    channel: str
    name: str
    startDate: float
    endDate: float = None
    period: str = None

    def __repr__(self):
        return f'<{self.id} {self.name} {self.startDate}>'