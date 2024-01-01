from pyramid.httpexceptions import HTTPFound
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from artauction.data import repository


@view_config(route_name='art', renderer='artauction:templates/home/art.pt', request_method='GET')
def art_get(request: Request):
    bidder_id = 1  # hardcoded but ideally user data cna come from cookie object (dictionary)
    bidder = repository.get_bidder_by_id(bidder_id, True)

    art_id = int(request.matchdict.get('art_id'))
    art = repository.get_art_by_id(art_id, True)
    if not art:
        return Response(status=404)

    highest_bid = 0
    for bid in art.bids:
        if bid.bid_offer > highest_bid:
            highest_bid = bid.bid_offer

    return {
        'bidder': bidder,
        'art': art,
        'highest_bid': highest_bid,
        'error': None
    }


@view_config(route_name='art', renderer='artauction:templates/home/art.pt', request_method='POST')
def art_post(request: Request):
    bidder_id = 1  # hardcoded but ideally user data cna come from cookie object (dictionary)
    bidder = repository.get_bidder_by_id(bidder_id, True)

    art_id = int(request.matchdict.get('art_id'))
    art = repository.get_art_by_id(art_id, True)
    if not art:
        return Response(status=404)

    highest_bid = 0
    for bid in art.bids:
        if bid.bid_offer > highest_bid:
            highest_bid = bid.bid_offer

    bid_offer = float(request.POST.get('bid_offer', -1))
    if bid_offer < 0:
        error = 'Invalid bid offer value:'

        return {
            'bidder': bidder,
            'art': art,
            'highest_bid': highest_bid,
            'error': error,
            'bid_offer': bid_offer
        }
    elif bid_offer > bidder.funds:
        error = 'Insufficient funds for bid offer:'

        return {
            'bidder': bidder,
            'art': art,
            'highest_bid': highest_bid,
            'error': error,
            'bid_offer': bid_offer
        }

    bid = repository.get_bid_by_bidder_id_art_id(bidder_id, art_id)
    if not bid:
        bid = repository.create_bid(art, bidder, bid_offer)
    else:
        bid = repository.update_bid(bid.id, art, bidder, bid_offer)

    if bid.status == "CLOSED":
        return HTTPFound(location='/account/collection/{}'.format(bidder_id))
    else:
        return HTTPFound(location='/account/bids/{}'.format(bidder_id))

