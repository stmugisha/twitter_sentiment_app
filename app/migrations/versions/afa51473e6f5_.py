"""empty message

Revision ID: afa51473e6f5
Revises: 
Create Date: 2020-10-20 13:46:22.825671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afa51473e6f5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('keywords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('keyword', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tweets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tweet', sa.String(), nullable=True),
    sa.Column('user', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.Integer(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('tweets')
    op.drop_table('keywords')
    # ### end Alembic commands ###
