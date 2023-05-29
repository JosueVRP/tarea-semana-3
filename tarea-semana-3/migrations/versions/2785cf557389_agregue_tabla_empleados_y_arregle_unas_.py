"""agregue tabla empleados y arregle unas cosas

Revision ID: 2785cf557389
Revises: 920235e63caa
Create Date: 2023-05-28 21:19:24.761467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2785cf557389'
down_revision = '920235e63caa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('last_name', sa.Text(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['area_id'], ['areas.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###