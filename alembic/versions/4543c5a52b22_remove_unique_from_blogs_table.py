"""remove unique from blogs table

Revision ID: 4543c5a52b22
Revises: af1e9e92af95
Create Date: 2023-09-13 17:25:06.767677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4543c5a52b22'
down_revision = 'af1e9e92af95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('blogs_user_id_key', 'blogs', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('blogs_user_id_key', 'blogs', ['user_id'])
    # ### end Alembic commands ###
