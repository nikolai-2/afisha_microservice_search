import random
from typing import List, Optional

from sqlalchemy import text
from app.database import engine
import config
from app.models.db import DBData

QUERY_FILE_PATH = config.BaseConfig.BASE_PATH + '/app/search/sql/query.sql'


def check_tags_names(tags_names) -> List[Optional[str]]:
    if not isinstance(tags_names, list): return []

    tags_names = [x for x in tags_names if x]
    if not tags_names: return []

    return tags_names


def load_db():

    with open(QUERY_FILE_PATH, 'r') as sql_file:
        result = engine.execute(text(sql_file.read()))
    for r in result:
        yield DBData(event_id=r.event_id,
                     event_image=r.event_image,
                     event_period=r.event_period,
                     event_name=r.event_name,
                     event_text=r.event_text,
                     event_place=r.event_place,
                     event_start_date=r.event_start_date,
                     event_end_date=r.event_end_date,
                     channel_name=r.channel_name,
                     counter=r.counter,
                     tags=check_tags_names(r.tags_names))
