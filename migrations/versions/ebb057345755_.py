"""empty message

Revision ID: ebb057345755
Revises: eefa9bc46c39
Create Date: 2024-01-19 11:58:57.093651

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ebb057345755'
down_revision = 'eefa9bc46c39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_registration', schema=None) as batch_op:
        batch_op.add_column(sa.Column('userid', sa.Integer(), nullable=True))
        batch_op.drop_constraint('user_registration_ibfk_2', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['userid'], ['user_id'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_registration', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('user_registration_ibfk_2', 'user', ['user_id'], ['user_id'])
        batch_op.drop_column('userid')

    # ### end Alembic commands ###
