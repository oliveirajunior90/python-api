"""primary key on id user

Revision ID: 76411c597a01
Revises: cc2ab5277de2
Create Date: 2022-02-17 19:31:21.832745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76411c597a01'
down_revision = 'cc2ab5277de2'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('users')
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
