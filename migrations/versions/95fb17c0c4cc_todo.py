"""'todo'

Revision ID: 95fb17c0c4cc
Revises: c0246302ffc1
Create Date: 2019-05-28 16:11:38.920917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95fb17c0c4cc'
down_revision = 'c0246302ffc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('detail', sa.String(length=300), nullable=True),
    sa.Column('is_completed', sa.Boolean(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['type_id'], ['todo_type.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    op.drop_table('todo_type')
    # ### end Alembic commands ###
