from typing import Optional

from sqlalchemy.orm import subqueryload

from artauction.data.db_session import DbSession
from artauction.data.models.bidders import Bidder
from artauction.data.models.arts import Art
from artauction.data.models.bids import Bid


def get_bidder_by_id(bidder_id: int, include_bids=True) -> Optional[Bidder]:
    session = DbSession.create_session()
    try:
        if not include_bids:
            return session.query(Bidder).filter(Bidder.id == bidder_id).first()
        else:
            return session.query(Bidder) \
                .options(subqueryload(Bidder.bids)) \
                .filter(Bidder.id == bidder_id) \
                .first()
    finally:
        session.close()


def get_arts_for_auction(include_bids=True) -> Optional[Art]:
    session = DbSession.create_session()
    try:
        if not include_bids:
            return session.query(Art).all()
        else:
            return session.query(Art) \
                .options(subqueryload(Art.bids)) \
                .all()
    finally:
        session.close()


def get_art_by_id(art_id: int, include_bids=True) -> Optional[Art]:
    session = DbSession.create_session()
    try:
        if not include_bids:
            return session.query(Art).filter(Art.id == art_id).first()
        else:
            return session.query(Art) \
                .options(subqueryload(Art.bids)) \
                .filter(Art.id == art_id) \
                .first()
    finally:
        session.close()


def create_bid(art: Art, bidder: Bidder, bid_offer: float) -> Bid:
    session = DbSession.create_session()
    session.expire_on_commit = False

    try:
        bid = Bid()
        bid.status = "CLOSED" if bid_offer >= art.price else "OPEN"
        if bid.status == "CLOSED":
            update_bidder(bidder.id, bid_offer)
        bid.bid_offer = bid_offer
        bid.bidder = bidder
        bid.art = art
        session.add(bid)

        session.commit()
    finally:
        session.close()

    return bid


def update_bid(bid_id: int, art: Art, bidder: Bidder, bid_offer: float) -> Bid:
    session = DbSession.create_session()
    session.expire_on_commit = False

    try:
        bid = session.query(Bid).filter(Bid.id == bid_id).one()
        bid.status = "CLOSED" if bid_offer >= art.price else "OPEN"
        if bid.status == "CLOSED":
            update_bidder(bidder.id, bid_offer)
        bid.bid_offer = bid_offer

        session.commit()
    finally:
        session.close()

    return bid


def update_bidder(bidder_id: int, bid_offer: float) -> Bidder:
    session = DbSession.create_session()
    session.expire_on_commit = False

    try:
        bidder = session.query(Bidder).filter(Bidder.id == bidder_id).one()
        bidder.funds = bidder.funds - bid_offer

        session.commit()
    finally:
        session.close()

    return bidder


def get_bid_by_bidder_id_art_id(bidder_id: int, art_id: int) -> Bid:
    session = DbSession.create_session()
    try:
        return session.query(Bid) \
            .filter(Bid.bidder_id == bidder_id, Bid.art_id == art_id) \
            .first()
    finally:
        session.close()

