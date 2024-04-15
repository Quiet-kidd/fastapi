"""add content to post table

Revision ID: b6fd50b3b0dd
Revises: 9e17a3762099
Create Date: 2024-04-10 13:28:19.098736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b6fd50b3b0dd'
down_revision: Union[str, None] = '9e17a3762099'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
