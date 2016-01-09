"""empty message

Revision ID: 3ce8378f4b1
Revises: 4ac103a941a
Create Date: 2015-12-26 18:02:40.332398

"""

# revision identifiers, used by Alembic.
revision = '3ce8378f4b1'
down_revision = '4ac103a941a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role', sa.String(length=20), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'role')
    ### end Alembic commands ###