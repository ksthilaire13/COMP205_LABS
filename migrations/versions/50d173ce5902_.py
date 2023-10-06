"""empty message

Revision ID: 50d173ce5902
Revises: 
Create Date: 2023-10-06 19:01:09.610547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50d173ce5902'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('artist_name', sa.String(length=64), nullable=True),
    sa.Column('hometown', sa.String(length=64), nullable=True),
    sa.Column('genre', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('artist_id')
    )
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_artist_artist_name'), ['artist_name'], unique=True)
        batch_op.create_index(batch_op.f('ix_artist_description'), ['description'], unique=True)
        batch_op.create_index(batch_op.f('ix_artist_genre'), ['genre'], unique=True)
        batch_op.create_index(batch_op.f('ix_artist_hometown'), ['hometown'], unique=True)

    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('user_email', sa.String(length=64), nullable=True),
    sa.Column('user_password', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_user_email'), ['user_email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_user_password'), ['user_password'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('venue',
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('venue_name', sa.String(length=64), nullable=True),
    sa.Column('venue_address', sa.String(length=64), nullable=True),
    sa.Column('venue_description', sa.String(length=128), nullable=True),
    sa.Column('max_capacity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('venue_id')
    )
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_venue_max_capacity'), ['max_capacity'], unique=True)
        batch_op.create_index(batch_op.f('ix_venue_venue_address'), ['venue_address'], unique=True)
        batch_op.create_index(batch_op.f('ix_venue_venue_description'), ['venue_description'], unique=True)
        batch_op.create_index(batch_op.f('ix_venue_venue_name'), ['venue_name'], unique=True)

    op.create_table('event',
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('event_name', sa.String(length=64), nullable=True),
    sa.Column('event_date', sa.String(length=32), nullable=True),
    sa.Column('event_description', sa.String(length=128), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.venue_id'], ),
    sa.PrimaryKeyConstraint('event_id')
    )
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_event_event_date'), ['event_date'], unique=True)
        batch_op.create_index(batch_op.f('ix_event_event_description'), ['event_description'], unique=True)
        batch_op.create_index(batch_op.f('ix_event_event_name'), ['event_name'], unique=True)

    op.create_table('artist_to_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.artist_id'], ),
    sa.ForeignKeyConstraint(['event_id'], ['event.event_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artist_to_event')
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_event_event_name'))
        batch_op.drop_index(batch_op.f('ix_event_event_description'))
        batch_op.drop_index(batch_op.f('ix_event_event_date'))

    op.drop_table('event')
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_venue_venue_name'))
        batch_op.drop_index(batch_op.f('ix_venue_venue_description'))
        batch_op.drop_index(batch_op.f('ix_venue_venue_address'))
        batch_op.drop_index(batch_op.f('ix_venue_max_capacity'))

    op.drop_table('venue')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_user_password'))
        batch_op.drop_index(batch_op.f('ix_user_user_email'))

    op.drop_table('user')
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_artist_hometown'))
        batch_op.drop_index(batch_op.f('ix_artist_genre'))
        batch_op.drop_index(batch_op.f('ix_artist_description'))
        batch_op.drop_index(batch_op.f('ix_artist_artist_name'))

    op.drop_table('artist')
    # ### end Alembic commands ###
