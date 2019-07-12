"""empty message

Revision ID: 76002e80a642
Revises: 8dff842c714a
Create Date: 2019-07-19 11:43:54.836785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76002e80a642'
down_revision = '8dff842c714a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu_template',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu_template_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('day', sa.Enum('monday', 'tuesday', 'wednesday', 'thursday', 'friday', name='weekdays'), nullable=False),
    sa.Column('meal_period', sa.Enum('lunch', 'breakfast', name='mealperiods'), nullable=False),
    sa.Column('main_meal_id', sa.Integer(), nullable=False),
    sa.Column('allowed_side', sa.Integer(), nullable=True),
    sa.Column('allowed_protein', sa.Integer(), nullable=True),
    sa.Column('side_items', sa.String(), nullable=False),
    sa.Column('protein_items', sa.String(), nullable=False),
    sa.Column('templateId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['main_meal_id'], ['meal_items.id'], ),
    sa.ForeignKeyConstraint(['templateId'], ['menu_template.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menu_template_item')
    op.drop_table('menu_template')
    # ### end Alembic commands ###
