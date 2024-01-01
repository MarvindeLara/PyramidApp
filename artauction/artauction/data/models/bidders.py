import datetime
import sqlalchemy
from sqlalchemy import orm
from artauction.data.modelbase import SqlAlchemyBase
from artauction.data.models.bids import Bid


class Bidder(SqlAlchemyBase):
    __tablename__ = 'bidders'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    full_name = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=True)
    funds = sqlalchemy.Column(sqlalchemy.Float, default=0.0, index=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=True, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True, index=True)
    last_login = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    loan = sqlalchemy.Column(sqlalchemy.Float, default=0.0, index=True)

    # many-to-one
    bids = orm.relationship('Bid', order_by=[Bid.created_date.desc()], back_populates='bidder')
