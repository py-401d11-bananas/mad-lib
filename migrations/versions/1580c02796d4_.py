"""empty message

Revision ID: 1580c02796d4
Revises: 
Create Date: 2019-03-18 20:14:11.815920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1580c02796d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('preset_story',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('content', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('content')
    )
    op.create_index(op.f('ix_preset_story_title'), 'preset_story', ['title'], unique=True)
    op.create_table('user_stories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('content', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('content')
    )
    op.create_index(op.f('ix_user_stories_title'), 'user_stories', ['title'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_user_stories_title'), table_name='user_stories')
    op.drop_table('user_stories')
    op.drop_index(op.f('ix_preset_story_title'), table_name='preset_story')
    op.drop_table('preset_story')
    # ### end Alembic commands ###
