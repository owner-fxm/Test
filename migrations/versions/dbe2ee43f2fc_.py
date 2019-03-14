"""empty message

Revision ID: dbe2ee43f2fc
Revises: 3ff5227377d4
Create Date: 2019-03-14 17:58:34.916928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbe2ee43f2fc'
down_revision = '3ff5227377d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cinema', sa.Column('c_user', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'cinema', 'cinema_user', ['c_user'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cinema', type_='foreignkey')
    op.drop_column('cinema', 'c_user')
    # ### end Alembic commands ###