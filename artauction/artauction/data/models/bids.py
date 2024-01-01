import datetime
import sqlalchemy
from sqlalchemy import orm
from artauction.data.modelbase import SqlAlchemyBase


class Bid(SqlAlchemyBase):
    __tablename__ = 'bids'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    status = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)
    bid_offer = sqlalchemy.Column(sqlalchemy.Float, default=0, index=True, nullable=False)

    bidder_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('bidders.id'), nullable=False)
    # ont-to-one
    bidder = orm.relationship('Bidder', back_populates='bids')

    art_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('arts.id'), nullable=False)
    # ont-to-one
    art = orm.relationship('Art', back_populates='bids')


