"""Add user model2

Revision ID: ba160cbfe5da
Revises: c962c8fe834e
Create Date: 2026-11-04 16:01:13.834898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba160cbfe5da'
down_revision: Union[str, Sequence[str], None] = 'c962c8fe834e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('products', sa.Column('seller_id', sa.Integer(), nullable=True))

    op.execute(
        "INSERT INTO users (email, hashed_password, is_active, role) "
        "SELECT 'default@example.com', 'x', true, 'user' "
        "WHERE NOT EXISTS (SELECT 1 FROM users)"
    )
    op.alter_column('products', 'seller_id', nullable=False)
    op.create_foreign_key(
        'fk_products_seller_id', 'products', 'users', ['seller_id'], ['id']
    )


def downgrade() -> None:
    op.drop_constraint('fk_products_seller_id', 'products', type_='foreignkey')
    op.drop_column('products', 'seller_id')