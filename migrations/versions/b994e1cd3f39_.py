"""empty message

Revision ID: b994e1cd3f39
Revises: 6c8403c8cd46
Create Date: 2023-10-09 21:25:24.470269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b994e1cd3f39'
down_revision = '6c8403c8cd46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('venue_city', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('venue_state', sa.String(length=2), nullable=True))
        batch_op.create_index(batch_op.f('ix_venue_venue_city'), ['venue_city'], unique=False)
        batch_op.create_index(batch_op.f('ix_venue_venue_state'), ['venue_state'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_venue_venue_state'))
        batch_op.drop_index(batch_op.f('ix_venue_venue_city'))
        batch_op.drop_column('venue_state')
        batch_op.drop_column('venue_city')

    # ### end Alembic commands ###