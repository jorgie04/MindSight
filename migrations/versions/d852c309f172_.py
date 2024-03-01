"""empty message

Revision ID: d852c309f172
Revises: 3a2cf4b26f88
Create Date: 2024-03-01 23:09:47.999595

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd852c309f172'
down_revision = '3a2cf4b26f88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_information', schema=None) as batch_op:
        batch_op.drop_column('gpa')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_information', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gpa', mysql.FLOAT(), nullable=True))

    # ### end Alembic commands ###
