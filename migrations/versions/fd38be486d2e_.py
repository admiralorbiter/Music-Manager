"""empty message

Revision ID: fd38be486d2e
Revises: 
Create Date: 2024-08-10 17:31:22.536245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd38be486d2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('spotify_track', schema=None) as batch_op:
        batch_op.add_column(sa.Column('spotify_id', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('artist_ids', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('helper', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('added_by', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('added_at', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('genres', sa.String(length=1000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('spotify_track', schema=None) as batch_op:
        batch_op.drop_column('genres')
        batch_op.drop_column('added_at')
        batch_op.drop_column('added_by')
        batch_op.drop_column('helper')
        batch_op.drop_column('artist_ids')
        batch_op.drop_column('spotify_id')

    # ### end Alembic commands ###
