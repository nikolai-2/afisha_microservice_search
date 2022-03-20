import random

from sqlalchemy import text
from app.database import engine
import config
from app.models.db import DBData

QUERY_FILE_PATH = config.BaseConfig.BASE_PATH + '/app/search/sql/query.sql'


def load_db():
    event_names = ['изготовление мормышек',
                   'разработка браузера на ассемблере',
                   'подъем в горы',
                   'иммитация программирования',
                   'Горы и скалы']
    event_texts = ['Что такое вообще эти ваши мормышки?',
                   'Я просто извращенец и пишу браузер ']
    event_places = []
    channel_names = []
    tags_names = []
    for i in range(5):
        yield DBData(event_id=i+1,
                     event_image='pass',
                     event_period=random.randint(1, 2 ** 4),
                     event_name=event_names[i],
                     event_text=event_texts[i],
                     event_place=event_places[i],
                     event_start_date=random.randint(1, 100),
                     event_end_date=random.randint(80, 200),
                     channel_name=channel_names[i],
                     tags=tags_names[i])


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
                     tags=r.tags_names)
