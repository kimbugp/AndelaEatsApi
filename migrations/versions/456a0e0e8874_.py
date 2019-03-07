"""empty message

Revision ID: 456a0e0e8874
Revises: 5826d1bca108
Create Date: 2019-03-07 10:12:31.268155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '456a0e0e8874'
down_revision = '5826d1bca108'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('faqs', 'question')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('faqs', sa.Column('question', sa.VARCHAR(length=2000), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
