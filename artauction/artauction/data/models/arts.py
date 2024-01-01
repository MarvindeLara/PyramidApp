import datetime
import sqlalchemy
from sqlalchemy import orm
from artauction.data.modelbase import SqlAlchemyBase


class Art(SqlAlchemyBase):
    __tablename__ = 'arts'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    artist = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)
    title = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)
    year = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)
    tag = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)
    price = sqlalchemy.Column(sqlalchemy.Float, default=0, index=True, nullable=False)
    owner = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=True)

    # many-to-one
    bids = orm.relationship('Bid', back_populates='art')

