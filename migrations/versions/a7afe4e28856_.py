"""empty message

Revision ID: a7afe4e28856
Revises: 8814988415fe
Create Date: 2024-03-02 16:11:20.111040

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a7afe4e28856'
down_revision = '8814988415fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('substance_abuse_history', schema=None) as batch_op:
        batch_op.add_column(sa.Column('benzo_way_of_intake', sa.String(length=50), nullable=True))
        batch_op.drop_column('benzo__way_of_intake')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('substance_abuse_history', schema=None) as batch_op:
        batch_op.add_column(sa.Column('benzo__way_of_intake', mysql.VARCHAR(length=50), nullable=True))
        batch_op.drop_column('benzo_way_of_intake')

    # ### end Alembic commands ###
