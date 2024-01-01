from math import ceil

from pyramid.httpexceptions import HTTPFound
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from artauction.data import repository


@view_config(route_name='collection', renderer='artauction:templates/home/collection.pt')
def bids(request: Request):
    bidder_id = int(request.matchdict.get('bidder_id'))
    bidder = repository.get_bidder_by_id(bidder_id, True)
    closed_bids = []

    row_bid = {0: None, 1: None}
    for bid in bidder.bids:
        if bid.status == "CLOSED":
            art = repository.get_art_by_id(bid.art_id, False)
            if not row_bid[0]:
                row_bid[0] = (bid, art)
            elif not row_bid[1]:
                row_bid[1] = (bid, art)
            if row_bid[0] and row_bid[1]:
                closed_bids.append(row_bid)
                row_bid = {0: None, 1: None}

    if row_bid[0]:  # for last incomplete row
        closed_bids.append(row_bid)

    return {
        'bidder': bidder,
        'closed_bids': closed_bids
    }

