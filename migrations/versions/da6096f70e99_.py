"""empty message

Revision ID: da6096f70e99
Revises: dbe2ee43f2fc
Create Date: 2019-03-14 19:19:28.709497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da6096f70e99'
down_revision = 'dbe2ee43f2fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hall',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('h_num', sa.String(length=32), nullable=True),
    sa.Column('h_mode', sa.String(length=32), nullable=True),
    sa.Column('h_seats', sa.String(length=256), nullable=True),
    sa.Column('h_cinema', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['h_cinema'], ['cinema.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hall')
    # ### end Alembic commands ###
