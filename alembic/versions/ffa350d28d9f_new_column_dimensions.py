"""new column dimensions

Revision ID: ffa350d28d9f
Revises: 4c40f3e66462
Create Date: 2023-03-25 22:02:57.912061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffa350d28d9f'
down_revision = '4c40f3e66462'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('dimensions', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'dimensions')
    # ### end Alembic commands ###
