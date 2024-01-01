import datetime
import random

from artauction.data.db_session import DbSession
from artauction.data.models.bidders import Bidder
from artauction.data.models.arts import Art


def load_starter_data():
    __import_bidders()
    __import_arts()
    # __import_bids() don't need this, just add bids through ?


def __import_bidders():
    session = DbSession.create_session()
    if session.query(Bidder).count() > 0:
        return

    bidder = Bidder()
    bidder.full_name = 'Marvin DeLara'
    bidder.funds = 98400
    bidder.email = 'marvin.swdev@gmail.com'
    bidder.hashed_password = '1234'
    session.add(bidder)

    session.commit()
    session.close()


def __import_arts():
    session = DbSession.create_session()
    if session.query(Art).count() > 0:
        return

    titles = [
        'Wa9ilX9XYOI',
        'WKQt_X-SKFI',
        'Ql6JhGdbQg0',
        'z-lh7Mz7wFQ',
        'YzamNB_T4WQ',
        'DwYrHrOpG6U',
        'Tg8KhzS-b8w',
        'wuD9Xb3dUZs',
        'qgWUv52K6Fk',
        '6YP8nTssV2k',
        'xXPXAVu-Ufg',
        'hSkbqHnt-g4',
        'qDZ-Xd8dX6w',
        'vSGBVxbLOMU',
        'ze_aQiu3ZFU',
        'OPE3qT-l2gc',
        'W1Usc1JLwJ8',
        '7mBOyYTrxBA',
        '6YP8nTssV2k',
        'R9MeGDvj-hM',
        'Rhj7g7Cs4mg',
        'AP-29z0BTmA',
        'kznh8gbL-LU',
        'ZP1laOmploQ',
    ]

    year = [
        '1924',
        '1935',
        '1948',
        '1957',
        '1969',
        '1964',
        '1857',
        '1884',
        '2011',
        '1995',
        '1974',
        '1973',
        '1987',
        '1992',
        '2006',
        '2000',
        '2020',
        '2023',
        '2017',
    ]

    tags = [
        'https://source.unsplash.com/Wa9ilX9XYOI',
        'https://source.unsplash.com/WKQt_X-SKFI',
        'https://source.unsplash.com/Ql6JhGdbQg0',
        'https://source.unsplash.com/z-lh7Mz7wFQ',
        'https://source.unsplash.com/YzamNB_T4WQ',
        'https://source.unsplash.com/DwYrHrOpG6U',
        'https://source.unsplash.com/Tg8KhzS-b8w',
        'https://source.unsplash.com/wuD9Xb3dUZs',
        'https://source.unsplash.com/qgWUv52K6Fk',
        'https://source.unsplash.com/6YP8nTssV2k',
        'https://source.unsplash.com/xXPXAVu-Ufg',
        'https://source.unsplash.com/hSkbqHnt-g4',
        'https://source.unsplash.com/qDZ-Xd8dX6w',
        'https://source.unsplash.com/vSGBVxbLOMU',
        'https://source.unsplash.com/ze_aQiu3ZFU',
        'https://source.unsplash.com/OPE3qT-l2gc',
        'https://source.unsplash.com/W1Usc1JLwJ8',
        'https://source.unsplash.com/7mBOyYTrxBA',
        'https://source.unsplash.com/6YP8nTssV2k',
        'https://source.unsplash.com/R9MeGDvj-hM',
        'https://source.unsplash.com/Rhj7g7Cs4mg',
        'https://source.unsplash.com/AP-29z0BTmA',
        'https://source.unsplash.com/kznh8gbL-LU',
        'https://source.unsplash.com/a-painting-of-pink-and-yellow-flowers-on-a-white-background-ZP1laOmploQ',
    ]

    COUNT = 24
    for _ in range(0, COUNT):
        art = Art()
        art.artist = "Marvin DeLara"
        selected = random.choice(titles)
        art.title = selected
        titles.remove(selected)
        art.year = random.choice(year)
        art.description = 'Lorem ipsum dolor amet bushwick banh mi irony sustainable twee slow-carb whatever iPhone austin kale chips.'
        selected = random.choice(tags)
        art.tag = selected
        tags.remove(selected)
        art.price = round(random.uniform(10000.00, 200000.00), 2)

        session.add(art)

    session.commit()
    session.close()
