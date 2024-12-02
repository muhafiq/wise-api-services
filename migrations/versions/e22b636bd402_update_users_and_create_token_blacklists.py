"""update users and create token_blacklists

Revision ID: e22b636bd402
Revises: 6a0911c495e9
Create Date: 2024-11-25 16:16:56.147268

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e22b636bd402'
down_revision = '6a0911c495e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token_blacklists',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('jti', sa.String(length=255), nullable=False),
    sa.Column('revoked', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('jti')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('refresh_token')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('refresh_token', mysql.TEXT(), nullable=True))

    op.drop_table('token_blacklists')
    # ### end Alembic commands ###