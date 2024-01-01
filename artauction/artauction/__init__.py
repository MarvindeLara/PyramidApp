import os

from pyramid.config import Configurator

# need to ALWAYS import relative to artauction
from artauction.data.db_session import DbSession
from artauction.bin import load_base_data


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        config.include('.routes')
        config.scan()

    init_db()

    return config.make_wsgi_app()


def init_db():
    db_file = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'db',
        'art_auction.sqlite'
    )
    DbSession.global_init(db_file)
    load_base_data.load_starter_data()
