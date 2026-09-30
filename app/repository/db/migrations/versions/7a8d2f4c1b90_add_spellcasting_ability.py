"""add_spell_char

Revision ID: 7a8d2f4c1b90
Revises: f0a4e56301c7
Create Date: 2026-09-29

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '7a8d2f4c1b90'
down_revision: Union[str, None] = 'f0a4e56301c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, None] = None


spell_char = postgresql.ENUM(
    'INT', 'WIS', 'CHA', name='spell_char'
)


def upgrade() -> None:
    spell_char.create(op.get_bind(), checkfirst=True)
    op.add_column(
        'd_class',
        sa.Column('spell_char', spell_char, nullable=True)
    )
    op.alter_column('d_class', 'spell_char', nullable=False)


def downgrade() -> None:
    op.drop_column('d_class', 'spell_char')
    spell_char.drop(op.get_bind(), checkfirst=True)