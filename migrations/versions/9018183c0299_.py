"""empty message

Revision ID: 9018183c0299
Revises: 67db41d1b07d
Create Date: 2021-05-20 22:23:04.311213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9018183c0299'
down_revision = '67db41d1b07d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rental',
    sa.Column('rental_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('video_id', sa.Integer(), nullable=True),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['video.id'], ),
    sa.PrimaryKeyConstraint('rental_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rental')
    # ### end Alembic commands ###