"""empty message

Revision ID: 42e61807095f
Revises: 5e16bd3ac7ef
Create Date: 2019-01-14 11:49:52.461555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42e61807095f'
down_revision = '5e16bd3ac7ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vendor_ratings', sa.Column('main_meal_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'vendor_ratings', 'meal_items', ['main_meal_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'vendor_ratings', type_='foreignkey')
    op.drop_column('vendor_ratings', 'main_meal_id')
    # ### end Alembic commands ###
