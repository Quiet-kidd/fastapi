"""add last few columns  to post table

Revision ID: 62e04d1edbb9
Revises: f376c04b37fe
Create Date: 2024-04-10 16:12:05.329201

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62e04d1edbb9'
down_revision: Union[str, None] = 'f376c04b37fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published',sa.Boolean(), nullable= False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts', 'created_at')
    pass
