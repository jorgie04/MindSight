"""empty message

Revision ID: 5749c163ad83
Revises: 494383cf7e09
Create Date: 2023-10-31 00:29:07.365010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5749c163ad83'
down_revision = '494383cf7e09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('college',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('college_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['college_id'], ['college.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('course')
    op.drop_table('college')
    # ### end Alembic commands ###