from pyramid.httpexceptions import HTTPFound
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from artauction.data import repository


@view_config(route_name='bids', renderer='artauction:templates/home/bids.pt')
def bids(request: Request):
    bidder_id = int(request.matchdict.get('bidder_id'))
    bidder = repository.get_bidder_by_id(bidder_id, True)
    open_bids = []
    closed_bids = []

    for bid in bidder.bids:
        if bid.status == "OPEN":
            art = repository.get_art_by_id(bid.art_id, True)

            art_open = True
            highest_bid = 0
            for art_bid in art.bids:
                if art_bid.bid_offer > highest_bid:
                    highest_bid = art_bid.bid_offer
                if art_open:
                    if art_bid.status == "OPEN":
                        continue
                    elif art_bid.status == "CLOSED" and art_bid.bidder_id != bidder_id:
                        art_open = False

            if art_open:
                open_bids.append((bid, art, highest_bid))
            else:
                closed_bids.append((bid, art, highest_bid))

    return {
        'bidder': bidder,
        'open_bids': open_bids,
        'closed_bids': closed_bids
    }

