from pyramid.request import Request
from pyramid.view import view_config

from artauction.data import repository


@view_config(route_name='home', renderer='artauction:templates/home/home.pt')
def home(request: Request):
    bidder_id = 1  # hardcoded but ideally user data cna come from cookie object (dictionary)
    bidder = repository.get_bidder_by_id(bidder_id, True)
    arts_for_auction = repository.get_arts_for_auction(True)
    arts_open_for_auction = []
    for art in arts_for_auction:  # this is better don in SQL and use SQLAlchemy Core
        open = True
        for bid in art.bids:
            if bid.status == "CLOSED":
                open = False
                break
        if open:
            arts_open_for_auction.append(art)

    return {
        'bidder': bidder,
        'arts': arts_open_for_auction  # you can also filter here using list comprehension
    }
