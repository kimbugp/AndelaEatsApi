"""empty message

Revision ID: cfeef5d4b2cd
Revises: a5dcf891bf4f
Create Date: 2019-03-21 15:10:53.459941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfeef5d4b2cd'
down_revision = 'a5dcf891bf4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meal_sessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('name', sa.Enum('breakfast', 'lunch', name='mealsessionnames'), nullable=True),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('stop_time', sa.Time(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('vendors', sa.Column('average_rating', sa.Float(), nullable=False, default=0))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vendors', 'average_rating')
    op.drop_table('meal_sessions')
    # ### end Alembic commands ###