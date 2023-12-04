"""tenant table defined

Revision ID: 7ca65a4288bf
Revises: a012c2c4f702
Create Date: 2023-12-04 17:05:38.127414

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7ca65a4288bf'
down_revision = 'a012c2c4f702'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'tenants',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('first_name', sa.String(), nullable=False),
        sa.Column('last_name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('address_1', sa.String(), nullable=False),
        sa.Column('address_2', sa.String(), nullable=False),
        sa.Column('phone_1', sa.String(), nullable=False),
        sa.Column('phone_2', sa.String(), nullable=False),
        sa.Column('CNIC', sa.String(length=15), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('id')
    )
    op.add_column('contracts', sa.Column('tenant_id', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_unique_constraint(None, 'contracts', ['tenant_id'])
    op.create_foreign_key(None, 'contracts', 'tenants', ['tenant_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tenants_in', type_='unique')
    op.drop_constraint(None, 'contracts', type_='foreignkey')
    op.drop_column('contracts', 'tenant_id')
    op.drop_table('tenants')
    # ### end Alembic commands ###