"""Updates players table typing and adds disambiguation column

Revision ID: e0d2bbbb17aa
Revises: 454b10b69772
Create Date: 2024-07-27 23:06:25.096662

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e0d2bbbb17aa"
down_revision: Union[str, None] = "454b10b69772"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "players", sa.Column("disambiguation", sa.String(length=255), nullable=True)
    )
    op.alter_column(
        "players", "name", existing_type=sa.VARCHAR(length=255), nullable=False
    )
    op.create_unique_constraint(None, "players", ["disambiguation"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "players", type_="unique")
    op.alter_column(
        "players", "name", existing_type=sa.VARCHAR(length=255), nullable=True
    )
    op.drop_column("players", "disambiguation")
    # ### end Alembic commands ###
