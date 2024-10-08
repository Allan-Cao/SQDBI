from sqlalchemy import ForeignKey, String, Integer, BigInteger, DateTime, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from SQDBI.models import Base


class Game(Base):
    __tablename__ = "games"

    id: Mapped[str] = mapped_column(
        String(255), primary_key=True
    )  # Complete game id containing region and game id (e.g. EUW1_1234567890)
    game_id: Mapped[int] = mapped_column(BigInteger)  # Riot's game id
    platform_id: Mapped[str] = mapped_column(String(50))  # e.g. EUW1
    game_creation: Mapped[int | None] = mapped_column(BigInteger)
    game_start: Mapped[int | None] = mapped_column(BigInteger)
    game_end: Mapped[int | None] = mapped_column(BigInteger)
    game_duration: Mapped[int | None] = mapped_column(Integer)  # in seconds
    game_type: Mapped[str | None] = mapped_column(
        String(50)
    )  # This should be "SOLOQUEUE" for Queueid 420 games and SCRIM/ESPORTS for TR games
    patch: Mapped[str | None] = mapped_column(String(10))
    # NULL or 0 for Tournament Realm games
    queue_id: Mapped[int | None] = mapped_column(Integer)
    tournament_id: Mapped[str | None] = mapped_column(ForeignKey("tournaments.id"))
    game_number: Mapped[int | None] = mapped_column(Integer)
    update: Mapped[datetime | None] = mapped_column(DateTime, default=func.now())
