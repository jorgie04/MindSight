"""empty message

Revision ID: b8e721dcddc3
Revises: 9065800bb67b
Create Date: 2023-10-31 01:27:01.238579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8e721dcddc3'
down_revision = '9065800bb67b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_information', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_name', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('first_name', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_information', schema=None) as batch_op:
        batch_op.drop_column('first_name')
        batch_op.drop_column('last_name')

    # ### end Alembic commands ###
