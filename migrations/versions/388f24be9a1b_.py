"""empty message

Revision ID: 388f24be9a1b
Revises: afa51473e6f5
Create Date: 2020-10-20 13:53:28.282052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '388f24be9a1b'
down_revision = 'afa51473e6f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tweets', sa.Column('intent', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tweets', 'intent')
    # ### end Alembic commands ###
