"""add user table

Revision ID: ad50cd177b56
Revises: b6fd50b3b0dd
Create Date: 2024-04-10 13:34:04.216651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad50cd177b56'
down_revision: Union[str, None] = 'b6fd50b3b0dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(),nullable=False),
        sa.Column('email', sa.String(),nullable=False),
        sa.Column('password', sa.String(),nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
        )
    pass


def downgrade():
    op.drop_table('users')
    pass
