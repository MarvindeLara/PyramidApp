"""Adds bidders.loan column

Revision ID: 26aa987ed6ad
Revises: dea2d165d130
Create Date: 2023-08-24 14:56:47.320101

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26aa987ed6ad'
down_revision: Union[str, None] = 'dea2d165d130'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bidders', sa.Column('loan', sa.Float(), nullable=True))
    op.create_index(op.f('ix_bidders_loan'), 'bidders', ['loan'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bidders_loan'), table_name='bidders')
    op.drop_column('bidders', 'loan')
    # ### end Alembic commands ###
